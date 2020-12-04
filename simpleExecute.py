import pytest
from datetime import datetime
from pipelines.utils import configmanagement as cm

from pipelines.jobs import run_quality_tests

run_quality_tests.etl("silver/weather/temperatures")
