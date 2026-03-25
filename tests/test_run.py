import pytest
from pathlib import Path
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

# The tests below are here for the demonstration purpose
# and should be replaced with the ones testing the project
# functionality


class TestKedroRun:
    def test_kedro_run_no_pipeline(self):
        # This example test expects a pipeline run failure, since
        # the default project template contains no pipelines.
        bootstrap_project(Path.cwd())

        with pytest.raises(Exception) as excinfo:  # noqa
            with KedroSession.create(project_path=Path.cwd()) as session:
                result = session.run()
                assert result is None
