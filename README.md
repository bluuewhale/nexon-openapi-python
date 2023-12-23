# Nexon OpenAPI Python library

Nexon Python 라이브러리는 넥슨에서 제공하는 [OpenAPI](https://openapi.nexon.com/)에 대한 python 인터페이스를 제공합니다.

## Requirements
Python 3.7 버전 이상

## Install
```bash
pip install nexon_openapi
```

## Features
Nexon OpeanAPI Python 라이브러리에서 지원하는 기능들은 다음과 같습니다.

- 넥슨 OpenAPI에 대한 동기 및 비동기 클라이언트 지원
- 요청/응답에 대한 강력한 타입 힌트 지원
- 일시적인 오류에 대한 자동 재시도 (`408`, `409`, `429`, `500`)

## Supported APIs
현재까지 지원되는 API 목록은 다음과 같습니다.

- 바람의나라
- 바람의나라:연
- 메이플스토리
- 메이플스토리M
- 마비노기 영웅전
- 크레이지아케이드
- 히트2
- V4
- 카트라이더 러쉬플러스
- FC 온라인


## Usage
API 호출 예제는 [여기](https://github.com/BlueWhaleKo/nexon-openapi-python/tree/main/examples)에서 확인하실 수 있습니다.

```python
import os
from nexon_openapi import NexonOpenAPI

client = NexonOpenAPI(
    api_key=os.environ.get("NEXON_OPENAPI_API_KEY") # api_key 값이 주어지지 않은 경우, 기본적으로 환경 변수(`NEXON_OPEN_API_KEY`)를 파싱합니다.
)

ocid = client.maplestory.get_ocid(character_name="")
character_basic = client.maplestory.get_character_basic(ocid=ocid)

```

## Async usage
API 호출 예제는 [여기](https://github.com/BlueWhaleKo/nexon-openapi-python/tree/main/examples)에서 확인하실 수 있습니다.

```python
import asyncio
import os
from nexon_openapi import NexonOpenAPIAsync

client = NexonOpenAPIAsync(
    api_key=os.environ.get("NEXON_OPENAPI_API_KEY") # api_key 값이 주어지지 않은 경우, 기본적으로 환경 변수(`NEXON_OPEN_API_KEY`)를 파싱합니다.
)

async def main() -> None:
    ocid = await client.maplestory.get_ocid(character_name="")
    character_basic = await client.maplestory.get_character_basic(ocid=ocid)

asyncio.run(main())
```

## Examples
API 호출 예제는 [여기](https://github.com/BlueWhaleKo/nexon-openapi-python/tree/main/examples)에서 확인하실 수 있습니다.


## Retries
API 요청 중에 오류가 발생한 경우, 특저 오류는 2번의 재시도를 하도록 기본적으로 설정되어 있습니다. 네트워크 연결 오류, `408`(Request Timeout), `409`(Conflict), `429`(Rate Limit), 그리고 `>=500`(Internal Server Error)에 해당하는 오류들은 기본적으로 모두 재시도됩니다.

`max_retries` 옵션을 사용하여 재시도 설정을 구성하거나 비활성화할 수 있습니다:"

```python
from nexon_openapi import NexonOpenAPI
    client = NexonOpenAPI(max_retries=0)  # 기본 값은 2입니다.
```