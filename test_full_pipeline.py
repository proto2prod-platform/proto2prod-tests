import subprocess
import tempfile
import os
import shutil

def test_full_pipeline():
    # Clone scaffold template and initialize project
    with tempfile.TemporaryDirectory() as tmpdir:
        os.chdir(tmpdir)
        subprocess.run(["copier", "repo", "../templates", "--data", "{'project_name':'test_proj'}"], check=True)
        # Run platform checks
        os.chdir("test_proj")
        subprocess.run(["make", "proto2prod-check"], check=True)
