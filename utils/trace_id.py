from urllib.request import Request

from fastapi import FastAPI

from core.conf import settings

def get_request_trace_id(request: Request)->str:
    return request.headers.get(settings.TRACE_ID_REQUEST_HEADER_KEY) or settings.LOG_CID_DEFAULT_VALUE