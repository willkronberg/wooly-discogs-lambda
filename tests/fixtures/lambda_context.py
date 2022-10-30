import pytest


class LambdaContext:
    def __init__(self):
        self.function_name = "test-function-name"
        self.memory_limit_in_mb = 1024
        self.invoked_function_arn = "test-function-arn"
        self.aws_request_id = "test-request-id"


@pytest.fixture
def lambda_context():
    return LambdaContext()
