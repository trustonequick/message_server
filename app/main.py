import uvicorn
from fastapi import FastAPI

from app.common.config import conf
from app.routes import index, message, dozn, coocon


def create_app():
    c = conf()
    app = FastAPI(
        title="스매피 메시지 발송 통합 서버.",
        description="스매피 메시지 발송 통합 서버.",
        version="0.0.8",
        docs_url=c.DOCS_URL,
        redoc_url=None,
    )
    # 라우터 정의
    app.include_router(index.router)
    app.include_router(message.router)
    app.include_router(dozn.router)
    app.include_router(coocon.router)

    return app


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True)
else:
    app = create_app()
