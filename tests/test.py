import os
current_path = os.path.dirname(os.path.abspath(__file__))
from zhijie_toolbox import toolbox


toolbox.create_package_template(current_path, "test_project")