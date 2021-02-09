{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "shell project",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyPmqLpleKvI63VSShZ1wlWe",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ddgatticus/Virtual_assistant/blob/Main/Chat_bot_incomplete.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8o8E9QpzeiBa"
      },
      "source": [
        "!pip install wolframalpha"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "R030PSacea9e"
      },
      "source": [
        "!pip install datetime"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ow7finf6eU6g"
      },
      "source": [
        "!pip install wikipedia"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7reDwEfEQTMM"
      },
      "source": [
        "from nltk.chat.util import Chat, reflections\r\n",
        "import wikipedia \r\n",
        "import datetime\r\n",
        "import random\r\n",
        "import wolframalpha"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cNOqKPfWQizt"
      },
      "source": [
        "answers = [\r\n",
        "    ['my name is (.*)', ['hi %1']],\r\n",
        "    ['(hi|hello|hey|ola)', ['hey', 'hey there', 'hi', 'hi there', 'hello']],\r\n",
        "    ['(.*) in (.*) is fun', ['%1 in %2 is indeed fun']],\r\n",
        "    ['(.*)(location|city) ?', 'Tokyo, Japan'],\r\n",
        "    ['(.*) created you?', ['Atticus Malley did using NLTK']],\r\n",
        "    ['how is the weather in (.*)', ['the weather in %1 is ok']],\r\n",
        "    ['(.*)help(.*)', ['I can help you']],\r\n",
        "    ['whats your name?', ['my name is PYTHANT_v.13']],\r\n",
        "    ['what is your name?', ['my name is PYTHANT_v.13']],\r\n",
        "    ['whats your name', ['my name is PYTHANT_v.13']],\r\n",
        "    ['what is your name', ['my name is PYTHANT_v.13']],\r\n",
        "    ['how old are you?', ['I am 3 weeks old']],\r\n",
        "    ['whats up', ['I am a computer, nothing can really be going on for me, besides that how are you?']]\r\n",
        "    ['I am good', ['Thats good to hear']],\r\n",
        "]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wzcA1TIKRqd5"
      },
      "source": [
        "reflections"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "WR3mT5Q5hhLS"
      },
      "source": [
        "howareyou = [\r\n",
        "        if \r\n",
        "]"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "A6te79iQYFIZ"
      },
      "source": [
        "my_dummy_reflecitons = {\r\n",
        "    'go' : 'gone',\r\n",
        "    'hello' : 'hey there'\r\n",
        "}"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 599
        },
        "id": "KJw4xef7Q4uy",
        "outputId": "1094eb6c-3e6c-4605-ddec-e12a2ef0974c"
      },
      "source": [
        "print('hello I am PYTHANT_v.13, you can ask me certain questions, my creator should have provided you with a list')\r\n",
        "chat = Chat(answers, reflections)\r\n",
        "#chat._substitute('go hello')\r\n",
        "chat.converse()"
      ],
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "hello I am PYTHANT_v.13, you can ask me certain questions, my creator should have provided you with a list\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    728\u001b[0m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 729\u001b[0;31m                 \u001b[0mident\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreply\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstdin_socket\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    730\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/jupyter_client/session.py\u001b[0m in \u001b[0;36mrecv\u001b[0;34m(self, socket, mode, content, copy)\u001b[0m\n\u001b[1;32m    802\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 803\u001b[0;31m             \u001b[0mmsg_list\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msocket\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv_multipart\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmode\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcopy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcopy\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    804\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mzmq\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mZMQError\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/zmq/sugar/socket.py\u001b[0m in \u001b[0;36mrecv_multipart\u001b[0;34m(self, flags, copy, track)\u001b[0m\n\u001b[1;32m    582\u001b[0m         \"\"\"\n\u001b[0;32m--> 583\u001b[0;31m         \u001b[0mparts\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mrecv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mflags\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcopy\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mcopy\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtrack\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mtrack\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    584\u001b[0m         \u001b[0;31m# have first part already, only loop while more to receive\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32mzmq/backend/cython/socket.pyx\u001b[0m in \u001b[0;36mzmq.backend.cython.socket.Socket.recv\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mzmq/backend/cython/socket.pyx\u001b[0m in \u001b[0;36mzmq.backend.cython.socket.Socket.recv\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32mzmq/backend/cython/socket.pyx\u001b[0m in \u001b[0;36mzmq.backend.cython.socket._recv_copy\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/zmq/backend/cython/checkrc.pxd\u001b[0m in \u001b[0;36mzmq.backend.cython.checkrc._check_rc\u001b[0;34m()\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: ",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-63-8027bb2acfd6>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mchat\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mChat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0manswers\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mreflections\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;31m#chat._substitute('go hello')\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mchat\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconverse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/nltk/chat/util.py\u001b[0m in \u001b[0;36mconverse\u001b[0;34m(self, quit)\u001b[0m\n\u001b[1;32m    115\u001b[0m         \u001b[0;32mwhile\u001b[0m \u001b[0muser_input\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mquit\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    116\u001b[0m             \u001b[0muser_input\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mquit\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 117\u001b[0;31m             \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0muser_input\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\">\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    118\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mEOFError\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    119\u001b[0m                 \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0muser_input\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    702\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    703\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 704\u001b[0;31m             \u001b[0mpassword\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    705\u001b[0m         )\n\u001b[1;32m    706\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.6/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    732\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    733\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 734\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    735\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    736\u001b[0m                 \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    }
  ]
}