from curses import window
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

class BasePage(object):
  MAIN_NAV_ELEMENTS = ('homes', 'why-meritage', 'buyer-resources', 'my-home')
  STATES = ('az', 'ca', 'co', 'fl', 'ga', 'nc', 'sc', 'tn', 'tx', 'map')
  WHY_MERITAGE_NAV_ELEMENTS = ('why-meritage', 'testimonials', 'reviews', 'energy-efficiency', 'how-we-design', 'how-we-build', 'awards')
  BUYER_RESOURCES_NAV_ELEMENTS = ('buyer-resources', 'homebuying', 'home-financing', 'energy-efficiency', 'home-design')
  TOP_BAR_ELEMENTS = ('myaccount', 'agents', 'contact')
  
  def __init__(self, driver):
    self.driver = driver
  
  # get the DOM of the current page, use when testing links and navigation
  def get_html(self): 
    return self.driver.find_element(By.TAG_NAME, 'html')
  
  def get_title(self):
    return self.driver.title
  
  def close_cookies(self):
    cookies_bottom_banner = self.driver.find_elements(By.ID, "onetrust-banner-sdk")
    if len(cookies_bottom_banner) != 0:
      time.sleep(2)
      WebDriverWait(self.driver, timeout=10).until(EC.visibility_of(cookies_bottom_banner[0]))
      result = self.driver.execute_script("return arguments[0].style.display != \"none\"", cookies_bottom_banner[0])
      if result:
        close_cookies = self.driver.find_element(By.XPATH, "//*[@id='onetrust-close-btn-container']/a")
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of(close_cookies))
        close_cookies.click()
        WebDriverWait(self.driver, timeout=10).until(EC.invisibility_of_element(cookies_bottom_banner[0]))
        
  def new_tab(self, original_window):
    WebDriverWait(self.driver, timeout=3).until(EC.number_of_windows_to_be(2))
    for window_handle in self.driver.window_handles:
      if window_handle != original_window:
        self.driver.switch_to.window(window_handle)
        if self.driver.title == '':
          time.sleep(2)
          break
        else:
          break

  def get_text_section_header(self, section):
    header = section.find_element(By.TAG_NAME, 'h2')
    return header.text
  
  def get_text_section_body(self, section):
    body = section.find_element(By.TAG_NAME, 'p')
    return body.text
  
  def click_element_section_button(self, section):
    section.find_element(By.TAG_NAME, 'a').click()

  def get_element_section_placeholder_image(self, section):
    return section.find_element(By.TAG_NAME, "img")
    
  def click_element_section_play_button(self, section):
    section.find_element(By.CLASS_NAME, "video-trigger").click()
  
  def get_input_into_form(self, form):
    form.send_keys('test_input')
    return form.get_attribute('value')

  def get_input_first_name(self, form):
    first_name = form.find_element(By.ID, 'FormModel_FirstName')
    return self.get_input_into_form(first_name)

  def get_input_last_name(self, form):
    last_name = form.find_element(By.ID, 'FormModel_LastName')
    return self.get_input_into_form(last_name)

  # FOR SIGN IN
  def get_input_sign_in_email(self, form):
    email_address = form.find_element(By.ID, 'FormModel_Email')
    return self.get_input_into_form(email_address)

  # FOR CREATE ACCOUNT
  def get_input_create_account_email_address(self, form):
    email_address = form.find_element(By.ID, 'FormModel_EmailAddress')
    return self.get_input_into_form(email_address)

  def get_input_phone_number(self, form):
    phone_number = form.find_element(By.ID, 'FormModel_PhoneNumber')
    return self.get_input_into_form(phone_number)

  # FOR SIGN IN
  def get_input_sign_in_password(self, form):
    password = form.find_element(By.ID, 'FormModel_Password')
    return self.get_input_into_form(password)

  # FOR CREATE ACCOUNT
  def get_input_create_account_password(self, form):
    password = form.find_element(By.ID, 'create_password')
    return self.get_input_into_form(password)
  
  def get_input_confirm_password(self, form):
    confirm_password = form.find_element(By.ID, 'confirm_password')
    return self.get_input_into_form(confirm_password)

  def get_input_company_name(self, form):
    company_name = form.find_element(By.ID, 'FormModel_CompanyName')
    return self.get_input_into_form(company_name)
  
  def get_input_address_1(self, form):
    address_1 = form.find_element(By.ID, 'FormModel_AddressLine1')
    return self.get_input_into_form(address_1)
  
  def get_input_address_2(self, form):
    address_2 = form.find_element(By.ID, 'FormModel_AddressLine2')
    return self.get_input_into_form(address_2)

  def get_input_city(self, form):
    city = form.find_element(By.ID, 'FormModel_City')
    return self.get_input_into_form(city)
  
  def get_input_zip(self, form):
    zip = form.find_element(By.ID, 'FormModel_Zip')
    return self.get_input_into_form(zip)
  
  def get_input_your_question(self, form):
    your_question = form.find_element(By.ID, 'FormModel_YourQuestion')
    return self.get_input_into_form(your_question)
  
  def button_is_clickable(self, button):
    bool = False
    bool = WebDriverWait(self.driver, timeout=4).until(EC.element_to_be_clickable(button))
    return bool
  
  def get_element_youtube_overlay(self):
    return self.driver.find_element(By.ID, 'youtube-video')
  
  def javascript_image(self, image):
    result = self.driver.execute_script("return arguments[0].complete && " + "arguments[0].width > 0", image)
    return result
  
  def get_section_by_aria_label(self, tag_name, aria_label):
    return self.driver.find_element(By.XPATH, f"//{tag_name}[@aria-label='{aria_label}']")
  
  def check_plain_button(self, button):
    return self.driver.execute_script("return arguments[0].classList.contains('plain') && " + "getComputedStyle(arguments[0]).textDecoration.includes('underline')", button)
  
