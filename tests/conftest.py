from pipelines.utils import configmanagement as cm
from datetime import datetime
import platform
import os


def pytest_cmdline_preparse(config, args):
    
    datetime_now_str = datetime.now().strftime('%Y%m%dT%H%M%S%f')
    html_file = f'tests/reports/{datetime_now_str}-quality-report.html'
    
    if not cm.is_local():
        html_file = f'/{html_file}'

    args.extend(['--html', html_file, '--self-contained-html'])

def pytest_unconfigure(config):
    if not cm.is_local():
        html_report_path = os.path.join(config.invocation_dir.strpath, config.option.htmlpath)
        test_path = config.option.file_or_dir[0].replace("./","").replace(".py", "").replace("/dbfs/datatest/code/", "")

        file_name = html_report_path.split("/")[-1]
        cm.get_dbutils().fs.cp(f"file:///{html_report_path}", f"/mnt/{test_path}/{file_name}")
            
        






        
        
