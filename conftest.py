import pytest
import niquests
from clients.post_client import PostClient
from clients.comments_client import CommentsClient


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def api_session():
    with niquests.Session() as session:
        session.headers.update({"Content-Type": "application/json"})
        yield session


@pytest.fixture
def post_api(api_session, base_url):
    return PostClient(session=api_session, base_url=base_url)


@pytest.fixture
def comments_api(api_session, base_url):
    return CommentsClient(session=api_session, base_url=base_url)
