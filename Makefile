VENV_NAME = .venv


PYTHON = $(VENV_NAME)/bin/python
PIP = $(VENV_NAME)/bin/pip
VENV_INIT = $(VENV_NAME)/Scripts/Activate

setup: $(VENV_NAME)  
# @echo "Instalando dependências..."
# $(PIP) install --upgrade pip setuptools wheel
# $(PIP) install -r requirements.txt
	@echo "Ambiente configurado!"

$(VENV_NAME):  
	@echo "Criando ambiente virtual..."
	python3 -m venv $(VENV_NAME)
	@echo "Ambiente virtual criado em $(VENV_NAME)"