import requests
from sqlalchemy import insert, select, and_
from sqlalchemy.exc import SQLAlchemyError

from app.model.pds import PdsAttach


class PdsService:
    @staticmethod
    def selectone_file(db, pno):
        try:
            find_pno = PdsAttach.pno == pno
            stmt = select(PdsAttach.fname).where(find_pno)
            result = db.execute(stmt).scalars().first()

            return result
        except SQLAlchemyError as ex:
            print(f' ▶▶▶ selectone_member 오류 발생 : {str(ex)}')






