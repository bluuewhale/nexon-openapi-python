from __future__ import annotations

import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import NexonOpenAPI, NexonOpenAPIAsync


class SyncAPIResource:
    _client: NexonOpenAPI

    def __init__(self, client: NexonOpenAPI) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete

    def _sleep(self, seconds: float) -> None:
        time.sleep(seconds)


class AsyncAPIResource:
    _client: NexonOpenAPIAsync

    def __init__(self, client: NexonOpenAPIAsync) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete

    def _sleep(self, seconds: float) -> None:
        time.sleep(seconds)
