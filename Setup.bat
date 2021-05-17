SET mypath=%CD%

cd "%mypath%" && python -m venv QRCodeGen && cd QRCodeGen\Scripts && activate.bat && python -m pip install qrcode && python -m pip install Pillow