class BasePageHeader(BasePage):
  def header_get_element_meritage_image_container(self):
    return self.driver.find_element(By.CSS_SELECTOR, "body > nav > div.row.full-width.diff.nav--bottom > div > a > div.logo--dark")

  def header_get_element_meritage_image_translucent(self):
    return self.driver.find_element(By.CSS_SELECTOR, ".logo--dark > img:nth-child(1)")

  def header_get_element_search_button(self):
    return self.driver.find_element(By.CSS_SELECTOR, "#button--search")

  def header_get_element_site_search_overlay(self):
    return self.driver.find_element(By.CSS_SELECTOR, "#site-search--overlay")
  
  def header_click_search_button(self):
    self.header_get_element_search_button().click()

  def header_get_element_top_bar_info(self, element):
    return self.driver.find_element(By.XPATH, f"//a[@href='/{element}']")
  
  def header_click_top_bar_element(self, element):
    html = self.get_html()
    header_top_bar_element = self.header_get_element_top_bar_info(element)
    header_top_bar_element.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
  
  def header_get_element_header_main(self, element):
    return self.driver.find_element(By.XPATH, f"//a[@href='/{element}']")

  def header_click_main_element(self, element):
    html = self.get_html()
    header_main_element = self.header_get_element_header_main(element)
    header_main_element.click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html)) # wait until the entire old webpage is not present until we assert for the title of the new page

  def header_get_element_header_level2(self, level1_element, level2_element):
    level1 = self.header_get_element_header_main(level1_element)
    if level1_element != level2_element:
      if level1_element == 'homes':
        if level2_element == 'map':
          return level1.find_element(By.XPATH, f"//a[@href='/{level1_element}']")
        else:
          return level1.find_element(By.XPATH, f"//a[@href='/state/{level2_element}']")
      else:
        return level1.find_element(By.XPATH, f"//a[@href='/{level1_element}/{level2_element}']")
    else:
      return level1.find_element(By.XPATH, f"//a[@href='/{level1_element}']")

  def header_click_level2_element(self, level1_element, level2_element):
    html = self.get_html()
    header_main_element = self.header_get_element_header_main(level1_element)
    header_level2_element = self.header_get_element_header_level2(level1_element, level2_element)
    
    action = ActionChains(self.driver)
    action.move_to_element(header_main_element).move_by_offset(0, 50).move_to_element(header_level2_element).click().perform()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
    if self.driver.title == '':
      time.sleep(5) # Firefox takes longer to load the title for some reason
    

