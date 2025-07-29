import time

from selenium.common import NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

errors = [NoSuchElementException, ElementNotInteractableException, StaleElementReferenceException]
driver = webdriver.WebDriver()
wait = WebDriverWait(driver, 60, poll_frequency=.2, ignored_exceptions=errors)


# driver.get("https://www.ticketmaster.ca/blackpink-2025-world-tour-toronto-ontario-07-22-2025/event/10006252DC87273D")
driver.get("https://www.ticketmaster.ca/")

# Search for Blackpink event
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='searchFormInput-input']")))
driver.find_element(by=By.CSS_SELECTOR, value="input[id='searchFormInput-input']").send_keys("Blackpink")
driver.find_element(by=By.CSS_SELECTOR, value="input[id='searchFormInput-input']").submit()

driver.implicitly_wait(15)
# Check correct date time and event info before click on Find Tickets button
search_texts = ["BLACKPINK", "Toronto, ON", "Rogers Stadium", "2025-07-22", "Tue", "8:00 p.m."]
ul_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='eventList']")))
li_elements = ul_element.find_elements(by=By.TAG_NAME, value="li")
for li in li_elements:
    li_text = li.text  # Extract text content

    # Check if all search texts are present in the li element
    if all(text in li_text for text in search_texts):
        # print("Matching <li> found!")
        # print(li.get_attribute("outerHTML"))  # Print the matching <li> HTML
        find_tickets_button = li.find_element(by=By.TAG_NAME, value="a")
        driver.execute_script("arguments[0].scrollIntoView(true);", find_tickets_button)
        time.sleep(5)
        wait.until(EC.element_to_be_clickable(find_tickets_button)).click()
        # find_tickets_button.click()
        break

# Find "I Understand" button and click it
# Wait for the page to load
wait.until(lambda _ : driver.find_element(by=By.CSS_SELECTOR, value="button[data-bdd='accept-modal-accept-button']"))
i_agree_button = driver.find_element(by=By.CSS_SELECTOR, value="button[data-bdd='accept-modal-accept-button']")
i_agree_button.click()

select_drop_down = Select(wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[id='filter-bar-quantity']"))))
select_drop_down.select_by_value("4")

# Wait for the page to load
time.sleep(5)

scrollable_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-bdd='qp-split-scroll']")))

finish_scroll = False

def scroll_to_bottom():
    global finish_scroll
    last_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_element)

    while True:
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_element)
        time.sleep(2)  # Wait for content to load

        new_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_element)
        if new_height == last_height:
            finish_scroll = True
            break
        last_height = new_height

scroll_to_bottom()

menu_items = driver.find_element(by=By.CSS_SELECTOR, value="ul[data-bdd='quick-picks-list']")
# items  = menu_items.find_elements(by=By.TAG_NAME, value="li")
# for item in items:
#     print(item.text)

print('Finish scroll: {}'.format(finish_scroll))
wait.until(lambda _ : finish_scroll)
li_elements = menu_items.find_elements(by=By.XPATH, value="//li[contains(., 'Sec N113')]")
# driver.find_elements(by=By.XPATH, value="//li[contains(., 'Sec N113')]")
# row_113.find_element(by=By.TAG_NAME, value="button").click()
for li in li_elements:
    print(li.get_attribute("outerHTML"))
    li_description = li.find_element(by=By.CSS_SELECTOR, value="span[title='Section Description']")
    print(li_description.text)

row_num = input("Select the row number: ")
li_element = None

for i, element in enumerate(li_elements):
    if row_num in element.text:
        li_element = li_elements.pop(i)

print(li_element.text)
li_button_element = li_element.find_element(by=By.TAG_NAME, value="button")
li_button_element.click()

# After click on the price button, click to the next button
next_button = driver.find_element(by=By.CSS_SELECTOR, value="button[data-bdd='offer-card-buy-button']")
next_button.click()

# Wait for the login page to load
driver.implicitly_wait(15)
driver.find_element(by=By.CSS_SELECTOR, value="input[data-bdd='email-address-field']").send_keys("ticketmaster@allaninbox.com")
driver.find_element(by=By.CSS_SELECTOR, value="input[data-bdd='password-field']").send_keys("Dangkhoa20102000$$")
driver.find_element(by=By.CSS_SELECTOR, value="input[data-bdd='password-field']").submit()

# Enter CVV number
print('========Checking Credit Card Iframe is available========')
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@class='zoid-component-frame']")))
# iframe = driver.find_element(by=By.XPATH, value="//iframe[id='braintree-hosted-field-cvv' and name='braintree-hosted-field-cvv']")
print('========Switched to Credit Card Iframe========')
# payment_iframe = driver.find_element(by=By.XPATH, value="//iframe[@class='zoid-component-frame']")
# # payment_iframe = credit_card_div.find_element(by=By.TAG_NAME, value="iframe")
# print(payment_iframe)
# driver.switch_to.frame(payment_iframe)
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "//input[id='cvv']")))
# driver.find_element(by=By.CSS_SELECTOR, value="input[id='cvv']").send_keys("1234")
print('========Checking CVV Iframe is available========')
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id='braintree-hosted-field-cvv']")))
print('========Switched to CVV Iframe========')
driver.find_element(by=By.CSS_SELECTOR, value="input[id='cvv']").send_keys("2082")
print('========Switch back to parent content========')
driver.switch_to.default_content()

time.sleep(5)
checkout_section = driver.find_element(by=By.CSS_SELECTOR, value="div[data-tid='checkout-sections']")
div_checkout_section = checkout_section.find_elements(by=By.XPATH, value="./div")
print(len(div_checkout_section))
if len(div_checkout_section) > 2:
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='nofalseinput']"))).click()

checkbox_div = wait.until(EC.element_to_be_clickable((By.ID, "placeOrderOptIn1")))
checkbox_div.find_element(by=By.TAG_NAME, value="span").click()
# driver.find_element(by=By.XPATH, value=".//*[contains(text(), 'I have read and agree to the current')]").click()
# print('ol element: ', ol_element)

# Click Place Order Btn
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-tid='place-order-btn']"))).click()

close_window = input(str("Enter 'YES' when you want to close the window: "))
if close_window.lower() == 'yes':
    driver.quit()

