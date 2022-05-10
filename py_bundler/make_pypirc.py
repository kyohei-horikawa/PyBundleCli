def make_pypirc(pypi_account, pypi_password, test_pypi_account, test_pypi_password):
    template = f"""[distutils]
index-servers =
  pypi
  testpypi

[pypi]
repository: https://upload.pypi.org/legacy/
username: {pypi_account}
password: {pypi_password}

[testpypi]
repository: https://test.pypi.org/legacy/
username: {test_pypi_account}
password: {test_pypi_password}
"""
    with open('.pypirc', 'w') as f:
        f.write(template)
