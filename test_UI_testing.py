import datetime, time
from playwright.sync_api import sync_playwright, expect

def test_full_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # 1. Go to TodoMVC.

        page.goto("https://todomvc.com/examples/react/dist/")

        time.sleep(1)

        # 2. Validate that you are in the correct URL.

        url = page.url
        print("URL:", url)
        print("Validate URL")
        assert url == 'https://todomvc.com/examples/react/dist/' , 'URL not matched'
        
        time.sleep(1)

        # 3. Add a TODO item with the text “TODO 1 - ” concatenated with the current date.

        text_to_write = 'TODO 1 - ' + str(datetime.date.today())
        page.fill('xpath=//*[@id="todo-input"]' , text_to_write)
        page.keyboard.press("Enter")

        time.sleep(1)

        # 4. Verify that the new to-do item appears in the list
        
        text_todo = page.locator('xpath=//*[@id="root"]/main/ul/li/div/label').text_content()
        assert text_todo == text_to_write, 'TODO text is not equal'

        time.sleep(1)


        # 5. Add a TODO item with the text “TODO 2 - ” concatenated with the next day (tomorrow).

        text2_to_write = 'TODO 2 - ' + str(datetime.date.today() + datetime.timedelta(days=1))
        page.fill('xpath=//*[@id="todo-input"]' , text2_to_write)
        page.keyboard.press("Enter")
        
        time.sleep(1)

    
        # 6. Mark the current date TODO item as completed

        checkbox_second_element = page.locator('xpath=//*[@id="root"]/main/ul/li[2]/div/input')
        checkbox_second_element.click()

        time.sleep(1)       

        # 7. Verify that the item is displayed as completed (e.g., struck-through text)
    
        todo_el_to_check = page.locator('xpath=//*[@id="root"]/main/ul/li[2]/div/label')
        expect(todo_el_to_check).to_have_css("text-decoration", "line-through solid rgb(148, 148, 148)")
      
        time.sleep(1)

        # 8. Delete the TODO 2 item

        second_element = page.locator('xpath=//*[@id="root"]/main/ul/li[2]/div/label').hover()

        delete_button = page.locator('xpath=//*[@id="root"]/main/ul/li[2]/div/button').click()

        time.sleep(1)

        # 9. Verify that the item is removed from the list

        number_of_elements = page.locator('xpath=//*[@id="root"]/footer/span').text_content()
        assert number_of_elements == '1 item left!', 'Wrong number of items'

        time.sleep(1)

        # 10. Add a test report summarizing the test results (preferably Allure)

