from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import platform
import os

service = Service('/usr/local/bin/msedgedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.implicitly_wait(240)

# 登录学习通
driver.get('https://passport2.chaoxing.com/login?newversion=true')
driver.maximize_window()

print("登录后请输入要开始操作的首个视频链接：")
video_url = input()
driver.get(video_url)

while True:
    # 进入视频最外层页面
    video_info = driver.find_element(By.ID, "iframe")
    driver.switch_to.frame(video_info)
    # 进入视频内层并播放
    video = driver.find_elements(By.CLASS_NAME, "ans-attach-online.ans-insertvideo-online")
    num = 0
    for vid in video:
        # 拖动到可见的元素去
        driver.execute_script("arguments[0].scrollIntoView();", vid)

        driver.switch_to.frame(vid)
        video_play = driver.find_element(By.CLASS_NAME, "vjs-big-play-button")
        video_play.click()

        # 退回主页面层然后再次进入视频最外层页面
        # 检测任务是否完成、视频播放进度
        driver.switch_to.default_content()
        driver.switch_to.frame(video_info)
        while True:
            driver.switch_to.frame(vid)
            play = driver.find_element(By.CLASS_NAME, "vjs-play-control.vjs-control.vjs-button")
            if play.get_attribute("title") == "播放":
                play.click()
            driver.switch_to.default_content()
            driver.switch_to.frame(video_info)

            jobStatus = driver.find_elements(By.CLASS_NAME, "ans-job-icon")[num]
            jobStatus_style = jobStatus.value_of_css_property("background")

            if jobStatus_style == """rgba(0, 0, 0, 0) url("https://mooc1.chaoxing.com/ananas/css/job-status.png") no-repeat scroll 0px -24px / auto padding-box border-box""":
                break

        num += 1

    driver.switch_to.default_content()
    next = driver.find_element(By.CLASS_NAME, "jb_btn.jb_btn_92.fs14.prev_next.next")
    driver.execute_script('arguments[0].click()', next)