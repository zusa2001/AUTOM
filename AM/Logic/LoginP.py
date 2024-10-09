from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
from Banner import print_welcome_banner
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# ------------------------- LOGIN FUNCTION -------------------------

def login_to_service(tenant_name, user_email, user_password, driver, website_url):
    # Element locators (IDs, names) used in the login and form processes
    tenant_input_name = 'tenant_input'  # Replace with actual tenant input name
    submit_button_name = 'submit_button'  # Replace with actual submit button name
    email_input_id = 'email_input'  # Replace with actual email input ID
    password_input_id = 'password_input'  # Replace with actual password input ID
    submit_button_id = 'final_submit_button'  # Replace with actual submit button ID
    checkbox_id = 'remember_me_checkbox'  # Replace with actual checkbox ID

    def click_with_retry(locator, max_attempts=3):
        """Retries clicking on an element if it becomes stale."""
        attempt = 0
        while attempt < max_attempts:
            try:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                break
            except StaleElementReferenceException:
                attempt += 1
                print(f"StaleElementReferenceException encountered. Retrying... {attempt}/{max_attempts}")
                if attempt == max_attempts:
                    raise

    try:
        # Open the login page
        driver.get(website_url)

        # Step 1: Input the tenant name
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, tenant_input_name))
        )
        input_field.clear()
        input_field.send_keys(tenant_name)

        # Step 2: Submit the tenant information
        click_with_retry((By.NAME, submit_button_name))

        # Step 3: Input the email for MFA (Multi-Factor Authentication)
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, email_input_id))
        )
        email_input.clear()
        email_input.send_keys(user_email)

        # Step 4: Submit the email
        click_with_retry((By.ID, submit_button_id))

        # Step 5: Input the password (wait for the password field to be ready)
        pw_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, password_input_id))
        )
        pw_input.clear()
        pw_input.send_keys(user_password)

        # Step 6: Submit the password
        click_with_retry((By.ID, submit_button_id))

        # Pause for the user to complete MFA via the Authenticator app (adjust as necessary)
        WebDriverWait(driver, 15).until(lambda driver: driver.execute_script("return document.readyState") == "complete")

        # Step 7: Check and click the "Don't show this again" checkbox if not already selected
        checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, checkbox_id))
        )
        if not checkbox.is_selected():
            checkbox.click()

        # Step 8: Submit the checkbox confirmation
        click_with_retry((By.ID, submit_button_id))

    finally:
        # Close the browser after completing the process
        time.sleep(10)
