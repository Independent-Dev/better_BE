from _pytest import mark
import py
import pytest

# pytestmark = [pytest.mark.smoke, pytest.mark.reg]


@pytest.fixture(scope='module')  # scope를 주면 이 scope 내에서 한 번만 실행됨.
def my_setup():
    print("")
    print(">>>> MY SETUP <<<<")
    return {'id': 1}


@pytest.mark.smoke
def test_login_page_valid(my_setup):
    print("login with valid user")
    assert 1 == 2, "1 is not 2"


@pytest.mark.reg
def test_login_page_wrong(my_setup):
    # 이와 같이 매개변수로 넘기면 이를 위한 일종의 환경이 setup되고, setup의 return 값에 접근할 수 있음. 매개변수로 넘기지 않으면 함수로 취급함.
    print(my_setup['id'])
    print("login with wrong password")
