from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

website = "https://www.adamchoi.co.uk/teamgoals/detailed"
path = ""
driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element("xpath", "//label[@analytics-event='All matches']")
all_matches_button.click()

dropdown = Select(driver.find_element(By.ID,'country'))
dropdown.select_by_visible_text('Spain')

time.sleep(3)
matches = driver.find_elements(By.TAG_NAME, "tr")

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element("xpath", "./td[1]").text)
    home_team.append(match.find_element("xpath", "./td[2]").text)
    score.append(match.find_element("xpath", "./td[3]").text)
    away_team.append(match.find_element("xpath", "./td[4]").text)

driver.quit()
df = pd.DataFrame({'date': date, 'home_team': home_team, 'score': score, 'away_team': away_team})
df.to_csv('football_data.csv', index = False)
print(df)