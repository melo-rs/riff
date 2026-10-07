from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from riff.exceptions import RiffError


async def riff_exception_handler(_: Request, exc: RiffError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={"status_code": exc.status_code, "message": exc.message},
    )


def add_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(RiffError, riff_exception_handler)  # type: ignore
