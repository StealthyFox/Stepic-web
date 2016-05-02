mkdir web
git clone https://github.com/stealthyfox/web web

#символическая ссылка (sudo ln -sf : с удалением существующих целевых файлов)
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
# -rf удаление конфига по умолчанию (с ним не хватает памяти), из-за удаления может быть ошибка соединения
sudo rm /etc/nginx/sites-enabled/default #в sites-en только test.conf

#В скрипте init.sh, который предлагалось написать, удобней сразу перезаписывать ссылку на дефолтную конфигурацию:
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default

sudo /etc/init.d/nginx restart



sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

#Просмотр логов
sudo cat /var/log/nginx/error.log
#удаление символической ссылки
sudo rm /etc/nginx/sites-enabled/test.conf
#проверка, что символическая ссылка ведет на ваш конфиг
cat /etc/nginx/sites-enabled/test.conf
#для проверки ответа на запрос
curl -I http://localhost:80/uploads/1.html
#_________________________________________________________
  location ~* ^.+\.\w+$ {
    root /home/box/web/public;
  }

listen *:80;
listen 80 default;
http://www.rubular.com/﻿ - проверка регулярок
