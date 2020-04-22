import os
import pytest

pytest.main(['-s', '-q', '--alluredir=./result'])
os.system('allure serve ./result')

