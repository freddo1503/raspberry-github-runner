import subprocess
import json
import os
import uuid
from pathlib import Path
import pytest
from dotenv import load_dotenv

load_dotenv()

TEST_USERNAME = "freddo1503"
TEST_REPOS = ["lexigram", "portfolio"]


@pytest.fixture
def github_token():
    """
    Retrieve the GitHub Personal Access Token (PAT) from environment variables.
    If the token is missing, the test will be skipped.
    """
    token = os.getenv("GITHUB_PAT")
    if not token:
        pytest.skip("Environment variable 'GITHUB_PAT' not set.")
    return token


def test_get_runner_tokens_cli(github_token):
    """
    Test case to validate `get_github_repo_tokens.py` CLI functionality.

    Args:
        github_token (str): GitHub personal access token fixture.
    """
    base_tmp_path = Path("tmp")
    base_tmp_path.mkdir(parents=True, exist_ok=True)

    output_file = base_tmp_path / f"tokens_{uuid.uuid4().hex}.json"
    repo_arg = ",".join(TEST_REPOS)

    try:
        script_path = Path(__file__).resolve().parent.parent.parent / "scripts/get_github_repo_tokens.py"
        cmd = [
            "uv",
            "run",
            str(script_path),
            "--repos", repo_arg,
            "--token", github_token,
            "--username", TEST_USERNAME,
            "--output", str(output_file),
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
        )

        assert result.returncode == 0, f"Script failed: {result.stderr}"

        assert output_file.exists(), "Output file was not created."

        with open(output_file) as f:
            data = json.load(f)

        for repo in TEST_REPOS:
            assert repo in data, f"Repository '{repo}' not found in output."
            assert isinstance(data[repo], str), f"Token for '{repo}' is not a string."
            assert len(data[repo]) > 0, f"Token for '{repo}' is empty."

    finally:
        if output_file.exists():
            output_file.unlink()
        if base_tmp_path.exists() and not any(base_tmp_path.iterdir()):
            base_tmp_path.rmdir()

