__author__ = 'Konstantin Dmitriev'

import os.path

class RenderChanFile():
    def __init__(self, path, modules, projects):
        self.targetFormat = ""
        self.projectPath = self._findProjectRoot(path)
        #self.project = projects.get(self.projectPath)
        self.localPath = self._findLocalPath(path)
        self.project=projects.get(self.projectPath)
        self.module = modules.getByExtension(os.path.splitext(path)[1][1:])

        # Load Module


    def _findProjectRoot(self, path):
        while True:
            if os.path.exists(os.path.join(path,"project.conf")) or os.path.exists(os.path.join(path,"remake.conf")):
                return path
            if os.path.dirname(path) == path:
                return ""
            path = os.path.dirname(path)

    def _findLocalPath(self, path):
        if path.startswith(self.projectPath):
            localpath=path[len(self.projectPath):]
            while localpath.startswith('/'):
                localpath=localpath[1:]
            return localpath
        else:
            return path

    def getProjectRoot(self):
        return self.projectPath

    def getPath(self):
        return os.path.join(self.projectPath, self.localPath)

    def getRenderPath(self):
        return os.path.join(self.projectPath, "render", self.localPath+"."+self.targetFormat )

    def getProfileRenderPath(self):
        profile = "480x270"
        return os.path.join(self.projectPath, "render", "project.conf", profile, self.localPath+"."+self.targetFormat )

    def getOutputFormat(self):
        # Check for project-defined format
        format=self.project.getFormat()
        # TODO: Check for .conf file for this module
        # ...
        # TODO: Allow module to override format
        #self.module.overrideFormat(format)
        return format

    def getDependencies(self):
        return []

    def isValid(self):
        if self.projectPath != "":
            return True
        else:
            return False