import subprocess
import tempfile
import os
import shutil

def test_full_pipeline():
    orig_cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmpdir:
        # Clone scaffold template and initialize project
        template_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "templates"))
        os.chdir(tmpdir)
        subprocess.run(["copier", "copy", template_path, "test_proj", "--data", "{'project_name':'test_proj'}"], check=True)
        # Run platform checks
        os.chdir("test_proj")
        subprocess.run(["make", "proto2prod-check"], check=True)
        os.chdir(orig_cwd)
