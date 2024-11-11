from urllib import request
from project import Project
import toml 


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)

        project_info = parsed_toml["tool"]["poetry"]

        name = project_info["name"]
        description = project_info["description"]
        authors = project_info["authors"]
        license = project_info["license"]
        dependencies = project_info["dependencies"]
        dev_dependencies = project_info["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dependencies)
