from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from page_base import BasePage
import time  

class ReviewsPage(BasePage):
  def get_text_main_header(self):
    return self.driver.find_element(By.XPATH, "/html/body/main/header/div/div/h1").text
  
  # Need to find a way to get image when it is hard coded as CSS style bacgkorund image. Same problem for the main image on the state pages
  def get_element_main_image(self):
    return self.driver.find_element(By.XPATH, "")
  
  # The section below contains a few different views that are dynamic:
  # 1. The default view
  # 2. The view when "Write a Review" is selected
  # 3. The view when the pencil icon is selected inside view 2
  # ***Note*** this section and the reviews below are allin an iframe. We need to switch the driver to this iframe whenever we try to find an element within it.
  def get_element_reviews_summary_section(self):
    self.driver.switch_to.frame("bfpublish") 
    return self.driver.find_element(By.CLASS_NAME, "reviewlistheader")

  ################# View 1 (default) Elements ######################
  # Get view 1 element, run tests on its children elements and on whether this is hidden or not depending on if the "Write a review" button was pressed. This is visible until that button is pressed.
  def get_element_reviews_summary_view_1(self):
    reviews_summary = self.get_element_reviews_summary_section()
    return reviews_summary.find_element(By.CLASS_NAME, "reviewlistheader-inner")

  def get_text_reviews_summary_view_1_header(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_element(By.TAG_NAME, 'h2').text
  
  def get_elements_reviews_summary_view_1_rating_value(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    elements = reviews_summary.find_elements(By.CLASS_NAME, "ratingval")
    numbers = [0, 0, 0, 0, 0]
    for i, element in enumerate(elements):
      numbers[i] = int(element.text)
    return numbers
  
  def get_elements_reviews_summary_view_1_stars(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_elements(By.CLASS_NAME, "starOn")
    # assert there are 5 stars
  
  def get_text_review_summary_view_1_rating(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_element(By.CLASS_NAME, "be-c-ratingval").text
    # assert is rational number?
  
  def get_elements_review_summary_view_1_rating_stars(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_elements(By.CLASS_NAME, "be-c-star")
    # assert there are 5 stars
  
  def get_text_review_summary_view_1_reviews_number(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    return reviews_summary.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div/div/div[2]/div/div[2]/div[2]").text
    # assert reviews in string
  
  def click_element_review_summary_view_1_write_review_button(self):
    reviews_summary = self.get_element_reviews_summary_view_1()
    reviews_summary.find_element(By.ID, "btnWriteAReview").click()
    

  def click_element_review_summary_view_1_contact_us_button(self):
    original_window = self.driver.current_window_handle
    reviews_summary = self.get_element_reviews_summary_view_1()
    reviews_summary.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/a[2]/div').click()
    self.new_tab(original_window)
    #clicking opens view 2
  
  ################## View 2 Elements #######################
  # Get view 2 element, run tests on its children elements and on whether this is hidden or not depending on if the "Write a review" button was pressed. This is hidden until that button is pressed.
  def get_element_review_summary_view_2(self):
    self.driver.switch_to.default_content() # from view to view 2 need to switch to default content. If we do not do this we are telling the driver for the iframe to switch to itself. But there is no iframe within the iframe so it breaks.
    reviews_summary = self.get_element_reviews_summary_section()
    return reviews_summary.find_element(By.CLASS_NAME, "review-opinion-options")
    # this becomes unhidden when write a review button is pressed, so we have to click that button in our tests that test elements in view 2

  def get_text_review_summary_view_2_header(self):
    view_2 = self.get_element_review_summary_view_2()
    return view_2.find_element(By.TAG_NAME, 'h2').text
  
  def get_text_review_summary_view_2_sub_header(self):
    view_2 = self.get_element_review_summary_view_2()
    return view_2.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[1]').text
  
  def click_element_review_summary_view_2_google_button(self):
    original_window = self.driver.current_window_handle
    view_2 = self.get_element_review_summary_view_2()
    view_2.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[2]/div/div[2]/a[1]').click()
    self.new_tab(original_window)
    # clicking button opens a new tab

  def click_element_review_summary_view_2_pencil_button(self):
    original_window = self.driver.current_window_handle
    view_2 = self.get_element_review_summary_view_2()
    view_2.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/div[2]/a[2]").click()
    self.new_tab(original_window)
    # switches to view 3

  # NO LONGER EXISTS
  ######################### View 3 Elements #############################
  # Get view 3 element, run tests on its children elements and on whether this is hidden or not depending on if the pencil button was pressed inside of view 2. This is hidden until thaose buttons are pressed.
  # def get_element_review_summary_view_3(self):
  #   self.driver.switch_to.default_content() # from view 2 to view 3 need to switch to default content. If we do not do this we are telling the driver for the iframe to switch to itself. But there is no iframe within the iframe so it breaks.
  #   reviews_summary = self.get_element_reviews_summary_section()
  #   return reviews_summary.find_element(By.ID, "reviewFormWrapper")
  #   # unhidden after the write a review button AND then the pencil button is clicked
  
  # def get_text_review_summary_view_3_header(self):
  #   view_3 = self.get_element_review_summary_view_3()
  #   return view_3.find_element(By.TAG_NAME, 'h2').text
  
  # def get_elements_review_summary_view_3_stars(self):
  #   view_3 = self.get_element_review_summary_view_3()
  #   span = view_3.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/form/div/div[1]/div[1]/span")
  #   stars = span.find_elements(By.TAG_NAME, 'span')
  #   return stars
  
  # def click_element_review_summary_view_3_star(self, star_number):
  #   stars = self.get_elements_review_summary_view_3_stars()
  #   stars[star_number].click()
  # # star is clicked, assert classList contains be-star-on

  # def get_input_review_summary_view_3_describe_experience(self):
  #   text_area = self.driver.find_element(By.ID, 'review__comments')
  #   text_area.send_keys('test_input')
  #   return text_area.get_attribute('value')

  # def get_text_review_summary_view_3_sub_text(self):
  #   view_3 = self.get_element_review_summary_view_3()
  #   return view_3.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/form/div/div[2]/div/div[1]/div[2]/div/span[1]').text
  
  # def get_text_review_summary_view_3_sub_sub_text(self):
  #   view_3 = self.get_element_review_summary_view_3()
  #   return view_3.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/form/div/div[2]/div/div[1]/div[2]/div/span[2]').text
  
  # # opens new tab
  # def click_element_review_summary_view_3_privacy_policy(self):
  #   original_window = self.driver.current_window_handle
  #   view_3 = self.get_element_review_summary_view_3()
  #   view_3.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/form/div/div[2]/div/div[1]/div[2]/div/span[3]/a[1]').click()
  #   self.new_tab(original_window)
  
  # # opens new tab
  # def click_element_review_summary_view_3_terms_of_service(self):
  #   original_window = self.driver.current_window_handle
  #   view_3 = self.get_element_review_summary_view_3()
  #   view_3.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/form/div/div[2]/div/div[1]/div[2]/div/span[3]/a[2]').click()
  #   self.new_tab(original_window)
  
  # def check_element_review_summary_view_3_button_is_clickable(self):
  #   element = self.driver.find_element(By.ID, 'btnSubmit')
  #   bool = False
  #   bool = WebDriverWait(self.driver, timeout=3).until(EC.element_to_be_clickable(element))
  #   return bool
  # #############################################################
  
  def get_elements_all_reviews(self):
    self.driver.switch_to.frame("bfpublish")
    all_reviews = self.driver.find_element(By.ID, 'allReviews')
    reviews = all_reviews.find_elements(By.CLASS_NAME, "reviewblock")
    self.driver.switch_to.default_content() # since this method is called twice in test_more_reviews_on_scroll we need to reset the driver back to the main page so that the second time we call this function we do not look for the iframe inside the iframe.
    return reviews
  
  # Cross origin policy makes scrolling inside of an iFrame that is in a web page a pain. Get the scrollable element in the iframe using WebDriver then scroll. This scrolls just the iFrame.
  def scroll_down(self):
    self.driver.switch_to.frame('bfpublish')
    scrollable_element = self.driver.find_element(By.XPATH, '/html/body')
    self.driver.execute_script("arguments[0].scrollBy(0, 5000)", scrollable_element)
    time.sleep(2)
    self.driver.switch_to.default_content()
  
  def get_element_aside(self):
    return self.driver.find_element(By.XPATH, '/html/body/main/aside')
  
  def get_text_aside_header(self):
    aside = self.get_element_aside()
    return self.get_text_section_header(aside)

  def get_text_aside_body(self):
    aside = self.get_element_aside()
    return self.get_text_section_body(aside)
  
  def click_element_aside_button(self):
    aside = self.get_element_aside()
    self.click_element_section_button(aside)