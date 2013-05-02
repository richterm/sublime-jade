import sublime_plugin
import sublime
import subprocess
import os
from os.path import *

JADE_PLUGIN_FOLDER = dirname(realpath(__file__)) + os.sep


class JadeCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        selection = self.view.sel()[0]
        selection_text = self.view.substr(selection)
        if(selection.empty()):
            selection = sublime.Region(0, self.view.size())
            selection_text = self.view.substr(selection)
        fileBase = "tmp"
        tmpFile = fileBase + ".jade"
        tmp_file = open(tmpFile, "w")
        tmp_file.write(selection_text)
        tmp_file.close()

        p = subprocess.Popen(["jade -P " + tmpFile], cwd=JADE_PLUGIN_FOLDER, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        (out, err) = p.communicate()

        outFile = JADE_PLUGIN_FOLDER + fileBase + ".html"
        out_file = open(outFile, "r")
        data = out_file.read()
        out_file.close()
        os.remove(outFile)
        os.remove(tmpFile)

        self.view.replace(edit, selection, data)
