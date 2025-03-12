from sqlalchemy import create_engine, Column, Integer, Numeric, Date
from sqlalchemy.orm import declarative_base, sessionmaker
import pytest

DATABASE_URL = "postgresql://postgres:2024@localhost:5432/QA"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Sales(Base):
    __tablename__ = 'sales'
    sale_id = Column(Integer, primary_key=True)
    store_id = Column(Integer, nullable=False)
    customer_id = Column(Integer, nullable=False)
    dt = Column(Date, nullable=False)
    amt = Column(Numeric(10, 2), nullable=False)


@pytest.fixture
def session():
    db_session = Session()
    yield db_session
    db_session.close()


def test_add_sale(session):
    new_sale = Sales(
        sale_id=1000, store_id=10, customer_id=20,
        dt="2025-03-12", amt=100.00
    )
    session.add(new_sale)
    session.commit()

    sale = session.query(Sales).filter_by(sale_id=1000).first()
    assert sale is not None
    assert sale.amt == 100.00

    session.delete(sale)
    session.commit()


def test_update_sale(session):
    new_sale = Sales(
        sale_id=2000, store_id=11, customer_id=21,
        dt="2025-03-13", amt=200.00
    )
    session.add(new_sale)
    session.commit()

    sale = session.query(Sales).filter_by(sale_id=2000).first()
    sale.amt = 250.00
    session.commit()

    updated_sale = session.query(Sales).filter_by(sale_id=2000).first()
    assert updated_sale.amt == 250.00

    session.delete(updated_sale)
    session.commit()


def test_delete_sale(session):
    new_sale = Sales(
        sale_id=3000, store_id=12, customer_id=22,
        dt="2025-03-14", amt=300.00
    )
    session.add(new_sale)
    session.commit()

    session.delete(new_sale)
    session.commit()

    deleted_sale = session.query(Sales).filter_by(sale_id=3000).first()
    assert deleted_sale is None
