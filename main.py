from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from app.routes.member import member_router

app = FastAPI()
templates = Jinja2Templates(directory="views/templates") # jinja2 설정
app.mount('/static', StaticFiles(directory='views/static'), name='static')

app.include_router(member_router, prefix='/member')

@app.get("/",response_class=HTMLResponse)
async def index(req:Request):
    return templates.TemplateResponse('index.html',{'request':req})


if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app',reload=True)
