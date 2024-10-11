"""Definitions for creating and using the database connection."""

from sqlmodel import Session, SQLModel, create_engine, select

from .common import settings
from .models import Service  # pylint: disable=unused-import

engine = create_engine(str(settings.db_url), echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)


def list_services(session: Session):
    """Get a list of all services registered with the homepage service."""
    statement = select(Service)
    results = session.exec(statement)
    svcs = list(results.all())
    return svcs


init_db()
