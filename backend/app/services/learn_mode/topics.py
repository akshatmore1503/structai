"""Static topic catalog for Learn Mode."""

TOPICS = [
    {
        "id": "load-balancing",
        "title": "Load Balancing",
        "description": "How traffic is distributed across servers to ensure availability and performance.",
        "icon": "⚖️",
        "difficulty": "beginner",
        "estimated_minutes": 10,
    },
    {
        "id": "caching",
        "title": "Caching Strategies",
        "description": "In-memory caching, eviction policies, cache-aside, write-through, and CDNs.",
        "icon": "⚡",
        "difficulty": "beginner",
        "estimated_minutes": 12,
    },
    {
        "id": "databases-sql-vs-nosql",
        "title": "SQL vs NoSQL",
        "description": "When to pick relational databases versus document, key-value, or column stores.",
        "icon": "🗄️",
        "difficulty": "beginner",
        "estimated_minutes": 15,
    },
    {
        "id": "message-queues",
        "title": "Message Queues & Event Streaming",
        "description": "Kafka, RabbitMQ, decoupling services, exactly-once delivery, and backpressure.",
        "icon": "📨",
        "difficulty": "intermediate",
        "estimated_minutes": 15,
    },
    {
        "id": "cap-theorem",
        "title": "CAP Theorem",
        "description": "Consistency, Availability, and Partition tolerance — picking two in distributed systems.",
        "icon": "📐",
        "difficulty": "intermediate",
        "estimated_minutes": 10,
    },
    {
        "id": "api-design",
        "title": "API Design & Rate Limiting",
        "description": "REST vs GraphQL, versioning, pagination, throttling, and API gateways.",
        "icon": "🔌",
        "difficulty": "intermediate",
        "estimated_minutes": 12,
    },
    {
        "id": "database-sharding",
        "title": "Database Sharding & Replication",
        "description": "Horizontal partitioning, consistent hashing, read replicas, and leader election.",
        "icon": "🔀",
        "difficulty": "advanced",
        "estimated_minutes": 20,
    },
    {
        "id": "microservices",
        "title": "Microservices Architecture",
        "description": "Service decomposition, inter-service communication, service discovery, and failure handling.",
        "icon": "🧩",
        "difficulty": "advanced",
        "estimated_minutes": 20,
    },
    {
        "id": "cdn-object-storage",
        "title": "CDN & Object Storage",
        "description": "Edge delivery, S3-compatible storage, presigned URLs, and media pipelines.",
        "icon": "🌐",
        "difficulty": "beginner",
        "estimated_minutes": 10,
    },
    {
        "id": "distributed-consensus",
        "title": "Distributed Consensus",
        "description": "Raft, Paxos, leader election, and how distributed databases agree on state.",
        "icon": "🤝",
        "difficulty": "advanced",
        "estimated_minutes": 25,
    },
]


def get_topic(topic_id: str) -> dict | None:
    return next((t for t in TOPICS if t["id"] == topic_id), None)
