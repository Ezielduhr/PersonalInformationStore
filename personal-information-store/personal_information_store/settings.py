import os
from pathlib import Path

application_settings = {}
repository_name = 'PersonalInformationStore'
current_working_directory = Path.cwd()
if repository_name in current_working_directory.parts:
    application_settings['root_dir'] = str(current_working_directory.parent).split(repository_name)[0] + repository_name
else:
    application_settings['root_dir'] = str(Path.home())

def export_settings():
    for setting, value in application_settings.items():
        os.environ[setting] = value
