from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from app.dbfactory import get_db
from app.service.board import BoardService

board_router= APIRouter()
templates = Jinja2Templates(directory='views/templates')

@board_router.get('/list',response_class=HTMLResponse)
async def list(req: Request, db: Session =Depends(get_db)):
    try:
        bdlist = BoardService.select_board(db)
        print(bdlist)
        return templates.TemplateResponse('/board/list.html', {'request':req})

    except Exception as ex:
        print(f'▷▷▷ list 오류 발생 : {str(ex)}')
        return RedirectResponse(url='/member/error', status_code=303)

@board_router.get('/write',response_class=HTMLResponse)
async def write(req: Request):
    return templates.TemplateResponse('/board/write.html', {'request':req})

@board_router.get('/view',response_class=HTMLResponse)
async def view(req: Request):
    return templates.TemplateResponse('/board/view.html', {'request':req})
