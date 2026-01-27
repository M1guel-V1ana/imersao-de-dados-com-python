{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyODZlv7eC+HnQmUr6kyjHnw",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/KevnNewEra/playing-with-numbers-in-python/blob/main/PlayingWithNumbers.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8BjStbG_068-",
        "outputId": "a04731bf-ab2f-4869-9e33-d312090b6f7f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-------------------------------\n",
            "WELCOME TO THE GAME\n",
            "-------------------------------\n",
            "are you ready to play? (y/n)\n",
            "y\n",
            "ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ ℔ ℕ № ℗ ℘ ℙ ℚ ℛ ℜ ℝ ℞ ℟(LOADING...) ℠ ℡ ™ ℣ ℤ ℥ Ω ℧ ℨ ℩ K Å ℬ ℭ ℮ ℯ ℰ ℱ Ⅎ ℳ ℴ ℵ\n",
            "say one number: \n",
            "1\n",
            "say another number: \n",
            "1\n",
            "you want some order? (+ , - , * , / )\n",
            "-\n",
            "the result is:  0\n",
            "tks!\n",
            "do you want to know something? (y/n)\n",
            "y\n",
            "sure??? (y/n)\n",
            "y\n",
            "Can I ask you a question? (y/n)\n",
            "n\n",
            "Ok, maybe next time.\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "\u001b[31mfollow me in instagram pleeease\u001b[0m: \u001b[32mnewkevn"
          ]
        }
      ],
      "source": [
        "print (\"-------------------------------\")\n",
        "print (\"WELCOME TO THE GAME\")\n",
        "print (\"-------------------------------\")\n",
        "print (\"are you ready to play? (y/n)\")\n",
        "answer = input()\n",
        "\n",
        "if answer == 'y':\n",
        "    texto = \"ℌ ℍ ℎ ℏ ℐ ℑ ℒ ℓ ℔ ℕ № ℗ ℘ ℙ ℚ ℛ ℜ ℝ ℞ ℟(LOADING...) ℠ ℡ ™ ℣ ℤ ℥ Ω ℧ ℨ ℩ K Å ℬ ℭ ℮ ℯ ℰ ℱ Ⅎ ℳ ℴ ℵ\"\n",
        "    import time\n",
        "    for letra in texto:\n",
        "        print(letra, end='', flush=True)\n",
        "        time.sleep(0.1)\n",
        "    print ()\n",
        "    print (\"say one number: \")\n",
        "    n1 = int(input())\n",
        "    print('say another number: ')\n",
        "    n2 = int(input())\n",
        "    print ('you want some order? (+ , - , * , / )')\n",
        "    op = input()\n",
        "\n",
        "    if op == '+':\n",
        "        s = n1 + n2\n",
        "    elif op == '-':\n",
        "        s = n1 - n2\n",
        "    elif op == '*':\n",
        "        s = n1 * n2\n",
        "    elif op == '/':\n",
        "        s = n1 / n2\n",
        "\n",
        "    print(\"the result is: \", s)\n",
        "    print ('tks!')\n",
        "\n",
        "    print ('do you want to know something? (y/n)')\n",
        "    answer2 = input()\n",
        "    if answer2 == 'y':\n",
        "        print('sure??? (y/n)')\n",
        "        answer3 = input()\n",
        "        if answer3 == 'y':\n",
        "            print (\"Can I ask you a question? (y/n)\")\n",
        "            answer4 = input()\n",
        "            if answer4 == 'y':\n",
        "                print (\"What is the meaning of life?\")\n",
        "                answer5 = input()\n",
        "                print (\"Interesting answer! But why?\")\n",
        "                reason = input()\n",
        "                print (\"Wow! I never thought about that.\")\n",
        "            else:\n",
        "                print (\"Ok, maybe next time.\")\n",
        "    print ()\n",
        "    print ()\n",
        "    print ()\n",
        "    print ()\n",
        "    texto = '\\033[31mfollow me in instagram pleeease\\033[0m: \\033[32mnewkevn'\n",
        "    import time\n",
        "    for letra in texto:\n",
        "            print(letra, end='', flush=True)\n",
        "            time.sleep(0.1)\n",
        "else:\n",
        "    print (\"ok, bye!\")\n",
        "\n",
        "\n",
        "# codigo criado apenas por diversão, não leve a sério :)\n",
        "#by kevn, iniciante em programação!\n",
        "# fiz em ingles pq as palavras sairam da mente em ingles kkkk\n",
        "# espero que gostem :D"
      ]
    }
  ]
}