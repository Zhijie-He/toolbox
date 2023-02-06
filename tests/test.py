import os
current_path = os.path.dirname(os.path.abspath(__file__))
from zhijie_toolbox import toolbox

toolbox.create_package_template(current_path, "test_project")
toolbox.version_control(current_path, runs_name="A2")