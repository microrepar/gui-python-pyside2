pyinstaller --noconfirm --log-level=WARN ^
--windowed ^
--name="Exemplo" ^
--add-data="icons\;icons" ^
--add-data="MainWindow.ui;." ^
--paths="C:\Windows\System32\downlevel" ^
--paths="%~dp0\dlls" ^
--icon=icons\icon.ico ^
mainwindow.py