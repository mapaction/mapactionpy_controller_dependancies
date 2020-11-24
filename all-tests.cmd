
:: env3 set DISTUTILS_DEBUG=true

:: Py 2.7
.\env27\Scripts\python.exe -m autopep8 --in-place --max-line-length=120 --recursive . --exclude ./env*

for %%g in (env27, env37, env38) do (
 %%g\Scripts\python.exe .\test_imports.py
)

