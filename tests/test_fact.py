from typer.testing import CliRunner

from src.catto import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["fact", "--category", "cats"])
    assert result.exit_code == 0
    assert (
        "a fun fact about cats!:"
        in result.stdout.strip("\n").strip(" ").lower()
    ) or ("no fun facts found for cats, sadly" in result.stdout.strip("\n").strip(" ").lower())
