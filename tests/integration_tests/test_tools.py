from typing import Type

from langchain_jenkins.tools import JenkinsJobRun
from langchain_tests.integration_tests import ToolsIntegrationTests


class TestJenkinsJobRunIntegration(ToolsIntegrationTests):
    @property
    def tool_constructor(self) -> Type[JenkinsJobRun]:
        return JenkinsJobRun

    @property
    def tool_constructor_params(self) -> dict:
        # if your tool constructor instead required initialization arguments like
        # `def __init__(self, some_arg: int):`, you would return those here
        # as a dictionary, e.g.: `return {'some_arg': 42}`
        return {}


