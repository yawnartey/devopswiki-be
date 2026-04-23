from database import SessionLocal
from models import Resource

seed_data = [
    # Docker
    {
        "title": "Docker Official Documentation",
        "url": "https://docs.docker.com",
        "description": "Official Docker docs covering installation, images, containers, and networking.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["docker", "containers"]
    },
    {
        "title": "Docker Getting Started Tutorial",
        "url": "https://docs.docker.com/get-started/",
        "description": "Step-by-step beginner tutorial for building and running your first Docker container.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["docker", "containers"]
    },
    {
        "title": "Dockerizing a Node.js Application",
        "url": "https://nodejs.org/en/docs/guides/nodejs-docker-webapp",
        "description": "Official guide on how to containerize a Node.js web application using Docker.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["docker", "containers", "nodejs"]
    },
    {
        "title": "Docker Compose Overview",
        "url": "https://docs.docker.com/compose/",
        "description": "Learn how to define and run multi-container Docker applications using Docker Compose.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["docker", "containers", "compose"]
    },
    {
        "title": "Docker Tutorial for Beginners [FULL COURSE in 3 Hours]",
        "url": "https://www.youtube.com/watch?v=3c-iBn73dDE&t=663s",
        "description": "Full Docker Tutorial | Complete Docker Course | Hands-on course with a lot of demos and explaining the concepts behind, so that you really understand it.",
        "source": "TechWorld with Nana",
        "type": "tutorial-videos",
        "tags": ["docker", "containers", "compose"]
    },
        {
        "title": "Docker in 100 Seconds",
        "url": "https://www.youtube.com/watch?v=Gjnup-PuquQ",
        "description": " Docker is a required skill for almost every developer in today's world. Learn the basics of Dockerfiles, images, and containers in 100 seconds.",
        "source": "Fireship",
        "type": "tutorial-videos",
        "tags": ["docker", "containers", "compose"]
    },   

    # Kubernetes
    {
        "title": "Kubernetes Official Documentation",
        "url": "https://kubernetes.io/docs",
        "description": "Official Kubernetes docs covering pods, deployments, services, and more.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["kubernetes", "containers", "orchestration"]
    },
    {
        "title": "Kubernetes Basics Interactive Tutorial",
        "url": "https://kubernetes.io/docs/tutorials/kubernetes-basics/",
        "description": "Hands-on tutorial to deploy, scale, and update a containerised application on Kubernetes.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["kubernetes", "orchestration"]
    },
    {
        "title": "Kubernetes: Up and Running — O'Reilly",
        "url": "https://www.oreilly.com/library/view/kubernetes-up-and/9781492046523/",
        "description": "Comprehensive book covering Kubernetes architecture, deployments, and production best practices.",
        "source": "book",
        "type": "book",
        "tags": ["kubernetes", "orchestration", "containers"]
    },
    {
        "title": "Kubernetes the Hard Way",
        "url": "https://github.com/kelseyhightower/kubernetes-the-hard-way",
        "description": "Step-by-step guide to bootstrapping a Kubernetes cluster from scratch by Kelsey Hightower.",
        "source": "github",
        "type": "tutorial",
        "tags": ["kubernetes", "orchestration", "devops"]
    },
        {
        "title": "Kubernetes Explained in 6 Minutes | k8s Architecture",
        "url": "https://www.youtube.com/watch?v=TlHvYWVUZyc",
        "description": "Step-by-step guide to bootstrapping a Kubernetes cluster from scratch by Kelsey Hightower.",
        "source": "ByteByteGo | YouTube",
        "type": "tutorial-video",
        "tags": ["kubernetes", "orchestration", "devops"]
    },

    {
        "title": "The Co-Creator of Kubernetes On Convincing Google, Building It, and Scaling for LLMs",
        "url": "https://www.youtube.com/watch?v=FKijpCEH9D8",
        "description": "This is a conversation with Brendan Burns, co-creator of Kubernetes and current technical fellow / CVP at Microsoft working on Azure. We discussed what it was like building it at Google, how he got buy-in, and what he learned along the way.",
        "source": "Ryan Peterman | YouTube",
        "type": "tutorial",
        "tags": ["kubernetes", "orchestration", "devops"]
    },

    # Terraform
    {
        "title": "Terraform by HashiCorp Docs",
        "url": "https://developer.hashicorp.com/terraform/docs",
        "description": "Official Terraform documentation for infrastructure as code.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["terraform", "infrastructure", "iac"]
    },
    {
        "title": "Terraform Getting Started with AWS",
        "url": "https://developer.hashicorp.com/terraform/tutorials/aws-get-started",
        "description": "Official tutorial to provision AWS infrastructure using Terraform from scratch.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["terraform", "aws", "iac"]
    },
    {
        "title": "Terraform Best Practices",
        "url": "https://www.terraform-best-practices.com",
        "description": "Community-maintained guide covering Terraform structure, modules, and production best practices.",
        "source": "community",
        "type": "guide",
        "tags": ["terraform", "iac", "infrastructure"]
    },
    {
        "title": "Terraform Registry — Browse Providers & Modules",
        "url": "https://registry.terraform.io",
        "description": "Official Terraform registry to discover and use providers and reusable modules.",
        "source": "official-docs",
        "type": "reference",
        "tags": ["terraform", "iac", "modules"]
    },

    # Jenkins
    {
        "title": "Jenkins User Documentation",
        "url": "https://www.jenkins.io/doc/",
        "description": "Official Jenkins docs for CI/CD pipeline setup and configuration.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["jenkins", "cicd"]
    },
    {
        "title": "Jenkins Pipeline Tutorial",
        "url": "https://www.jenkins.io/doc/book/pipeline/",
        "description": "Official guide to creating declarative and scripted Jenkins pipelines.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["jenkins", "cicd", "pipeline"]
    },
    {
        "title": "Jenkins with Docker — CI/CD Pipeline",
        "url": "https://www.jenkins.io/doc/book/installing/docker/",
        "description": "Guide to running Jenkins inside Docker and building Docker images in your pipeline.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["jenkins", "cicd", "docker"]
    },
    {
        "title": "Jenkins Plugin Index",
        "url": "https://plugins.jenkins.io",
        "description": "Browse and discover Jenkins plugins for extending CI/CD pipeline capabilities.",
        "source": "official-docs",
        "type": "reference",
        "tags": ["jenkins", "cicd", "plugins"]
    },

    # Grafana
    {
        "title": "Grafana Documentation",
        "url": "https://grafana.com/docs/",
        "description": "Official Grafana docs for dashboards, alerting, and data sources.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["grafana", "monitoring"]
    },
    {
        "title": "Grafana Fundamentals Tutorial",
        "url": "https://grafana.com/tutorials/grafana-fundamentals/",
        "description": "Beginner tutorial covering Grafana dashboards, panels, and data source connections.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["grafana", "monitoring", "dashboards"]
    },
    {
        "title": "Grafana + Prometheus Monitoring Stack",
        "url": "https://grafana.com/docs/grafana/latest/getting-started/get-started-grafana-prometheus/",
        "description": "Official guide to connecting Prometheus as a data source in Grafana for metrics visualisation.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["grafana", "prometheus", "monitoring"]
    },
    {
        "title": "Grafana Dashboard Best Practices",
        "url": "https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/best-practices/",
        "description": "Best practices for building readable, performant, and maintainable Grafana dashboards.",
        "source": "official-docs",
        "type": "guide",
        "tags": ["grafana", "monitoring", "dashboards"]
    },

    # Prometheus
    {
        "title": "Prometheus Documentation",
        "url": "https://prometheus.io/docs/",
        "description": "Official Prometheus docs for metrics collection and alerting.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["prometheus", "monitoring"]
    },
    {
        "title": "Prometheus Getting Started",
        "url": "https://prometheus.io/docs/prometheus/latest/getting_started/",
        "description": "Official getting started guide to install Prometheus and scrape your first metrics.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["prometheus", "monitoring"]
    },
    {
        "title": "PromQL Query Language Guide",
        "url": "https://prometheus.io/docs/prometheus/latest/querying/basics/",
        "description": "Official reference for PromQL — the query language used to retrieve and analyse Prometheus metrics.",
        "source": "official-docs",
        "type": "reference",
        "tags": ["prometheus", "monitoring", "promql"]
    },
    {
        "title": "Prometheus Alerting Rules",
        "url": "https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/",
        "description": "Guide to defining alerting rules in Prometheus to trigger notifications based on metric thresholds.",
        "source": "official-docs",
        "type": "guide",
        "tags": ["prometheus", "monitoring", "alerting"]
    },
    
    # Ansible
    {
        "title": "Ansible Official Documentation",
        "url": "https://docs.ansible.com",
        "description": "Official Ansible documentation covering installation, playbooks, modules, and inventory management.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["ansible", "automation", "iac"]
    },
    {
        "title": "Ansible Getting Started Guide",
        "url": "https://docs.ansible.com/ansible/latest/getting_started/index.html",
        "description": "Official beginner guide to installing Ansible and running your first playbook.",
        "source": "official-docs",
        "type": "tutorial",
        "tags": ["ansible", "automation"]
    },
    {
        "title": "Ansible Playbooks Documentation",
        "url": "https://docs.ansible.com/ansible/latest/playbook_guide/index.html",
        "description": "Official guide to writing Ansible playbooks for automating configuration and deployments.",
        "source": "official-docs",
        "type": "documentation",
        "tags": ["ansible", "automation", "playbooks"]
    },
    {
        "title": "Ansible Galaxy — Browse Roles & Collections",
        "url": "https://galaxy.ansible.com",
        "description": "Official Ansible Galaxy hub to discover and share reusable Ansible roles and collections.",
        "source": "official-docs",
        "type": "reference",
        "tags": ["ansible", "automation", "roles"]
    },
    {
        "title": "Ansible Full Course for Beginners",
        "url": "https://www.youtube.com/watch?v=1id6ERvfozo",
        "description": "Complete Ansible tutorial covering installation, playbooks, roles, and real-world automation examples.",
        "source": "TechWorld with Nana | YouTube",
        "type": "tutorial-video",
        "tags": ["ansible", "automation", "devops"]
    },
    {
        "title": "Ansible in 100 Seconds",
        "url": "https://www.youtube.com/watch?v=xRMPKQweySE",
        "description": "Quick overview of Ansible — what it is, how it works, and why it's used for IT automation.",
        "source": "Fireship | YouTube",
        "type": "tutorial-video",
        "tags": ["ansible", "automation", "devops"]
    },
]

def seed():
    db = SessionLocal()
    for item in seed_data:
        existing = db.query(Resource).filter_by(url=item["url"]).first()
        if existing:
            for key, value in item.items():
                setattr(existing, key, value)
        else:
            db.add(Resource(**item))
    db.commit()
    db.close()
    print("Seeding complete.")

if __name__ == "__main__":
    seed()