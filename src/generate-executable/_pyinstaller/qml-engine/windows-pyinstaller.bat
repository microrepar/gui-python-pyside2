pyinstaller --noconfirm --log-level=WARN ^
--windowed ^
--name="Exemplo" ^
--add-data="icons\;icons" ^
--add-data="MainWindow.qml\;." ^
--paths="C:\Windows\System32\downlevel" ^
--paths="%~dp0\dlls" ^
--icon=icons\icon.ico ^
main_qml_engine.py
