
if not exist env27\Scripts\python.exe (cmd /c C:/py27arcgis106/ArcGIS10.6/python.exe -m virtualenv --system-site-packages env27)
if not exist env37\Scripts\python.exe (cmd /c "C:\Program Files\Python37\python.exe" -m virtualenv env37)
if not exist env38\Scripts\python.exe (cmd /c "C:\Program Files\Python38\python.exe" -m virtualenv env38)

for %%g in (env27, env37, env38) do (
 %%g\Scripts\python.exe -m pip install %~dp0
)
