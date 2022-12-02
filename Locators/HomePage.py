from selenium.webdriver.common.by import By

class HomePage_locators:
    """ Route https://dev.foothunters.com/player/lewowi, login with admin account"""
    profile_icon = (By.CSS_SELECTOR, ".q-avatar.text-white.q-chip--colored")  # navbar avabar icon 
    logout_btn = (By.XPATH, "//div[normalize-space()='Logout']") # logout btn 

    like_btn = (By.XPATH, "//i[@role='img'][normalize-space()='thumb_up_off_alt']") # profile like button
    follow_btn = (By.XPATH, "//i[normalize-space()='person_add_alt_1']") # profile follow btn

    moderation_btn = (By.XPATH, "//i[normalize-space()='dashboard']") # navbar moderation btn
    moderation_page = (By.XPATH, "//i[normalize-space()='chrome_reader_mode']") # moderation btn
    approve_btn = (By.CSS_SELECTOR, ".q-btn__content.text-center") # change approve btn
    approve_popup = (By.CSS_SELECTOR, ".q-card__section.q-card__section--vert") # approve confirm btn
    moderatioin_done = (By.CSS_SELECTOR, ".q-btn__content.text-center") 

    # profile file uploading, login with player account

    video_upload_btn = (By.XPATH, "(//span[contains(text(),'Upload')])[2]") # profile video uploading btn
    browse_videos_btn = (By.XPATH,"//span[contains(text(),'Browse')]") # browse videos btn from popup
    title_input = (By.XPATH, "//input[@aria-label='Title']") # title input in popup
    description_input = (By.XPATH, "//textarea[@aria-label='Description']") # description input in popup
    publish_btn = (By.XPATH, "(//span[contains(text(),'Publish')])[1]") # publish btn input in profile

    precense_of_home_page_el = (By.CSS_SELECTOR, '.swiper-slide') # slider parent element in home page
    precense_of_uploaded_video = (By.XPATH, "//span[contains(text(),'Your video has been uploaded')]") # text on the video 
    precense_of_video = (By.XPATH, "//span[@title='file_example']") # uploaded video on the profile page.

    # Filter locators
    """ Route https://dev.foothunters.com/players, login with player's account"""
    search_input = (By.XPATH, "//input[@aria-label='Search for players']") # search input in players page

    filter_btn = (By.XPATH, "//span[normalize-space()='Filters']") # filter btn in players page
    filters_new = (By.XPATH, "//div[normalize-space()='New']") # New tab filter in players page
    filters_all = (By.XPATH, "//div[normalize-space()='All']") # All tab filter in players page
    players_found = (By.XPATH, "//span[@class='q-my-md text-h6 block full-width text-weight-regular']") # "Players Found" text
    players_count = (By.CSS_SELECTOR, ".q-btn.q-btn-item.non-selectable.no-outline.q-btn--standard.q-btn--rectangle.q-btn--rounded.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--gradient.gradient.q-py-none.q-px-xl.q-my-md") # Players count in "Found Player" page

    gender_selector = (By.XPATH, "(//div[@class='q-field__inner relative-position col self-stretch'])[4]") # gender filter btn
    gender_male = (By.XPATH,"//span[normalize-space()='Male']") # male gender filter btn
    gender_female = (By.XPATH,"//span[normalize-space()='Female']") # female gender filter btn
    apply_filers = (By.XPATH, "//span[normalize-space()='Apply Filters']") # apply filter btn

    # Moderation

    # moderation_elements = (By.CSS_SELECTOR,".q-item__section.column.q-item__section--main.justify-center")
    # moderation_view_buttons = (By.XPATH, "(//span[contains(text(),'View')])")

    # approve_btn = (By.XPATH, "//span[normalize-space()='Approve']")
    # reject_btn = (By.XPATH, "//span[normalize-space()='Reject']")
    # ok_btn = (By.XPATH, "//span[contains(text(),'OK')]")

    # Chat

    start_chat_button = (By.CSS_SELECTOR, "button[data-id='Start chat']")
    message_input = (By.CSS_SELECTOR, "textarea[data_id='message-input']") 
    send_button = (By.CSS_SELECTOR, "button[data_id='message-send']")
    message_btn = (By.CSS_SELECTOR, "button[data-id='message-button']")
    message_receiver = (By.CSS_SELECTOR, ".roomItem__name.text-body1")
    message_content = (By.CSS_SELECTOR, ".lastMessage__text.ellipsis")
    