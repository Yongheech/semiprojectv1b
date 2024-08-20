from sqlalchemy import insert

from app.model.member import Member


class MemberService:
    @staticmethod
    def insert_member(db, member):
        stmt = insert(Member).values(
            userid=member.userid, passwd=member.passwd,
            name=member.name,email=member.email )
        result = db.execute(stmt)
        db.commit()

        return result