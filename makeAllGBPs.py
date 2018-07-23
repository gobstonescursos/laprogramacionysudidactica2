#!/usr/bin/env python
import os
import zipfile

class GBPGenerator:
    def generateAll(self):
        import json
        guides = json.load (open('guides.json'))
        for guide in guides:
            for exercise in guide["exercises"]:
                self.generateGBP(os.path.normpath(exercise["path"]))

    def generateGBP(self,projectPath):
        zipf = zipfile.ZipFile(self.gbpPath(projectPath), 'w', zipfile.ZIP_DEFLATED)
        self.zipdir(projectPath, zipf)
        zipf.close()

    def zipdir(self,path, ziph):
        for root, dirs, files in os.walk(path):
            for file in files:
                realFilepath = os.path.join(root, file)
                ziph.write(realFilepath, os.path.relpath(realFilepath, path))

    def gbpPath(self,projectPath):
        from time import localtime, strftime
        return os.path.join(self.gbpsPath(),os.path.split(projectPath)[1] + '-' +  strftime("%Y%m%d%H%M%S", localtime()) + '.gbp')

    def deleteAll(self):
        if os.path.exists(self.gbpsPath()):
            for item in os.listdir(self.gbpsPath()):
                if item.endswith(".gbp"):
                    os.remove(os.path.join(self.gbpsPath(), item))
        else:
            os.makedirs(self.gbpsPath())

    def gbpsPath(self):
        return os.path.join("Proyectos","ArchivosDeProyectos-Generado")

if __name__ == '__main__':
    GBPGenerator().deleteAll()
    GBPGenerator().generateAll()