from selenium.webdriver.common.by import By

class HomePage_locators:
    profile_icon = (By.CSS_SELECTOR, ".q-avatar.text-white.q-chip--colored")
    logout_btn = (By.XPATH, "//div[normalize-space()='Logout']")

    like_btn = (By.CSS_SELECTOR, "div[class='q-page-container'] button:nth-child(1)")
    follow_btn = (By.CSS_SELECTOR, "div[class='q-page-container'] button:nth-child(2)")

    moderation_btn = (By.XPATH, "//i[normalize-space()='dashboard']")
    moderation_page = (By.XPATH, "//i[normalize-space()='chrome_reader_mode']")
    approve_btn = (By.CSS_SELECTOR, ".q-btn__content.text-center")
    approve_popup = (By.CSS_SELECTOR, ".q-card__section.q-card__section--vert")
    moderatioin_done = (By.CSS_SELECTOR, ".q-btn__content.text-center")

    # profile file uploading

    video_upload_btn = (By.XPATH, "(//span[contains(text(),'Upload')])[2]")
    browse_videos_btn = (By.XPATH,"//span[contains(text(),'Browse')]")
    title_input = (By.XPATH, "//input[@aria-label='Title']")
    description_input = (By.XPATH, "//textarea[@aria-label='Description']")
    publish_btn = (By.XPATH, "(//span[contains(text(),'Publish')])[1]")

    precense_of_home_page_el = (By.CSS_SELECTOR, '.swiper-slide')
    precense_of_uploaded_video = (By.XPATH, "//span[contains(text(),'Your video has been uploaded')]")
    precense_of_video = (By.XPATH, "//span[@title='file_example']")

    # Filter locators

    search_input = (By.XPATH, "//input[@aria-label='Search for players']")

    filter_btn = (By.XPATH, "//span[normalize-space()='Filters']")
    filters_new = (By.XPATH, "//div[normalize-space()='New']")
    filters_all = (By.XPATH, "//div[normalize-space()='All']")
    players_found = (By.XPATH, "//span[@class='q-my-md text-h6 block full-width text-weight-regular']")
    players_count = (By.CSS_SELECTOR, ".q-btn.q-btn-item.non-selectable.no-outline.q-btn--standard.q-btn--rectangle.q-btn--rounded.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--gradient.gradient.q-py-none.q-px-xl.q-my-md")

    gender_selector = (By.XPATH, "(//div[@class='q-field__inner relative-position col self-stretch'])[4]")
    gender_male = (By.XPATH,"//span[normalize-space()='Male']")
    gender_female = (By.XPATH,"//span[normalize-space()='Female']")
    apply_filers = (By.XPATH, "//span[normalize-space()='Apply Filters']")

    # Moderation

    moderation_elements = (By.CSS_SELECTOR,".q-item__section.column.q-item__section--main.justify-center")
    moderation_view_buttons = (By.XPATH, "(//span[contains(text(),'View')])")

    approve_btn = (By.XPATH, "//span[normalize-space()='Approve']")
    reject_btn = (By.XPATH, "//span[normalize-space()='Reject']")
    ok_btn = (By.XPATH, "//span[contains(text(),'OK')]")

    # Chat

    start_chat_button = (By.XPATH, "//span[normalize-space()='Start chat']")
    message_input = (By.XPATH, "//textarea[@placeholder='Message']")
    send_button = (By.XPATH, "//i[normalize-space()='send']")
    message_btn = (By.XPATH, "//span[normalize-space()='Messages']")
    message_receiver = (By.CSS_SELECTOR, ".roomItem__name.text-body1")
    message_content = (By.CSS_SELECTOR, ".lastMessage__text.ellipsis")