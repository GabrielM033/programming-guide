# Comandos Docker

### Buildar imagem Dockerfile 🛠️
- docker build -t nome-imagem .

### Executar imagem ▶️
- docker run -p 8000:8000 nome-imagem

### Validar se o container está em execução 🔍
- docker ps

### Acessar o container 🗃️
- docker exec -it nome-container bash
- docker exec -it nome-container sh

### Sair do container 🗄️
- exit ou ctrl + D

### Consumo de mémoria do container e etc... 📊
- docker stats nome-container

###  Capturar logs ⚙️
- docker logs -f nome-container
- docker logs --tail 100 nome-container

### Pausar e inicar um container ⏯️
- docker stop nome-container
- docker start nome-container

### Deletar um container ❌
- docker rm nome-container