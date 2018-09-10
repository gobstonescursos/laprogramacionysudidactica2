#!/usr/bin/env python
import os
import zipfile
import hashlib

class GBPGenerator:
    currentTime = None

    def generateAll(self):
        import json
        guides = json.load (open('guides.json'))
        for guide in guides:
            for exercise in guide["exercises"]:
                self.updateGBP(os.path.normpath(exercise["path"]))

    def updateGBP(self, projectPath):
        # If it doesn't exist a GBP for this project, generate it and return.
        try:
            existinggbpPath = self.findExistingGBP(projectPath)
        except NotFoundError:
            print("Will generate new GBP: " + self.gbpPath(projectPath))
            return
        finally:
            self.generateGBP(projectPath)
        
        # If it actually does exist a previous GBP, discard the newly generated in case it is the same as the existent
        # This way the script only generates GBPs for projects that did change.
        if MD5().equals(existinggbpPath, self.gbpPath(projectPath)):
            os.remove(self.gbpPath(projectPath))
        else:
            # In case the new one has changed, then we can remove the previous one.
            print("Project changed, GBP updated: " + self.gbpPath(projectPath))
            os.remove(existinggbpPath)

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
        if self.currentTime is None: # One time for all script execution. This way if I call gbpPath twice with same parameter, it returns the same value.
            from time import localtime, strftime
            self.currentTime = strftime("%Y-%m-%d-%H%M%S", localtime())
        
        return os.path.join(self.gbpsPath(),os.path.split(projectPath)[1] + '-' + self.currentTime + '.gbp')    

    def deleteAll(self):
        if os.path.exists(self.gbpsPath()):
            for item in os.listdir(self.gbpsPath()):
                if item.endswith(".gbp"):
                    os.remove(os.path.join(self.gbpsPath(), item))
        else:
            os.makedirs(self.gbpsPath())

    def gbpsPath(self):
        return os.path.join("Proyectos","ArchivosDeProyectos-Generado")

    def findExistingGBP(self,projectPath): # Returns the last generated gbp path (sorts by filename)
        import os, fnmatch
        result = []
        for root, dirs, files in os.walk(self.gbpsPath()):
            for name in sorted(files):
                if name.startswith(os.path.split(projectPath)[1].encode('utf8')):
                    result.append(os.path.join(root, name))
        
        if result == []:
            raise NotFoundError("Path not found: " + projectPath)

        return result[-1]

class NotFoundError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class MD5:
    def sum(self,fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def equals(self, fname1, fname2):
        return self.sum(fname1) == self.sum(fname2)
    

if __name__ == '__main__':
    # GBPGenerator().deleteAll()
    GBPGenerator().generateAll()