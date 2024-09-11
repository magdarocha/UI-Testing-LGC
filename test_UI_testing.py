import datetime, time
import pytest
from playwright.sync_api import sync_playwright, expect

text_to_write = 'TODO 1 - ' + str(datetime.date.today())
text2_to_write = 'TODO 2 - ' + str(datetime.date.today() + datetime.timedelta(days=1))

@pytest.fixture(scope='session')
def before_all():
    print("Begin Test Suite")

    print('Setup page')
    page = None

    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    p.stop()
    print("End Test Suite")

@pytest.fixture()
def before_each():
    yield
    time.sleep(1)

def test_001(before_all, before_each):
    # 1. Go to TodoMVC.
    page = before_all
    page.goto("https://todomvc.com/examples/react/dist/")

def test_002(before_all, before_each):
    page = before_all

    # 2. Validate that you are in the correct URL.
    url = page.url
    print("URL:", url)
    print("Validate URL")
    assert url == 'https://todomvc.com/examples/react/dist/' , 'URL not matched'

def test_003(before_all, before_each):
    page = before_all

    # 3. Add a TODO item with the text “TODO 1 - ” concatenated with the current date.

    # text_to_write = 'TODO 1 - ' + str(datetime.date.today())
    page.fill('xpath=//*[@id="todo-input"]' , text_to_write)
    page.keyboard.press("Enter")

    print("Created a ToDo element:", text_to_write)

def test_004(before_all, before_each):
    page = before_all

    # 4. Verify that the new to-do item appears in the list
    
    text_todo = page.locator('xpath=//*[@id="root"]/main/ul/li/div/label').text_content()
    assert text_todo == text_to_write, 'TODO text is not equal'

def test_005(before_all, before_each):
    page = before_all

    # 5. Add a TODO item with the text “TODO 2 - ” concatenated with the next day (tomorrow).

    # text2_to_write = 'TODO 2 - ' + str(datetime.date.today() + datetime.timedelta(days=1))
    page.fill('xpath=//*[@id="todo-input"]' , text2_to_write)
    page.keyboard.press("Enter")
    print("Created a ToDo2 element:", text2_to_write)

def test_006(before_all, before_each):
    page = before_all

    # 6. Mark the current date TODO item as completed

    checkbox_second_element = page.locator('xpath=//*[@id="root"]/main/ul/li[2]/div/input')
    checkbox_second_element.click()

def test_007(before_all, before_each):
    page = before_all

    # 7. Verify that the item is displayed as completed (e.g., struck-through text)

    todo_el_to_check = page.locator('xpath=//*[@id="root"]/main/ul/li[2]/div/label')
    expect(todo_el_to_check).to_have_css("text-decoration", "line-through solid rgb(148, 148, 148)")

def test_008(before_all, before_each):
    page = before_all

    # 8. Delete the TODO 2 item

    second_element = page.locator('xpath=//*[@id="root"]/main/ul/li[2]/div/label').hover()

    delete_button = page.locator('xpath=//*[@id="root"]/main/ul/li[2]/div/button').click()

def test_009(before_all, before_each):
    page = before_all

    # 9. Verify that the item is removed from the list

    to_do_list = page.locator('xpath=//*[@id="root"]/main/ul/li').all()
    count_to_do = len(to_do_list)
    print('Number of to do elements in the list is',count_to_do)
    assert count_to_do == 1, 'Wrong number of items'
