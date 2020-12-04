import pytest
from datetime import datetime
from pipelines.utils import configmanagement as cm

def etl(table_path):

    test_path = f"tests/{table_path}_test.py"

    if not cm.is_local():
        test_path = f"/dbfs/datatest/code/{test_path}"
    
    exit_code = pytest.main([test_path])

    if exit_code.value in (1,2,3,4,5): 
        raise Exception("Test(s) failed - check test report")



