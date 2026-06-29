import feedparser
from database import SessionLocal
from models import Resource

FEEDS = [
    {"url": "https://devops.com/feed/",                    "source": "devops.com",       "type": "article"},
    {"url": "https://thenewstack.io/feed/",                "source": "thenewstack.io",   "type": "article"},
    {"url": "https://www.docker.com/blog/feed/",           "source": "docker-blog",      "type": "article"},
    {"url": "https://kubernetes.io/feed.xml",              "source": "kubernetes-blog",  "type": "article"},
    {"url": "https://www.hashicorp.com/blog/feed.xml",     "source": "hashicorp-blog",   "type": "article"},
    {"url": "https://grafana.com/blog/news/index.xml",     "source": "grafana-blog",     "type": "article"},
    {"url": "https://www.jenkins.io/blog/rss.xml",         "source": "jenkins-blog",     "type": "article"},
]

TAG_MAP = {
    "docker":         ["docker", "dockerfile", "docker compose"],
    "containers":     ["container", "docker", "podman"],
    "kubernetes":     ["kubernetes", "k8s", "kubectl", "helm", "pod"],
    "orchestration":  ["orchestration", "kubernetes", "k8s"],
    "terraform":      ["terraform", "hashicorp"],
    "iac":            ["infrastructure as code", "iac", "terraform"],
    "infrastructure": ["infrastructure"],
    "jenkins":        ["jenkins"],
    "cicd":           ["ci/cd", "cicd", "continuous integration", "continuous deployment", "pipeline"],
    "grafana":        ["grafana", "dashboard"],
    "prometheus":     ["prometheus", "promql", "metrics"],
    "monitoring":     ["monitoring", "observability", "alerting"],
    "ansible":        ["ansible", "playbook"],
    "automation":     ["automation", "ansible"],
    "aws":            ["aws", "amazon web services", "ec2", "s3", "eks"],
    "devops":         ["devops", "sre", "site reliability"],
}

def assign_tags(title: str, description: str) -> list:
    text = f"{title} {description or ''}".lower()
    tags = set()
    for tag, keywords in TAG_MAP.items():
        if any(kw in text for kw in keywords):
            tags.add(tag)
    return list(tags)

def crawl():
    db = SessionLocal()
    added = 0
    for feed_config in FEEDS:
        print(f"Crawling {feed_config['source']}...")
        feed = feedparser.parse(feed_config["url"])
        for entry in feed.entries:
            url = entry.get("link", "").strip()
            if not url:
                continue
            if db.query(Resource).filter_by(url=url).first():
                continue
            title       = entry.get("title", "").strip()
            description = entry.get("summary", "").strip()
            tags        = assign_tags(title, description)
            db.add(Resource(
                title=title,
                url=url,
                description=description[:500] if description else None,
                source=feed_config["source"],
                type=feed_config["type"],
                tags=tags if tags else None,
            ))
            added += 1
    db.commit()
    db.close()
    print(f"Crawl complete. {added} new resource(s) added.")

if __name__ == "__main__":
    crawl()
