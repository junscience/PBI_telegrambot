from login import driver
from PIL import Image
from selenium.webdriver.common.by import By
import time
from tqdm import tqdm

# wait some time
time.sleep(1)
for i in tqdm(range(7)):
    time.sleep(1)
# open dashboard in a full-screen mode
screen_opt = driver.find_element(By.XPATH, '//*[@id="exploration-container-app-bars"]/app-bar/div/div[2]/button[3]')
screen_opt.click()
full_screen = driver.find_element(By.XPATH, '//*[@id="mat-menu-panel-6"]/div/button[1]')
full_screen.click()
full_screen_2 = driver.find_element(By.XPATH, '//*[@id="fitToPageButton"]')
full_screen_2.click()

# save and crop first screenshot
driver.save_screenshot('ss1.png')
img = Image.open('ss1.png')
cropped_img1 = img.crop((0, 0, 1600, 1000))
cropped_img1.save('ss1.png')

# list and make screenshots of all dashboards
dic = {}
for i in range(2, 6):
    next_dash = driver.find_element(By.XPATH, '//*[@id="pvExplorationHost"]/div/div/exploration-fullscreen-navigation/div/i[2]')
    next_dash.click()
    time.sleep(2)
    driver.save_screenshot(f'ss{i}.png')
    img = Image.open(f'ss{i}.png')
    cropped_img = img.crop((0, 0, 1600, 1000))
    cropped_img.save(f'ss{i}.png')
