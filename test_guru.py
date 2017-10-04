from selenium import webdriver
import logging
import time
from nose import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logging.basicConfig(filename="sample.log", level=logging.INFO,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
                    datefmt="%Y-%m-%d %H:%M:%S")

#test to see scm
class ecom():
    def __init__(self,url):
        self.url=url
        self.driver = webdriver.Chrome("C:\chromedriver.exe")
        self.driver.implicitly_wait(30)



        try:
            self.driver.get(self.url)



            logging.info("Logging to Guru bank console")




        except Exception as e:
            logging.error("Logging to openstack console failed")




    def close(self):
        self.driver.quit()

    def mobile(self):

        mobile_page=self.driver.find_element_by_xpath("//*[@id='nav']/ol/li[1]/a")
        mobile_page.click()
        return self.driver.page_source

    def current_url(self):
        return self.driver.current_url

    def page_source(self):
        return self.driver.page_source

    def mobile_sort(self):
        mobile_page = self.driver.find_element_by_xpath("//*[@id='nav']/ol/li[1]/a")
        mobile_page.click()
        sort_page=self.driver.find_element_by_xpath("//select[@title='Sort By']/option[@value='http://live.guru99.com/index.php/mobile.html?dir=asc&order=name']")
        sort_page.click()
        Mobile_names=self.driver.find_elements_by_xpath(".//a[@class='product-image']")
        self.names=[]
        for i in Mobile_names:
            self.names.append(i.get_attribute("title"))
        if sorted(self.names)==self.names:

            return True
        else:
            return False





    def verify_cost(self):
        flag=True
        mobile_page = self.driver.find_element_by_xpath("//*[@id='nav']/ol/li[1]/a")
        mobile_page.click()
        Mobile_names=self.driver.find_elements_by_xpath(".//a[@class='product-image']")
        print(Mobile_names)
        Mobile_price = self.driver.find_elements_by_xpath("//div[@class='product-info']//div[@class='price-box']//span[@class='price']")

        self.names_price = []
        for i,v in zip(Mobile_names,Mobile_price):

            self.names_price.append((i.get_attribute('title'),v.text))


        for i,v in self.names_price:
             Mobile_page=self.driver.find_element_by_xpath(".//a[@title='{}']".format(str(i))).click()
             if self.driver.find_element_by_xpath(".//div[@class='price-box']//span[@class='price']").text!=v:
                 flag=False
             self.driver.back()
        if flag==True:

            return True
        else:
            return False


    def verify_more_product(self):
         mobile_page = self.driver.find_element_by_xpath("//*[@id='nav']/ol/li[1]/a")
         mobile_page.click()
         cart=self.driver.find_element_by_xpath("//button[@title='Add to Cart']").click()
         quantity=self.driver.find_element_by_xpath("//input[@title='Qty']").send_keys("1000")
         update=self.driver.find_element_by_xpath("//button[@title='Update']").click()
         if "The maximum quantity allowed for purchase is 500" in self.driver.page_source:

             return True
         else:

             return False

    def verify_pop_up(self):
        flag=True
        mobile_page = self.driver.find_element_by_xpath("//*[@id='nav']/ol/li[1]/a")
        mobile_page.click()
        Mobile_names = self.driver.find_elements_by_xpath(".//a[@class='product-image']")

        names=[]
        for i in Mobile_names[0:2]:
            names.append(i.get_attribute("title"))

        for i in names:

            Mobile_page = self.driver.find_element_by_xpath(".//a[@title='{}']".format(str(i))).click()
            compare=self.driver.find_element_by_xpath("//a[@class='link-compare']").click()
            self.driver.back()
            self.driver.back()
        window_before = self.driver.window_handles[0]
        compare=self.driver.find_element_by_xpath("//button[@title='Compare']").click()
        window_after=self.driver.window_handles[1]

        switch=self.driver.switch_to.window(window_after)

        for i in names:
            if i not in self.driver.page_source:
                flag=False


        if flag==True:

            return True
        else:

            return False



    def create_account(self,firstname,lastname,email,password):

        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.password=password
        Account_menu=self.driver.find_element_by_xpath("//a[@href='http://live.guru99.com/index.php/customer/account/']/span[2]").click()
        My_account=self.driver.find_element_by_xpath("//a[@title='My Account']").click()
        Create_account=self.driver.find_element_by_xpath("//a[@title='Create an Account']").click()
        first_name=self.driver.find_element_by_xpath("//*[@id='firstname']").send_keys(self.firstname)
        last_name=self.driver.find_element_by_xpath("//*[@id='lastname']").send_keys(self.lastname)
        email=self.driver.find_element_by_xpath("//*[@id='email_address']").send_keys(self.email)
        password=self.driver.find_element_by_xpath("//*[@id='password']").send_keys(self.password)
        confirmation=self.driver.find_element_by_xpath("//*[@id='confirmation']").send_keys(self.password)
        Register=self.driver.find_element_by_xpath("//div/button[@title='Register']").click()


        if "There is already an account with this email address" in self.driver.page_source:
            self.driver.back()
            self.driver.back()
            email=self.driver.find_element_by_xpath("//*[@id='email']").send_keys(self.email)
            password=self.driver.find_element_by_xpath("//*[@id='pass']").send_keys(self.password)
            self.driver.find_element_by_xpath("//*[@id='send2']").click()
        elif "Thank you for registering with Main Website Store" not in  self.driver.page_source:
            return False





        tv_page=self.driver.find_element_by_xpath(".//a[@href='http://live.guru99.com/index.php/tv.html']").click()
        wishlists=self.driver.find_element_by_xpath("//a[@class='link-wishlist']").click()


        share_wishlist=self.driver.find_element_by_xpath("//div/button[@title='Share Wishlist']").click()
        enter_email=self.driver.find_element_by_xpath("//*[@id='email_address']").send_keys(self.email)
        share_list=self.driver.find_element_by_xpath("//div//button[@title='Share Wishlist']").click()
        if "Your Wishlist has been shared" not in self.driver.page_source:
            return False


        return True




























a1=ecom("http://live.guru99.com/index.php/")
a1.create_account('Rakesh','singh','rakeshsingh556575@gmail.com',"tcet@123")




def test_correct_user_pass():
    a1 = ecom("http://live.guru99.com/index.php/")
    assert "http://live.guru99.com/index.php/" == a1.current_url()

    a1.close()

def test_title():
    a1 = ecom("http://live.guru99.com/index.php/")
    assert "This is demo site for" in  a1.page_source()

    a1.close()

def test_mobile():
    a1 = ecom("http://live.guru99.com/index.php/")
    assert "Mobile" in a1.mobile()
    a1.close()


def test_sorted_mobile_names():
    a1 = ecom("http://live.guru99.com/index.php/")
    assert a1.mobile_sort()==True
    a1.close()


def test_price():
    a1 = ecom("http://live.guru99.com/index.php/")
    assert a1.verify_cost() == True
    a1.close()


def test_no_products():
    a1 = ecom("http://live.guru99.com/index.php/")
    assert a1.verify_more_product() == True
    a1.close()



def test_pop_up():
    a1 = ecom("http://live.guru99.com/index.php/")
    assert a1.verify_pop_up() == True
    a1.close()


def test_account_creation():
    a1 = ecom("http://live.guru99.com/index.php/")
    assert a1.create_account('Rakesh','singh','rakeshsingh556575@gmail.com',"tcet@123")==True
    a1.close()