import os
import sys
sys.path.append(os.path.abspath('../../'))
from cheapBuy.test.test_server_api import *

def test_answer():
   # test_server_api.py
   test_post_result()
   test_post_result_status()
   test_post_result_response_ebay()
