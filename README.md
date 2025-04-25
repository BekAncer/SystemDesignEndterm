## Overview

This middleware protects the API from traffic spikes and prevents overload by controlling the rate of incoming requests.

Implemented using **Token Bucket algorithm** for flexibility and better burst handling.

---

## How It Works

- Each client (identified by IP or API key) has a "bucket" of tokens.
    
- Each incoming request consumes 1 token.
    
- Tokens are refilled over time at a constant rate.
    
- If no tokens remain, the server responds with **HTTP 429 Too Many Requests**.
    

---

## Configuration

|Parameter|Description|Default|
|---|---|---|
|`rate`|Number of tokens added per second|5 tokens/sec|
|`capacity`|Maximum number of tokens in the bucket (burst size)|10 tokens|
|`token_expiry`|How long the tokens are stored (if using Redis)|1 hour|

Example settings:

```yaml
RATE_LIMIT_TOKENS_PER_SECOND: 5
RATE_LIMIT_BUCKET_CAPACITY: 10
RATE_LIMIT_REDIS_URL: redis://localhost:6379/0
```

---

## Why Token Bucket?

- Handles bursty traffic naturally.
    
- Allows smoothing spikes instead of immediate rejection.
    
- Simpler than Leaky Bucket for local service usage.
    

---

## HTTP Responses

|Code|Meaning|
|---|---|
|200 OK|Request processed normally|
|429 Too Many Requests|Client exceeded allowed request rate|
