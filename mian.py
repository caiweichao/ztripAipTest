import os
import pytest

pytest.main(['-s', '-q', '--alluredir=./result'])
# os.system('allure serve ./report')
os.system('allure generate  ./result -o ./reprot --clean')
