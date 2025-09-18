# Como roda esse trem

python manage.py migrate para o backend do django 

Em outro terminal, cd frontend, npm install vue-router pinia -> para os packages do node


#Teste

Caso queira testar os emails com link de reset, tenha o docker desktop aberto, depois em outro terminal separado: docker run -d -p 1025:1025 -p 8025:8025 --name mailhog mailhog/mailhog

Após isso, accesse http://localhost:8025 para o mailhog

Pronto! Vai simular como se fosse uma caixa de email :3


