# TableBot
Сделано Богачевой Анной Андреевной. Сервер арендовала у прекрасного Google Cloud'a. Бот данный может в различные манипуляции насущные с таблицами. Собственно вот команды в которые он могет (их описания можно увидеть при вызове /help)
![image](https://user-images.githubusercontent.com/80039591/146097356-65595084-4ffb-420a-b3f0-6adf8e152610.png)
И непосредственно примеры их выполнения\\
![image](https://user-images.githubusercontent.com/80039591/146097439-2ea519a3-fcee-4268-977b-d4083247b11e.png)
![image](https://user-images.githubusercontent.com/80039591/146097482-11e2f751-5fcd-47c4-8d55-62048b71951c.png)
![image](https://user-images.githubusercontent.com/80039591/146097577-49bd3839-8968-446e-8716-987b6d6b4504.png)
![image](https://user-images.githubusercontent.com/80039591/146097662-ef310d1d-3642-4ffa-b7a9-b15b2d4bfd94.png)
![image](https://user-images.githubusercontent.com/80039591/146097703-61bae8d0-8f8a-4426-a4ff-cfdc72438b28.png)
Кому этот бот может быть полезен? Ну возможно людям из фронтенда и людям, которым тяжело читать фронтенд код)0) и визуализировать в разных масштабах разные штуки. Спешу обратить внимание, что все воркфлоу из 3 и 4 пункта оценки есть. Но они представлены в различных джобах, но одном воркфлоу, что разрешалось в рамках выполнения задания!
Автоматический запуск бота на сервере реализовала полностью с помощью Watch Tower, который автоматом притягивает latest из DockerHuba. Содержание docker-compose файла:
version: '3'

services:
  bolaboba:
    image: annabogacheva/for-testing
    labels:
      - "com.centurylinklabs.watchtower.scope=myscope"
    environment:
      TELEGRAM_BOT_TOKEN: "5097013736:AAHOj0LU2GXj8dE2DXDMZlg8vFL8QRdhy0Q"

  watchtower:
    image: containrrr/watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    command: --interval 10 --scope myscope
    labels:
      - "com.centurylinklabs.watchtower.scope=myscope"
