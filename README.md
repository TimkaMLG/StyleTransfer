# StyleTransfer
Python telegram bot for style transfer between two photos. It can be found [here](https://t.me/cool_style_bot).

At the time of publication of this text the bot is running on [VK Cloud](https://mcs.mail.ru/) service, and will probably runs for the next month with interruptions for technical issues, then access to the bot via the link is not guaranteed.

Model
----------
For transferring style I chose [MSG-Net](https://github.com/zhanghang1989/PyTorch-Multi-Style-Transfer) implemented by [zhanghang1989](https://github.com/zhanghang1989). It is already pre-trained and small enough to work out in a few seconds per image. A little bit corrected for my purposes code is placed in [model.py](https://github.com/TimkaMLG/StyleTransfer/blob/main/model.py). 
Photo examples can be found in the [examples](https://github.com/TimkaMLG/StyleTransfer/tree/main/examples) folder.
The pre-trained weights of the model are placed in [21styles.model](https://github.com/TimkaMLG/StyleTransfer/blob/main/21styles.model).

<p align="center">
  <img src="examples/candy.jpg" width="350" title="First photo">
  <img src="examples/venice-boat.jpg" width="560" title="Second photo">
  <img src="examples/output.jpg" width="560" title="Result photo">
</p>

Bot
------
I used [pyTelegramBotApi](https://github.com/eternnoir/pyTelegramBotAPI) framework for the bot. It was chosen because it is quite simple and flexible, and also allows to write asynchronous code, which is very useful for Telegram bots. The intuitive interface of the bot is implemented using buttons, there is also detailed instruction for the user how to work with bot.
While working with bot, users photos are stored in the [chats](https://github.com/TimkaMLG/StyleTransfer/tree/main/chats) folder in subfolders with chat_id names.
The bots code is in [main.py](https://github.com/TimkaMLG/StyleTransfer/blob/main/main.py).

Setup
--------
To launch the bot, you should get a unique token [here](https://t.me/BotFather). Next, put it in the [main.py](https://github.com/TimkaMLG/StyleTransfer/blob/main/main.py) in line number 9 instead of `token = get_token()` write `token = <YOUR TOKEN>`.

Install
---------
Easy way: 
1) Download the repository.
2) Go to the root directory.
3) Install the required packages from [requirements.txt](https://github.com/TimkaMLG/StyleTransfer/blob/main/requirements.txt). This can be done by: 

`$ pip install -r requirements.txt`

If you have troubles with installation, then try installing without the cache directory: 

`$ pip install -r --no-cache-dir requirements.txt`

4) Run the bot using the: 

`$ python3 main.py`

Module installation:
-------------------

By file [setup.py](https://github.com/TimkaMLG/StyleTransfer/blob/main/setup.py) it is possible to build a package wheel, for this you should use:

`$ python3 setup.py sdist bdist_wheel`

Next, the assembled package will appear in the dist folder.

Docker installation:
--------------------

it is also possible to build a docker container using the Dockerfile:

`$ docker build -t python-docker-app .`

Deploy
---------
To deploy the Telegram bot, I used [VK Cloud](https://mcs.mail.ru/) service. Tested on a virtual machine with Ubuntu 22.04, 2 CPU cores and 4GB RAM. You can upload the application code there directly from github or from a local system using the [scp](https://en.wikipedia.org/wiki/Secure_copy_protocol) utility, install and run according to the instructions above.

Feedback
-----------
For questions related to the bot, you can contact me in my [telegram](https://t.me/TimkaMLG).
