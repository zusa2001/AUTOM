from selenium import webdriver
import logging
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from datetime import datetime
from Banner import print_welcome_banner
from Banner import print_schedule
from Banner import print_change
from selenium.webdriver.edge.options import Options
from Logic.LoginP import login_to_monet
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

# ---------------- Helper Function to Handle Stale Elements -----------------

def click_with_retry(driver, locator, max_attempts=3):
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

def get_elements_with_retry(driver, locator, max_attempts=3):
    """Retries fetching elements if a StaleElementReferenceException occurs."""
    attempt = 0
    while attempt < max_attempts:
        try:
            elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except StaleElementReferenceException:
            attempt += 1
            print(f"StaleElementReferenceException encountered. Retrying... {attempt}/{max_attempts}")
            if attempt == max_attempts:
                raise

# --------------------- Start of Main Logic --------------------------

# Print welcome banner (if needed)
print_welcome_banner()

# Initialize Edge options
logging.getLogger('selenium.webdriver.remote.remote_connection').setLevel(logging.ERROR)
edge_options = Options()
edge_options.add_argument('--disable-device-discovery-notifications')
edge_options.add_argument('--log-level=3')  # 3 = ERROR (Suppress INFO, WARNING, and ERROR logs from the browser)
edge_driver_path = 'AUTOM/AM/msedgedriver.exe'
website_url = 'YOUR_WEBSITE_URL'  # Replace with the target website URL
service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# User credentials for logging in
tenant_name = 'YOUR_TENANT_NAME'  # Replace with your tenant name
user_email = 'YOUR_EMAIL'  # Replace with your email
user_password = 'YOUR_PASSWORD'  # Replace with your password

# Call the login function
login_to_monet(tenant_name, user_email, user_password, driver, website_url)

# --------------------- STATUS CHANGE LOGIC --------------------------

# Define timeframes and corresponding statuses (based on schedule)
status_combo_box_id = 'statusListCombo'  # Combo box for status change
status_submit_button_id = 'submitmanualStatusChange'  # Submit button for status change

# Retry fetching the event time elements in case of Stale Element issues
event_time_elements = get_elements_with_retry(driver, (By.CLASS_NAME, 'eventTime'))

# Extract and print the time from each element
schedule_list = [0] * 14
for index, element in enumerate(event_time_elements):
    event_time = element.text.strip()  # Get the text and remove any surrounding whitespace
    if event_time != '':
        schedule_list[index] = event_time.replace(" - ", "-")

timeframes = {
    schedule_list[0]: "01. Available/Case Work",
    schedule_list[1]: "02. Break",
    schedule_list[2]: "01. Available/Case Work",
    schedule_list[3]: "03. Lunch",
    schedule_list[4]: "01. Available/Case Work",
    schedule_list[5]: "02. Break",
    schedule_list[6]: "01. Available/Case Work",
}

# Print the schedule
print_schedule()
for key, value in timeframes.items():
    print(f'{key}: {value}')

# ------------------ HELPER FUNCTIONS FOR STATUS UPDATE --------------------

# Function to get the current status based on the current time
def get_current_status(current_time):
    for timeframe, status in timeframes.items():
        start_time, end_time = [datetime.strptime(t, "%H:%M").time() for t in timeframe.split('-')]
        if start_time <= current_time <= end_time:
            return status
    return None  # Return None if no status matches the current time

# --------------------- MONITOR AND UPDATE STATUS --------------------------

# Loop continuously until the time reaches 4:30 PM (16:30)
CO = schedule_list[6]  # CO = Clock out
temp, clock_out = [datetime.strptime(t, "%H:%M").time() for t in CO.split('-')]
CO = clock_out.strftime("%H:%M")
print(f'Log Out: {clock_out}')

while datetime.now().time() <= datetime.strptime(CO, "%H:%M").time():
    # Get the current time
    current_time = datetime.now().time()

    # Locate the status combo box
    combobox = driver.find_element(By.ID, status_combo_box_id)
    select = Select(combobox)  # Create a Select object for interacting with the combo box

    # Get the currently selected status from the combo box
    currently_selected = select.first_selected_option.text.strip()

    # Determine the status that should be selected based on the current time
    status_to_select = get_current_status(current_time)

    currentStatusLbl = driver.find_element(By.ID, "adherenceCurrentStatus")
    currentStatusLblTxt = currentStatusLbl.text.strip()

    # If the current combo box selection differs from the required status, update it
    if status_to_select and status_to_select != currentStatusLblTxt:
        # Select the appropriate status in the combo box
        select.select_by_visible_text(status_to_select)

        # Submit the status change
        submit_button = driver.find_element(By.ID, status_submit_button_id)
        submit_button.click()
        print_change(currentStatusLblTxt,status_to_select)

    # Wait for 30 seconds before checking the time and status again
    time.sleep(10)

# Perform clock-out
time.sleep(10)
select.select_by_visible_text("Logged Out")

# Submit the status change
submit_button = driver.find_element(By.ID, status_submit_button_id)
submit_button.click()
time.sleep(10)
# End of the script
