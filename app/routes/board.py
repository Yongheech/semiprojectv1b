from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.templating import Jinja2Templates

from app.dbfactory import get_db
from app.service.board import BoardService

board_router= APIRouter()
templates = Jinja2Templates(directory='views/templates')

# 페이징 알고리즘
# 페이지당 게시글 수 : 25
# 1page : 1 ~ 25
# 2page : 26 ~ 50
# 3page : 51 ~ 75
# ...
# npage : (n - 1) * 25 + 1 ~ (n - 1) * 25 + 25

@board_router.get('/list/{cpg}',response_class=HTMLResponse)
async def list(req: Request, cpg: int, db: Session =Depends(get_db)):
    try:
        bdlist = BoardService.select_board(db, cpg)

        return templates.TemplateResponse('/board/list.html',
                      {'request':req, 'bdlist':bdlist, 'cpg': cpg })

    except Exception as ex:
        print(f'▷▷▷ list 오류 발생 : {str(ex)}')
        return RedirectResponse(url='/member/error', status_code=303)

@board_router.get('/write',response_class=HTMLResponse)
async def write(req: Request):
    return templates.TemplateResponse('/board/write.html', {'request':req})

@board_router.get('/view',response_class=HTMLResponse)
async def view(req: Request):
    return templates.TemplateResponse('/board/view.html', {'request':req})
