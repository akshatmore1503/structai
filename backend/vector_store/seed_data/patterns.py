"""
25 real-world architecture patterns used to seed the FAISS vector store.
Each entry is embedded and used for RAG during architecture generation.
"""

ARCHITECTURE_PATTERNS = [
    {
        "name": "URL Shortener",
        "tags": ["web", "read-heavy", "caching", "hashing"],
        "text": """URL Shortener System Design:
A URL shortener takes a long URL and maps it to a short code. Key requirements: low latency reads, high availability, globally distributed.
Architecture: Client → CDN → API Gateway → Load Balancer → Stateless App Servers → Base62 ID Generator.
Database: PostgreSQL for URL mappings (shortCode → longURL). Redis cache for hot URLs (LRU eviction, 80% hit rate).
Write path: App server generates unique ID using Snowflake or counter, stores (shortCode, longURL, userId, createdAt) in Postgres, invalidates or warms cache.
Read path: Check Redis first. On miss, query Postgres, write to cache, return 302 redirect.
Scale: Handles ~100K writes/day, ~10M reads/day. Shard Postgres by shortCode prefix. Use separate read replicas.
Availability: Multi-region deployment, active-passive failover. CDN caches frequent redirects at edge.""",
    },
    {
        "name": "Social Media Feed (Twitter/Instagram-style)",
        "tags": ["social", "feed", "fan-out", "timeline", "write-heavy"],
        "text": """Social Media Feed System Design:
Timeline generation for users following many accounts. Two approaches: fan-out on write (push model) vs fan-out on read (pull model).
Architecture: Client → API Gateway → Feed Service → Timeline Cache (Redis sorted set, score = timestamp).
Fan-out on write: When a user posts, a Feed Fanout Worker pushes the post to followers' timeline caches. Fast reads, expensive writes for users with millions of followers (celebrities use pull model hybrid).
Post Storage: Cassandra (wide-column, optimized for time-series reads). Media stored in S3 + CDN.
Notification: Kafka for async event streaming to Notification Service.
Search: Elasticsearch for hashtag/user search.
Scale: 300M DAU, 500M tweets/day. Shard by user_id. Cache top 800 posts per user timeline in Redis.""",
    },
    {
        "name": "Ride-Sharing Platform (Uber/Lyft)",
        "tags": ["real-time", "geospatial", "matching", "payments"],
        "text": """Ride-Sharing System Design:
Real-time driver-rider matching with geospatial indexing, surge pricing, and trip tracking.
Services: Location Service (driver GPS updates every 5s via WebSocket), Matching Service (geospatial index via PostGIS or Redis GEO), Pricing Service, Trip Service, Payment Service, Notification Service.
Location: Redis GEO commands store driver coordinates. Query radius with GEORADIUS. Expires drivers who haven't pinged in 30s.
Matching: Matching Service queries nearby drivers, applies filters (car type, ratings), sends offer to closest available driver first.
Payments: Stripe integration, async via Kafka. Idempotency keys prevent double charges.
Database: PostgreSQL for trips and users. MongoDB for driver documents. Cassandra for location history.
Real-time: WebSockets for driver/rider app updates. Fallback to long polling.""",
    },
    {
        "name": "Video Streaming Platform (Netflix-style)",
        "tags": ["streaming", "cdn", "encoding", "recommendations"],
        "text": """Video Streaming System Design:
Large-scale video upload, transcoding, storage, and adaptive bitrate streaming.
Upload: Client → API Gateway → Upload Service → S3 (raw video). Multipart upload for large files.
Transcoding: Upload triggers Kafka event → Transcoding Workers (FFmpeg) produce multiple resolutions (240p, 480p, 720p, 1080p, 4K) and formats (HLS, DASH) → store in S3 (transcoded).
CDN: CloudFront or Akamai serves video chunks from edge nodes. Manifest files (.m3u8) guide adaptive bitrate selection.
Database: Cassandra for video metadata, user watch history (time-series). Elasticsearch for search.
Recommendations: Batch ML pipeline (Spark) generates personalized recommendations, stored in Redis for fast serving.
Auth: JWT tokens. Content DRM with Widevine/FairPlay.
Scale: 200M subscribers, 3PB new content/day. CDN absorbs 99% of traffic.""",
    },
    {
        "name": "E-Commerce Platform (Amazon-style)",
        "tags": ["e-commerce", "inventory", "payments", "search", "microservices"],
        "text": """E-Commerce Platform System Design:
Product catalog, inventory, cart, checkout, payments, and order fulfillment as microservices.
Services: Product Service (PostgreSQL + Elasticsearch for search), Inventory Service (Redis for real-time stock counts), Cart Service (Redis, session-based), Order Service (PostgreSQL with saga pattern), Payment Service (Stripe/PayPal), Notification Service (SES/SNS).
Product Search: Elasticsearch powers faceted search (category, price range, ratings). Sync from Postgres via CDC (Debezium + Kafka).
Inventory: Optimistic locking on stock decrement. Redis atomic DECR prevents overselling. Kafka for inventory events.
Checkout: Distributed saga: Reserve Inventory → Charge Payment → Confirm Order → Notify. Compensating transactions on failure.
Caching: Redis caches product pages (TTL 1h), flash sale prices (TTL 10s). CDN caches product images.
Database: PostgreSQL for orders/users. DynamoDB for cart. Elasticsearch for catalog.""",
    },
    {
        "name": "Chat Application (WhatsApp/Slack-style)",
        "tags": ["messaging", "websocket", "real-time", "presence"],
        "text": """Real-Time Chat System Design:
1:1 and group messaging with delivery receipts, presence, and offline message queuing.
Architecture: Client → WebSocket Gateway (sticky sessions via consistent hashing) → Message Service → Kafka → Fan-out Workers → Storage.
Connection: WebSocket connections maintained per user. Connection metadata (userId → serverId) stored in Redis. When server A needs to deliver to user on server B, it publishes to Kafka topic.
Messages: Cassandra stores messages (partition key: conversation_id, cluster key: timestamp). Efficient range queries for message history.
Presence: Heartbeat every 30s. Redis stores {userId: lastSeen}. Status broadcast via pub/sub.
Offline: Messages queued in Kafka. Delivered on reconnect via push notification (APNs/FCM) first.
Media: Upload to S3, share URL in message. CDN serves media.
Scale: 2B users, 100B messages/day. 10M concurrent connections across gateway fleet.""",
    },
    {
        "name": "Search Engine (Google-style)",
        "tags": ["search", "indexing", "crawling", "ranking"],
        "text": """Web Search Engine System Design:
Distributed web crawler, inverted index, and ranked result serving.
Crawling: URL Frontier (priority queue in Redis) → Crawler Workers (download HTML) → Content Parser → URL Extractor → Deduplication (Bloom filter) → Content Store (S3).
Indexing: Hadoop MapReduce / Spark processes raw HTML → tokenizes → builds inverted index (term → [docId, frequency, positions]) stored in distributed key-value store (BigTable/Cassandra).
Ranking: TF-IDF + PageRank + ML-based ranking (BERT embeddings for semantic similarity). Pre-computed scores updated daily.
Serving: Query → Query Parser → Index Lookup (multiple shards in parallel) → Result Merger → Ranker → Cache (Redis, top 10K queries cached) → Client.
Scale: 100M websites, 8.5B searches/day. Index partitioned by URL hash. Query served in <200ms p99.""",
    },
    {
        "name": "Image Hosting Service (Imgur/Pinterest-style)",
        "tags": ["image", "object-storage", "cdn", "resizing"],
        "text": """Image Hosting System Design:
Scalable image upload, processing, storage, and delivery.
Upload: Client → API Gateway → Image Upload Service → S3 (original). Presigned S3 URL for direct browser-to-S3 upload bypasses backend.
Processing: S3 event → Lambda/Worker → Image Processor generates thumbnails (100px, 400px, 800px), WebP conversion, EXIF strip → store variants in S3.
CDN: CloudFront distribution on top of S3. Cache-Control headers for long TTL (1 year, immutable). Images served at edge.
Database: PostgreSQL stores image metadata (imageId, userId, s3Key, variants, uploadedAt). Redis caches popular image metadata.
URL scheme: img.structai.com/{imageId}/{size}.webp → CDN → S3 fallback.
Deduplication: Perceptual hash (pHash) on upload to detect near-duplicates. SHA256 for exact duplicates.
Scale: 5M uploads/day, 500M views/day. CDN absorbs ~95% of read traffic.""",
    },
    {
        "name": "Distributed Key-Value Store (Redis/DynamoDB-style)",
        "tags": ["key-value", "distributed", "replication", "consistency"],
        "text": """Distributed Key-Value Store Design:
Highly available, partition-tolerant KV store with tunable consistency.
Partitioning: Consistent hashing ring. Each key maps to a virtual node (vnode). 3 replicas per key on next 3 physical nodes clockwise on ring. Adding/removing nodes moves only K/N keys on average.
Replication: Leader-based replication. Writes go to leader, replicated to followers. Reads from leader (strong) or any replica (eventual, lower latency).
Conflict Resolution: Vector clocks for detecting concurrent writes. Last-write-wins (LWW) with NTP timestamps as fallback.
Failure Detection: Gossip protocol. Each node randomly selects 3 peers to exchange heartbeats every second.
Compaction: LSM tree (Log-Structured Merge-tree) for write optimization. SSTables flushed from memtable. Background compaction merges SSTables.
API: GET /key, PUT /key value, DELETE /key. TTL support via expiry timestamp in value metadata.""",
    },
    {
        "name": "Payment Processing System",
        "tags": ["payments", "transactions", "idempotency", "compliance"],
        "text": """Payment Processing System Design:
Reliable, fraud-resistant payment processing with strong consistency and regulatory compliance.
Flow: Client → Payment API → Fraud Detection (ML model, sync, <100ms) → Payment Processor (Stripe/Braintree) → Order Service notification via Kafka.
Idempotency: Every payment request carries idempotency_key. Stored in Redis (TTL 24h). If same key arrives twice, return cached result without double-charging.
Database: PostgreSQL with ACID transactions for all financial records. Event sourcing: append-only ledger of all transactions. Never update, only append.
Saga Pattern: Distributed transaction across Payment, Inventory, Order services using choreography-based saga. Compensating transactions for rollback.
Security: PCI-DSS compliance. Card data never stored; use Stripe tokens. TLS everywhere. API keys rotated quarterly.
Reconciliation: Daily batch job reconciles internal ledger against Stripe/bank statements. Discrepancies trigger alerts.
Retry: Exponential backoff with jitter for idempotent operations. Non-idempotent (charge) never retried automatically.""",
    },
    {
        "name": "Notification System",
        "tags": ["notifications", "push", "email", "sms", "async"],
        "text": """Notification System Design:
Multi-channel notification delivery (push, email, SMS, in-app) with priority queuing and rate limiting.
Architecture: Event Producers → Kafka → Notification Router → Channel Workers (Push/Email/SMS) → Delivery Providers (FCM/APNs, SES, Twilio).
Routing: Notification Router reads user preferences (channel priority, quiet hours, opt-outs) from Redis cache. Routes to appropriate Kafka partition per channel.
Push: FCM for Android, APNs for iOS. Worker batches up to 500 tokens per request. Handles token refresh and invalid token cleanup.
Email: SES/SendGrid. Template engine (Handlebars/Mustache) renders HTML. Bounce/complaint webhooks update suppression list.
Rate Limiting: Token bucket per user per channel. Max 5 push/hour, 3 email/day, 2 SMS/day for non-critical. Real-time alerts bypass limits.
Retry: Dead-letter queue (DLQ) for failed deliveries. 3 retries with exponential backoff. Manual review queue for persistent failures.""",
    },
    {
        "name": "API Rate Limiter",
        "tags": ["rate-limiting", "throttling", "redis", "api-gateway"],
        "text": """API Rate Limiter Design:
Distributed rate limiting at API Gateway level with multiple algorithms.
Algorithms: Token Bucket (bursty traffic allowed, refill at fixed rate), Sliding Window Counter (more accurate than fixed window, uses Redis sorted set with timestamp scores), Fixed Window Counter (simple, Redis INCR + EXPIRE).
Implementation: Redis-based. For sliding window: ZADD requests {timestamp} {requestId}, ZREMRANGEBYSCORE (remove old), ZCARD (count). All in Lua script for atomicity.
Multi-tier: Global limit (IP), User limit (API key), Endpoint limit (per route). Checked in order, first exceeded limit wins.
Headers: X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset, Retry-After.
Distributed: Redis Cluster ensures all gateway nodes share rate limit state. Lua scripts execute atomically on single shard.
Bypass: Whitelist for internal services. Admin override keys. Graceful degradation if Redis is down (fail open with logging).""",
    },
    {
        "name": "File Storage System (Dropbox/Google Drive-style)",
        "tags": ["file-storage", "sync", "versioning", "conflict-resolution"],
        "text": """File Storage System Design:
Cloud file sync with versioning, conflict resolution, and multi-device synchronization.
Upload: Client chunks large files (4MB chunks). Upload chunks in parallel to Upload Service → S3. Deduplication via SHA256 hash of chunk (store once, reference many times). Metadata stored in PostgreSQL (fileId, userId, path, chunks[], version, modifiedAt).
Sync: Long-polling or WebSocket connection to Sync Service. On file change, server sends delta (added/modified/deleted files since last_sync_token). Client applies delta and updates local DB.
Conflict Resolution: Last-write-wins for simple conflicts. Fork with "(1)" suffix when same file modified offline on two devices. User resolves manually.
Versioning: Keep last 30 versions per file. Version stored as S3 object (deduplicated chunks). Version metadata in Postgres.
Sharing: Shared folder stored under one owner. Collaborators have read/write permissions stored in ACL table. Real-time sync to all collaborators on change.
Scale: 500M users, 100B files. S3 for storage. Postgres partitioned by userId.""",
    },
    {
        "name": "Real-Time Collaborative Document Editor (Google Docs-style)",
        "tags": ["collaboration", "crdt", "operational-transform", "real-time"],
        "text": """Collaborative Document Editor Design:
Multiple users editing same document simultaneously with conflict-free merging.
Algorithm: Operational Transformation (OT) or CRDT (Conflict-free Replicated Data Types, e.g., Y.js / Automerge). CRDTs are preferred for offline-first support.
Architecture: Client → WebSocket Server (per-document room) → OT/CRDT merge engine → Kafka (persist ops) → Storage.
Real-time: Each keystroke produces an operation (insert char at position, delete range). Operations sent to server, transformed against concurrent ops, broadcast to all collaborators in room.
Persistence: Operations stored in Cassandra (append-only log). Periodic snapshot of full document state in S3. Recovery: load latest snapshot + replay ops.
Presence: Cursor positions and user avatars shown in real-time via WebSocket broadcast.
Permissions: Owner, Editor, Commenter, Viewer roles. Enforced at WebSocket server before broadcasting ops.
Offline: CRDT allows offline edits; merge on reconnect without data loss.""",
    },
    {
        "name": "Recommendation Engine",
        "tags": ["ml", "recommendations", "collaborative-filtering", "embeddings"],
        "text": """Recommendation Engine Design:
Personalized content recommendations using collaborative filtering and ML embeddings.
Data Pipeline: User events (clicks, views, purchases, dwell time) → Kafka → Stream Processor (Flink/Spark Streaming) → Feature Store (Redis for real-time, S3 for batch).
Model Training: Batch job (Spark) trains Matrix Factorization (ALS) model weekly. Produces user_embedding and item_embedding vectors stored in Feature Store.
Serving: Real-time: user_embedding (Redis) × candidate item embeddings → cosine similarity → top-K filtered by business rules → returned in <50ms.
Candidate Generation: ANN (Approximate Nearest Neighbor) index (FAISS/ScaNN) over item embeddings. Fast retrieval of top-500 candidates. Reranker model applies real-time context (time of day, device, recency).
Cold Start: New users get popularity-based recs. New items get content-based recs (text/image embeddings). Switched to collaborative filtering after 10 interactions.
A/B Testing: Experiment framework randomly assigns users to models. Metrics: CTR, conversion, dwell time.""",
    },
    {
        "name": "Distributed Message Queue (Kafka-style)",
        "tags": ["message-queue", "pub-sub", "partitioning", "exactly-once"],
        "text": """Distributed Message Queue Design:
Durable, ordered, high-throughput pub-sub message broker.
Concepts: Topics partitioned across brokers. Each partition is an ordered, immutable log. Consumers track offset per partition.
Write: Producer → Leader broker (round-robin or key-based partition assignment). Leader appends to partition log. Followers replicate. ACK after min.insync.replicas replicate.
Read: Consumer group: each partition consumed by exactly one consumer in group. Offset committed after processing. Replay by resetting offset.
Durability: Messages persisted to disk (sequential writes, zero-copy reads). Configurable retention (time or size).
Exactly-once: Idempotent producer (sequence numbers per partition). Transactional API for atomic write across partitions.
Scale: 1M messages/sec per broker. Horizontal scaling by adding brokers and rebalancing partitions. Zookeeper (or KRaft) for leader election and metadata.""",
    },
    {
        "name": "Authentication Service (Auth0-style)",
        "tags": ["auth", "oauth", "jwt", "sso"],
        "text": """Authentication Service Design:
Centralized auth with OAuth 2.0, JWT tokens, and multi-factor authentication.
Flows: Authorization Code Flow (web apps), PKCE (SPAs, mobile), Client Credentials (M2M), Refresh Token rotation.
Token Storage: Access token (JWT, 15 min TTL) contains userId, roles, scopes. Signed with RS256 (private key on auth server, public key distributed for verification). Refresh token (opaque, 30 day TTL) stored in HttpOnly cookie.
Token Validation: Resource servers validate JWT signature locally using public key (no network call). Check exp, iss, aud claims.
MFA: TOTP (Google Authenticator, RFC 6238). Backup codes hashed with bcrypt. WebAuthn/FIDO2 for passwordless.
Session Management: Refresh token rotation. Old refresh token invalidated on use (sliding window). Revocation list in Redis for immediate logout.
Database: PostgreSQL for users, applications, refresh tokens. Redis for rate limiting, revocation list, MFA challenges.
Security: bcrypt for passwords, rate limit login attempts, account lockout, breached password check (HaveIBeenPwned API).""",
    },
    {
        "name": "IoT Data Pipeline",
        "tags": ["iot", "time-series", "streaming", "sensors"],
        "text": """IoT Data Pipeline Design:
Ingest, process, and store high-frequency sensor data from millions of devices.
Ingestion: IoT devices → MQTT Broker (EMQX/AWS IoT Core) → Kafka. MQTT is lightweight, ideal for constrained devices. Kafka buffers spikes and decouples producers from consumers.
Stream Processing: Flink processes Kafka stream: deduplication, schema validation, unit conversion, anomaly detection (sliding window, z-score). Enrichment with device metadata from Redis cache.
Storage: InfluxDB or TimescaleDB for time-series data (high write throughput, time-range queries). Cold data compressed to S3 after 90 days (Parquet format).
Real-time: Alerts (threshold breaches) → Notification Service (SNS/SES). Dashboard via WebSocket push.
Batch Analytics: Spark reads Parquet from S3. Trains predictive maintenance models. Results stored in PostgreSQL for BI tools.
Device Registry: PostgreSQL stores device metadata (deviceId, type, firmware, location). Redis caches active device status.
Scale: 10M devices, 100K events/sec. Kafka with 50 partitions. InfluxDB cluster with 3-way replication.""",
    },
    {
        "name": "Content Delivery Network (CDN)",
        "tags": ["cdn", "edge", "caching", "geolocation"],
        "text": """CDN Design:
Globally distributed edge caching network to serve static and dynamic content with low latency.
Architecture: Origin Server → Regional PoPs (Points of Presence) → Edge Nodes → Client.
Routing: Anycast DNS routes client to nearest edge node. BGP routing optimizes path. GeoDNS as fallback.
Caching: Edge nodes cache content by URL + Vary headers. TTL set by Cache-Control from origin. Surrogate keys for tag-based purging. Stale-while-revalidate for zero-downtime refreshes.
Cache Miss: Edge → Regional PoP (L2 cache) → Origin. L2 absorbs 40% of origin misses. Negative caching for 404s.
Dynamic Content: Request collapsing (coalesce concurrent cache misses into one origin request). Edge Side Includes (ESI) for partial page caching.
Purging: API-based purge by URL or tag. Propagates to all edges in <5 seconds via internal gossip.
Security: DDoS mitigation at edge (rate limiting, IP reputation, CAPTCHA challenge). TLS termination at edge, HTTP/2 and HTTP/3 (QUIC) support.""",
    },
    {
        "name": "Banking / Ledger System",
        "tags": ["banking", "ledger", "acid", "double-entry"],
        "text": """Banking Ledger System Design:
Double-entry bookkeeping with strong consistency, auditability, and regulatory compliance.
Core Principle: Every transaction debits one account and credits another. Sum of all debits == sum of all credits always.
Database: PostgreSQL (ACID). accounts table (accountId, balance, currency, type). transactions table (append-only ledger: txId, fromAccount, toAccount, amount, timestamp, status, idempotencyKey).
Transfer Flow: Begin TX → Lock both accounts (consistent order to prevent deadlock) → Validate balance → INSERT transaction record → UPDATE balances → Commit. All atomic.
Idempotency: SHA256(fromAccount + toAccount + amount + clientRequestId) as idempotency key. Duplicate requests return same result without double-processing.
Event Sourcing: Account balance is derived by replaying transaction log. Balance stored as materialized view, updated synchronously within transaction.
Audit: Immutable transaction log. All records have created_at, never updated_at. Soft-delete only.
Compliance: AML checks via async Kafka event after commit. Suspicious activity alerts. 7-year data retention.""",
    },
    {
        "name": "Ad Serving System",
        "tags": ["ads", "real-time-bidding", "targeting", "low-latency"],
        "text": """Ad Serving System Design:
Real-time ad selection and serving with targeting, auctions, and <100ms latency budget.
RTB Flow: Publisher page load → Ad Request (userId, pageContext, adSlot) → Ad Server → runs auction in <100ms → returns winning ad.
Targeting: User profile (interests, demographics, location) stored in Redis (pre-computed, updated daily by batch ML job). Ad targeting criteria matched against user profile using bitmap indexes for fast intersection.
Auction: Second-price auction (winner pays second-highest bid + $0.01). Bids from DSPs collected in parallel with 80ms timeout. Vickrey auction logic in-memory.
Serving: Winning ad creative served from CDN. Click/impression tracking pixel fires to analytics.
Budget: Campaign budget tracked in Redis with atomic DECR. Budget exhausted → ad paused within seconds.
Frequency Capping: Redis bitmap per (userId, adId) with daily TTL. GETBIT/SETBIT atomic operations. Max 3 impressions/day/user per ad.
Scale: 10M ad requests/sec. Redis cluster (64 shards). Serving latency p99 <80ms.""",
    },
    {
        "name": "Location Tracking System",
        "tags": ["geospatial", "real-time", "tracking", "redis-geo"],
        "text": """Location Tracking System Design:
Real-time tracking of moving entities (vehicles, deliveries, field agents) with geofencing.
Ingestion: Mobile/device → Location API → Kafka. GPS pings every 5–10 seconds. Kafka partitioned by entityId for ordering.
Storage: Redis GEO for real-time positions (GEOADD fleet:{regionId} lng lat entityId, TTL 60s to auto-expire offline devices). Cassandra for historical tracks (partitioned by entityId + date, clustered by timestamp).
Geofencing: Geofence definitions (polygon/circle) stored in PostGIS. On location update, check GEORADIUS in Redis, then precise polygon check in PostGIS for candidates. Trigger event on enter/exit.
Query: Nearby entities: Redis GEORADIUS entityId lat lng radius km. Historical route: Cassandra range query on (entityId, date, start_time, end_time).
Real-time dashboard: WebSocket server subscribes to Kafka, pushes updates to connected dashboards. Each dashboard filtered by region.
Scale: 1M tracked entities, 100K location updates/sec. Redis cluster by region. Cassandra for hot history (7 days), S3+Parquet for cold (older).""",
    },
    {
        "name": "Code Deployment Pipeline (CI/CD)",
        "tags": ["cicd", "containers", "kubernetes", "blue-green"],
        "text": """CI/CD Pipeline System Design:
Automated build, test, and deployment pipeline with zero-downtime deployments.
Pipeline Stages: Code Push → Webhook → CI Server (GitHub Actions/Jenkins) → Build (Docker image) → Test (unit, integration, e2e) → Security Scan (Trivy, SAST) → Push to Registry (ECR/GCR) → Deploy.
Deployment Strategies: Blue-Green: maintain two identical production environments, switch traffic at load balancer. Zero-downtime, instant rollback. Canary: route 5% traffic to new version, monitor error rate, auto-promote or rollback.
Kubernetes: Pods managed by Deployments. Rolling update strategy with maxSurge=1, maxUnavailable=0. Health checks: liveness probe (restart if unhealthy), readiness probe (stop traffic if not ready).
Artifact Storage: Docker images in ECR with immutable tags (commit SHA). Helm charts in Git (GitOps). Infrastructure as Code in Terraform.
Rollback: kubectl rollout undo deployment/app. Automated rollback if error rate >1% post-deploy (via Prometheus alert → rollback webhook).
Secrets: HashiCorp Vault or AWS Secrets Manager. Injected as env vars or volume mounts at runtime, never baked into images.""",
    },
    {
        "name": "Data Warehouse / Analytics Platform",
        "tags": ["data-warehouse", "etl", "olap", "bi"],
        "text": """Data Warehouse System Design:
Centralized analytical data store with ETL pipelines and BI query serving.
Architecture: Source Systems (OLTP DBs, SaaS APIs, event streams) → ETL/ELT Pipeline → Data Lake (S3, raw zone) → Transform (dbt/Spark) → Data Warehouse (Snowflake/BigQuery/Redshift) → BI Tools (Tableau/Metabase).
Ingestion: Batch: Airbyte/Fivetran for SaaS sources, Debezium CDC for OLTP databases. Streaming: Kafka → Kafka Connect → S3 (Parquet).
Data Lake: Raw zone (unchanged source data), Staging zone (cleaned/typed), Curated zone (business-ready tables). Catalogued in AWS Glue / Apache Iceberg.
Transformation: dbt models define SQL transformations as version-controlled code. Run on schedule (daily) or triggered by new data. Incremental models for large tables.
Data Model: Star schema (fact tables + dimension tables). Pre-aggregated summary tables for dashboard performance.
Governance: Column-level lineage tracking. PII masking in staging zone. Row-level security in warehouse.
Scale: 100TB data warehouse. Columnar storage + vectorized execution. Query cache for repeated dashboard queries.""",
    },
    {
        "name": "Online Gaming / Matchmaking System",
        "tags": ["gaming", "matchmaking", "leaderboard", "real-time"],
        "text": """Online Gaming System Design:
Real-time multiplayer matchmaking, game state sync, and leaderboards.
Matchmaking: Player → Matchmaking Service (skill-based: Elo/MMR range, expand range every 30s timeout) → Game Server allocation via Game Server Manager (Agones/custom) → Session created.
Game State: Authoritative game server. Clients send inputs, server applies game logic, broadcasts state. UDP for low-latency (with custom reliability layer for critical events).
Session: Game session metadata in Redis (sessionId, players, server IP, state). TTL auto-cleans stale sessions.
Persistence: Player stats in PostgreSQL (wins, losses, MMR, achievements). Game replays in S3 (compressed event log).
Leaderboard: Redis Sorted Set (ZADD leaderboard score playerId). O(log N) updates, O(log N) rank queries. Daily/weekly sets with scheduled key rotation.
Anti-Cheat: Server-side validation of all game actions. Statistical anomaly detection (speed hacks, aim bots). Rate limiting on action frequency.
Scale: 10M concurrent players. Regional game servers for <50ms RTT. Matchmaking pods autoscaled by queue depth.""",
    },
]
