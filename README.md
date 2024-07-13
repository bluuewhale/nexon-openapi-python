# Nexon Open API Python library
The Nexon Open API Python library provides a Python interface to the [Nexon Open API](https://openapi.nexon.com/).

## Requirements
3.7 or higher

## Install
```bash
pip install nexon_openapi
```

## Features
The Nexon OpenAPI Python library supports the following features:

- Synchronous and asynchronous client support for Nexon OpenAPI
- Strong type hinting for requests/responses
- Automatic retries for temporary errors (408, 409, 429, 500)

## Supported APIs
The currently supported APIs are:
- The First Descendant (퍼스트 디센던트)
- MapleStory (메이플스토리)
- The Kingdom of the Winds (바람의나라)
- The Kingdom of the Winds: Yeon (바람의나라:연)
- MapleStoryM (메이플스토리M)
- Vindictus (마비노기 영웅전)
- Crazy Arcade (크레이지아케이드)
- HIT2 (히트2)
- V4
- KartRider Rush+ (카트라이더 러쉬플러스)
- FC Online (FC 온라인)

## Usage
You can find more examples of API calls [here](https://github.com/BlueWhaleKo/nexon-openapi-python/tree/main/examples).

### Sync
```python
import os
from nexon_openapi import NexonOpenAPI

client = NexonOpenAPI(
    # If the api_key is not provided, it defaults to parsing the environment variable (`NEXON_OPEN_API_KEY`).
    api_key=os.environ.get("NEXON_OPENAPI_API_KEY") 
)

ocid = client.maplestory.get_ocid(character_name="")
character_basic = client.maplestory.get_character_basic(ocid=ocid)
print(character_basic)

```

### Async 
```python
import asyncio
import os
from nexon_openapi import NexonOpenAPIAsync

client = NexonOpenAPIAsync(
    # If the api_key is not provided, it defaults to parsing the environment variable (`NEXON_OPEN_API_KEY`).
    api_key=os.environ.get("NEXON_OPENAPI_API_KEY") 
)

async def main() -> None:
    ocid = await client.maplestory.get_ocid(character_name="")
    character_basic = await client.maplestory.get_character_basic(ocid=ocid)
    print(character_basic)

asyncio.run(main())
```

## Examples
You can find examples of API calls [here](https://github.com/BlueWhaleKo/nexon-openapi-python/tree/main/examples).


## Retries
When an error occurs during an API request, certain errors are automatically retried up to 2 times by default. 
Errors related to network connectivity, `408` (Request Timeout), `409` (Conflict), `429` (Rate Limit), and >=`500` (Internal Server Error) are all retried by default.

You can configure or disable retry settings using the `max_retries` option:

```python
from nexon_openapi import NexonOpenAPI
    client = NexonOpenAPI(max_retries=0)  # the default value is 2.
```