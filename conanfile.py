from conans import ConanFile

class HelloPythonReuseConan(ConanFile):
    name = 'HelloPyReuse'
    version = '1.0'
    requires = "HelloPy/0.1@me/testing"

    def build(self):
        from hello import hello
        hello()
