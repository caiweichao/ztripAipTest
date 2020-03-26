import os
import pytest

pytest.main(['-s', '-q', '--alluredir=./report'])
# os.system('allure serve ./report')
# os.system('allure generate  ./report/allure_results/ -o unit/allure_html')
