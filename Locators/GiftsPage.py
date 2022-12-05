from selenium.webdriver.common.by import By

# Gifts
class GiftsPage_locators:
    userCard_username = (By.XPATH, "//span[@class='userCard__username text-h5']")
    points_count = (By.XPATH, "//span[@class='points__count text-h4 q-ml-sm']")
    profile_icon = (By.XPATH, "//span[@class='q-mr-sm']")
    userCard_points = (By.XPATH, "//span[@class='userCard__points q-ml-xs']")

    gift_card = (By.CSS_SELECTOR, ".q-btn.q-btn-item.non-selectable.no-outline.q-btn--flat.q-btn--rectangle.q-btn--rounded.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.gift__get.flex-shrink.q-py-sm")

    gift_cap = (By.CSS_SELECTOR, ".gift-cap")
    