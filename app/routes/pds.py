from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from app.dbfactory import get_db
# from app.service.pds import pdsService

pds_router = APIRouter()
templates = Jinja2Templates(directory='views/templates')

@pds_router.get('/write',response_class=HTMLResponse)
async def write(req: Request):
    return templates.TemplateResponse('/pds/write.html', {'request':req})

@pds_router.get('/view/{cpg}',response_class=HTMLResponse)
async def view(req: Request):
    return templates.TemplateResponse('/pds/view.html', {'request':req})

@pds_router.get('/list/{cpg}',response_class=HTMLResponse)
async def list(req: Request):
    return templates.TemplateResponse('/pds/list.html', {'request':req})