from page_reviews import ReviewsPage
from page_base import BasePage
import pytest
import time
from pathlib import *

# This page has IFRAMES on it. Check out page_reviews.py please...
# I could have just made to Test_ classes in this file, one testing the meritage page and one testing the iframe (they have their own URLs). I think I will do that next time...
URL = 'https://cd-sit.meritageweb.dev/why-meritage/reviews'

@pytest.mark.usefixtures("init__driver")
class BasicTest():
  pass

class Test_Reviews_Page(BasicTest):
  @pytest.fixture()
  def driver_settings(self):
    self.driver.get(URL)
  
  # Test the main header
  def test_main_header(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    header = review_page.get_text_main_header()
    assert "Hear from our Customers" in header
  
  # Test whether correct header displays in the default review summary section
  def test_view_1_header(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    header = review_page.get_text_reviews_summary_view_1_header()
    assert "review summary" in header
  
  # Test whether the rating values 5-1 are present on right side of default review summary view
  def test_view_1_rating_values(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    numbers = review_page.get_elements_reviews_summary_view_1_rating_value()
    assert 5 and 4 and 3 and 2 and 1 in numbers
  
  # Test whether each number has a star present next to it in default reviews summary view
  def test_view_1_stars(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    stars = review_page.get_elements_reviews_summary_view_1_stars()
    assert len(stars) == 5
  
  # Test whether the overall rating is displayed on the page
  def test_view_1_rating(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    rating = review_page.get_text_review_summary_view_1_rating()
    assert float(rating) > 0
  
  # Test whether the stars under the overall rating appear
  def test_view_1_rating_stars(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    stars = review_page.get_elements_review_summary_view_1_rating_stars()
    assert len(stars) == 5
  
  # Test whether the reviews sub text appears under the stars on default view of review summary container
  def test_view_1_number_reviews(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    text = review_page.get_text_review_summary_view_1_reviews_number()
    assert 'reviews' in text
  
  # Test whether the contact us button in default view navigates to the correct view when clicked
  def test_view_1_contact_us_button(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    review_page.close_cookies()
    review_page.click_element_review_summary_view_1_contact_us_button()
    assert '' == self.driver.title
  
  # Test whether the write review button opens up view 2 of the review summary container (top of the internal scroll window and above all of the reviews themselves) when clicked.
  def test_view_1_to_view_2_on_write_review_click(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    review_page.close_cookies()
    review_page.click_element_review_summary_view_1_write_review_button()
    view_2 = review_page.get_element_review_summary_view_2()
    result = self.driver.execute_script("return arguments[0].classList.contains('hidden') == false", view_2)
    assert result 
  
  # Test whether correct header is displayed for view 2 in the review summary container
  def test_view_2_header(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    review_page.click_element_review_summary_view_1_write_review_button()
    header = review_page.get_text_review_summary_view_2_header()
    assert 'Write a review' in header
  
  # Test whether correct text is displayed in view 2.
  def test_view_2_sub_header(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    review_page.click_element_review_summary_view_1_write_review_button()
    text = review_page.get_text_review_summary_view_2_sub_header()
    assert 'Great! Where would you like to write your review' in text
  
  # Test whether the google button navigates user to correct tab when clicked
  def test_view_2_google_button(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    review_page.click_element_review_summary_view_1_write_review_button()
    review_page.click_element_review_summary_view_2_google_button()
    assert 'Sign in - Google Accounts' or '' == self.driver.title
  
  # Test whether the pencil button opens view 3 in this container
  @pytest.mark.review
  def test_view_2_to_view_3_on_pencil_press(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    review_page.click_element_review_summary_view_1_write_review_button()
    review_page.click_element_review_summary_view_2_pencil_button()
    assert 'Meritage Homes Corporation | Better Business Bureau® Profile' or '' == self.driver.title
  
  # iFrame for view 3 changed. Now opens a new tab to third party...
  # # Test whether correct header appears in view 3
  # def test_view_3_header(self, driver_settings):
  #   review_page = ReviewsPage(self.driver)
  #   review_page.click_element_review_summary_view_1_write_review_button()
  #   review_page.click_element_review_summary_view_2_pencil_button()
  #   header = review_page.get_text_review_summary_view_3_header()
  #   assert 'Write a Review' in header
  
  # # Test whether clicking each star in view 3 changes it to orange
  # @pytest.mark.parametrize('star', [0, 1, 2, 3, 4])
  # def test_view_3_stars(self, star, driver_settings):
  #   review_page = ReviewsPage(self.driver)
  #   review_page.click_element_review_summary_view_1_write_review_button()
  #   review_page.click_element_review_summary_view_2_pencil_button()
  #   stars = review_page.get_elements_review_summary_view_3_stars()
  #   review_page.click_element_review_summary_view_3_star(star)
  #   result = self.driver.execute_script("return arguments[0].classList.contains('be-star-on')", stars[star])
  #   assert result
  
  # # Test whether the user can input text into the text area in view 3
  # def test_view_3_input(self, driver_settings):
  #   review_page = ReviewsPage(self.driver)
  #   review_page.click_element_review_summary_view_1_write_review_button()
  #   review_page.click_element_review_summary_view_2_pencil_button()
  #   input_text = review_page.get_input_review_summary_view_3_describe_experience()
  #   assert "test_input" == input_text
  
  # # Test whether the correct sub text appears below the text area in view 3
  # def test_view_3_sub_text(self, driver_settings):
  #   review_page = ReviewsPage(self.driver)
  #   review_page.click_element_review_summary_view_1_write_review_button()
  #   review_page.click_element_review_summary_view_2_pencil_button()
  #   sub_text = review_page.get_text_review_summary_view_3_sub_text()
  #   assert 'We recommend reviews to be at least 50 characters' in sub_text
  
  # # Test whether the correct text appears beneath the sub text in view 3
  # def test_view_3_sub_sub_text(self, driver_settings):
  #   review_page = ReviewsPage(self.driver)
  #   review_page.click_element_review_summary_view_1_write_review_button()
  #   review_page.click_element_review_summary_view_2_pencil_button()
  #   sub_sub_text = review_page.get_text_review_summary_view_3_sub_sub_text()
  #   assert 'Your review may be shared publicly on the web' in sub_sub_text
  
  # # Test whether the privacy policy button opens the "birdeye" privacy policy tab when clicked
  # def test_view_3_birdeye_on_privacy_policy_click(self, driver_settings):
  #   review_page = ReviewsPage(self.driver)
  #   review_page.click_element_review_summary_view_1_write_review_button()
  #   review_page.click_element_review_summary_view_2_pencil_button()
  #   review_page.click_element_review_summary_view_3_privacy_policy()
  #   assert 'New Message' or 'Privacy Policy' in self.driver.title
  
  # # Test whether the terms of service button opens the "birdeye" terms of service tab when clicked
  # def test_view_3_birdeye_on_terms_of_service_click(self, driver_settings):
  #   review_page = ReviewsPage(self.driver)
  #   review_page.click_element_review_summary_view_1_write_review_button()
  #   review_page.click_element_review_summary_view_2_pencil_button()
  #   review_page.click_element_review_summary_view_3_terms_of_service()
  #   assert 'New Message' or 'Terms' in self.driver.title
  
  # # Test whether the green submit button in view 3 is clickable. (I do not want to submit anything so do not actually click in the Page Object method)
  # def test_view_3_submit_button_is_clickable(self, driver_settings):
  #   review_page = ReviewsPage(self.driver)
  #   review_page.click_element_review_summary_view_1_write_review_button()
  #   review_page.click_element_review_summary_view_2_pencil_button()
  #   is_clickable = review_page.check_element_review_summary_view_3_button_is_clickable()
  #   assert is_clickable
  
  # Test whether more reviews populate when the user scrolls down
  def test_more_reviews_on_scroll(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    default_reviews_displayed = review_page.get_elements_all_reviews()
    review_page.scroll_down()
    after_scroll_reviews_displayed = review_page.get_elements_all_reviews()
    assert len(after_scroll_reviews_displayed) > len(default_reviews_displayed)
  
  # Test whether correct header appears in aside section
  def test_aside_header(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    header = review_page.get_text_aside_header()
    assert 'Your story begins here' in header
  
  # Test whether correct body appears in aside section
  def test_aside_body(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    body = review_page.get_text_aside_body()
    assert 'There are many great homes' in body
  
  # Test whether the aside button navigates to correct page on press
  def test_aside_button(self, driver_settings):
    review_page = ReviewsPage(self.driver)
    review_page.close_cookies()
    review_page.click_element_aside_button()
    assert 'Find a Home | Meritage Homes' == self.driver.title