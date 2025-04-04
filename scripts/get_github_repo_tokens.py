import json
import requests
import typer

app = typer.Typer(help="Get GitHub Actions runner tokens")


def get_runner_token(token: str, github_repo: str, github_username: str):
    """
    Get a registration token for a GitHub Actions runner.

    Args:
        :param token: GitHub Personal Access Token
        :param github_repo: Repository name (e.g., repo-name)
        :param github_username: GitHub username

    Returns:
        str: Runner registration token
    """
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    url = f'https://api.github.com/repos/{github_username}/{github_repo}/actions/runners/registration-token'
    response = requests.post(url, headers=headers)

    if response.status_code != 201:
        print(f"Error retrieving token for {github_repo}: {response.status_code}")
        print(response.text)
        return None

    return response.json()['token']


@app.command()
def main(
    repos: str = typer.Option(..., help="Comma-separated list of repository names (e.g., repo1,repo2)"),
    token: str = typer.Option(..., help="GitHub Personal Access Token"),
    output: str = typer.Option("tokens.json", help="Output JSON file"),
    username: str = typer.Option("freddo1503", help="GitHub username"),
):
    repo_list = [repo.strip() for repo in repos.split(',')]
    results = {}

    for repo in repo_list:
        runner_token = get_runner_token(token, repo, username)
        if runner_token:
            results[repo] = runner_token

    with open(output, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Retrieved tokens for {len(results)} repositories")
    print(f"Tokens saved to {output}")


if __name__ == "__main__":
    app()
