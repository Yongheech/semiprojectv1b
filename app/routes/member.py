from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from app.dbfactory import get_db
from app.schema.member import NewMember
from app.service.member import MemberService

member_router = APIRouter()
templates = Jinja2Templates(directory='views/templates')


@member_router.get('/join',response_class=HTMLResponse)
async def join(req: Request):
    return templates.TemplateResponse('/member/join.html', {'request':req})

@member_router.post('/join',response_class=HTMLResponse)
async def joinok(member: NewMember, db: Session = Depends(get_db)):
    print(member)
    result = MemberService.insert_member(db, member)
    print('처리결과:', result.rowcount)
@member_router.get('/login',response_class=HTMLResponse)
async def login(req: Request):
    return templates.TemplateResponse('/member/login.html', {'request':req})

@member_router.get('/myinfo',response_class=HTMLResponse)
async def myinfo(req: Request):
    return templates.TemplateResponse('/member/myinfo.html', {'request':req})