class BasePageFooter(BasePage):
  def footer_get_element_footer(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer")
  
  def footer_get_element_company_nav_block(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[1]")

  def footer_get_element_contact_nav_block(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[2]")
  
  def footer_click_element_company_element(self, element):
    if element != '5':
      html = self.get_html()
      contact_block = self.footer_get_element_company_nav_block() 
      contact_block.find_element(By.XPATH, f"/html/body/footer/div[1]/div/div/div[1]/ul/li[{element}]/a").click()
      WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
    else: # Clicking the fith element opens the window in a new tab
      original_window = self.driver.current_window_handle
      contact_block = self.footer_get_element_company_nav_block() 
      contact_block.find_element(By.XPATH, f"/html/body/footer/div[1]/div/div/div[1]/ul/li[{element}]/a").click()
      WebDriverWait(self.driver, timeout=3).until(EC.number_of_windows_to_be(2))
      for window_handle in self.driver.window_handles:
        if window_handle != original_window:
          self.driver.switch_to.window(window_handle)
          break
    if self.driver.title == '':
      time.sleep(3)
    
  def footer_click_element_contact_element(self, element):
    html = self.get_html()
    contact_block = self.footer_get_element_contact_nav_block() 
    contact_block.find_element(By.XPATH, f"/html/body/footer/div[1]/div/div/div[2]/ul/li[{element}]/a").click()
    WebDriverWait(self.driver, timeout=15).until(EC.staleness_of(html))
  
  def footer_get_element_optin_signup(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[4]/div")
  
  def footer_get_element_email_form_input(self):
    return self.driver.find_element(By.ID, "footer-open-modal-email")
  
  def footer_get_element_email_form_enter(self):
    return self.driver.find_element(By.ID, "footer-open-modal-trigger")
  
  def footer_get_element_email_form_error_image(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[4]/div/form/div[1]/div[2]")
  
  def footer_get_element_error_message(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[4]/div/form/div[2]")
  
  def footer_enter_keys_email_form_input(self):
    email_input = self.footer_get_element_email_form_input()
    email_input.send_keys('NotAValidEmail')
  
  def footer_click_element_email_form_enter(self):
    email_enter = self.footer_get_element_email_form_enter()
    email_enter.click()
  
  def footer_get_element_socials(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[5]/div[2]")
  
  def footer_click_element_social_media_link(self, element):
    original_window = self.driver.current_window_handle
    socials = self.footer_get_element_socials()
    social_media_link = socials.find_element(By.XPATH, f"/html/body/footer/div[1]/div/div/div[5]/div[2]/a[{element}]")  
    social_media_link.click()
    WebDriverWait(self.driver, timeout=3).until(EC.number_of_windows_to_be(2))
    for window_handle in self.driver.window_handles:
      if window_handle != original_window:
        self.driver.switch_to.window(window_handle)
        break
    if self.driver.title == '':
      time.sleep(3)
  
  def footer_click_element_privacy_policy_links(self, element):
    original_window = self.driver.current_window_handle
    privacy_element = self.driver.find_element(By.XPATH, f"/html/body/footer/div[2]/div/div/div[1]/div[1]/ul/li[{element}]/a")
    privacy_element.click()
    if element == '4': # My Meritage Portal opens in a new tab
      WebDriverWait(self.driver, timeout=3).until(EC.number_of_windows_to_be(2))
      for window_handle in self.driver.window_handles:
        if window_handle != original_window:
          self.driver.switch_to.window(window_handle)
          break
      if self.driver.title == '':
        time.sleep(3)
      
  def footer_get_element_uncollapsable_disclaimer(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[2]/div/div/div[2]/div/div/p[1]")
  
  def footer_get_text_uncollapsable_disclaimer(self):
    uncollapse_disclaimer = self.footer_get_element_uncollapsable_disclaimer()
    return uncollapse_disclaimer.text
  
  def footer_get_element_read_more(self):
    return self.driver.find_element(By.ID, "FooterReadMore")
  
  def footer_click_element_read_more(self):
    read_more = self.footer_get_element_read_more()
    read_more.click()
  
  def footer_get_element_read_more_wrapper(self):
    return self.driver.find_element(By.ID, "FooterReadMoreWrapper")
  
  def footer_get_element_green_read_more_button(self):
    return self.driver.find_element(By.ID, "ot-sdk-btn")
  
  def footer_click_element_green_read_more_button(self):
    green_read_more = self.footer_get_element_green_read_more_button()
    green_read_more.click()
  
  def footer_get_element_onetrust_overlay_on_green_press(self):
    return self.driver.find_element(By.ID, "onetrust-pc-sdk")
  
  def footer_get_element_eho_image(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[2]/div/div/div[1]/div[2]/ul/li[1]/img")
  
  def footer_get_element_energy_star_image(self):
    return self.driver.find_element(By.XPATH, "/html/body/footer/div[2]/div/div/div[1]/div[2]/ul/li[2]/img")