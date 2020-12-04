
# Data Quality Testing & Reporting Process
Full presentation available [![Data & AI Summit](https://www.youtube.com/watch?v=mZ33PJzJtlw&t=142s)](here)

Presentation slides & extended code snippets can be found in PresentationSlides.pdf


## Setup Environment
```
conda create --name datatest python=3.7
conda activate dbconnectappdemo
pip install -r requirements.txt
databricks-connect configure
```
## Mount Delta Lake & Reporting Containers
```
dbutils.fs.mount(
  source = "wasbs://data@<storage-account-name>.blob.core.windows.net",
  mount_point = "/mnt/data",
  extra_configs = {"<conf-key>":dbutils.secrets.get(scope = "<scope-name>", key = "<key-name>")})
```
```
dbutils.fs.mount(
  source = "wasbs://tests@<storage-account-name>.blob.core.windows.net",
  mount_point = "/mnt/tests",
  extra_configs = {"<conf-key>":dbutils.secrets.get(scope = "<scope-name>", key = "<key-name>")})
```

## Build wheel 
```
python setup.py bdist_wheel
```

## Copy project to dbfs (using databricks cli)
```
databricks fs cp -r --overwrite tests dbfs:/datatest/code/tests
databricks fs cp --overwrite dist/datatest-0.0.1-py3-none-any.whl dbfs:/datatest/code
```