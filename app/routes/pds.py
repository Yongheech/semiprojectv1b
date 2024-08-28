import os.path

import aiofiles
from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse, StreamingResponse
from starlette.templating import Jinja2Templates

from app.dbfactory import get_db
from app.service.pds import PdsService

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

@pds_router.get('/pdsdown/{pno}',response_class=HTMLResponse)
async def pdsdown(pno: int, db: Session = Depends(get_db)):

    DOWNLOAD_PATH = 'c:/Java/pdsupload/'
    down_fname = PdsService.selectone_file(db,pno)
    file_path = os.path.join(DOWNLOAD_PATH, down_fname)

    # 파일 다운로드시 작은 조각(chunk)으로 나눠 클라이언트에게 전송
    # pip install aiofiles
    async def iterfile():
        async with aiofiles.open(file_path, 'rb') as f:
            while chunk := await f. read(64 * 1024): # 64k chunk
                yield chunk
    return StreamingResponse(iterfile(),media_type='application/octet-stream',
                             headers={'Content-Disposition': f'attachment; filename={down_fname}'})

@pds_router.get('/mp3play/{pno}',response_class=HTMLResponse)
async def mp3play(pno: int, db:Session = Depends(get_db)):

    MUSIC_PATH = 'c:/Java/pdsupload/'
    audio_fname = PdsService.selectone_file(db, pno)
    file_path = os.path.join(MUSIC_PATH, audio_fname)

    # 파일 다운로드시 작은 조각(chunk)으로 나눠 클라이언트에게 전송
    # pip install aiofiles
    async def iterfile():
        async with aiofiles.open(file_path, 'rb') as f:
            while chunk := await f. read(64 * 1024): # 64k chunk
                yield chunk

    return StreamingResponse(iterfile() ,media_type='audio/mp3')