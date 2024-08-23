from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.model.board import Board


class BoardService:
    @staticmethod
    def select_board(db):
        try:
            stmt = select(Board.bno,Board.title,Board.userid,
                          Board.regdate,Board.views)\
                    .order_by(Board.bno.desc())
            result =db.execute(stmt)

            return result

        except SQLAlchemyError as ex:
            print(f'▶▶▶select_board 오류발생: {str(ex)}')