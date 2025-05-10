import pytest, allure

@allure.feature('Autorization')
@allure.story('Autorization with invalid user')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Autorization with invalid user')
def test_login_failure(login_page):
    with allure.step('Open login page'):
        login_page.navigate()
    with allure.step('Fill invalid user data'):
        login_page.login('user', 'password')
    with allure.step('Error Displayed - Invalid credentials. Please try again.'):
        assert login_page.get_error_msg() == 'Invalid credentials. Please try again.'

@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Autorization with valid user data')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])

def test_login_success(login_page, dashboard_page, username, password):
    with allure.step('Open login page'):
        login_page.navigate()
    with allure.step('Fill valid user data'):
        login_page.login(username, password)
    with allure.step("A welcome message with the user's name is displayed."):
        dashboard_page.assert_welcome_msg(f'Welcome {username}')