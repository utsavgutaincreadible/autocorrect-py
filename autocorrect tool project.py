{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "# *BharatIntern - Task 1*"
      ],
      "metadata": {
        "id": "l8fQ5vs149gy"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Building an ***AUTO-CORRECTION*** tool using AI in Python"
      ],
      "metadata": {
        "id": "JWw3omb45KLa"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "id": "WSqUrs4U3Fje",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0c0ff9d4-4e0a-484c-b1c3-62b60878664d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: spello in /usr/local/lib/python3.10/dist-packages (1.3.0)\n",
            "Requirement already satisfied: nltk<4,>=3.4.5 in /usr/local/lib/python3.10/dist-packages (from spello) (3.8.1)\n",
            "Requirement already satisfied: click in /usr/local/lib/python3.10/dist-packages (from nltk<4,>=3.4.5->spello) (8.1.6)\n",
            "Requirement already satisfied: joblib in /usr/local/lib/python3.10/dist-packages (from nltk<4,>=3.4.5->spello) (1.3.1)\n",
            "Requirement already satisfied: regex>=2021.8.3 in /usr/local/lib/python3.10/dist-packages (from nltk<4,>=3.4.5->spello) (2022.10.31)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from nltk<4,>=3.4.5->spello) (4.65.0)\n"
          ]
        }
      ],
      "source": [
        "pip install spello"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from spello.model import SpellCorrectionModel"
      ],
      "metadata": {
        "id": "MUDc8kqM38NB"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sp = SpellCorrectionModel(language=\"en\")"
      ],
      "metadata": {
        "id": "soQZX_ld4JMo"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "with open (\"words.txt\") as file:\n",
        "    data = file.readlines()\n",
        "\n",
        "data = [i.strip() for i in data]"
      ],
      "metadata": {
        "id": "us14YvXb4JsU"
      },
      "execution_count": 22,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sp.train(data)"
      ],
      "metadata": {
        "id": "-10mSOUL4LIQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "833be858-ffe0-43f1-d75c-471ffbafd5e6"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Spello training started..\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:spello.settings:Spello training started..\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Context model training started ...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:spello.settings:Context model training started ...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Symspell training started ...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:spello.settings:Symspell training started ...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Phoneme training started ...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:spello.settings:Phoneme training started ...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Spello training completed successfully ...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:spello.settings:Spello training completed successfully ...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sp.save(\"\")"
      ],
      "metadata": {
        "id": "KHi5138i4dy6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "24d63bc0-8eeb-4c78-91e6-f3c89eeee42f"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'./model.pkl'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 24
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sp.load(\"model.pkl\")"
      ],
      "metadata": {
        "id": "rgw2Wewv4flp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "348e53db-8454-4385-cc8e-9860d1b4b794"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<spello.model.SpellCorrectionModel at 0x7d820801b280>"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sentence = input(\"Enter the sentence/word : \")"
      ],
      "metadata": {
        "id": "xX8XkfAc4hXV",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0ca2d333-a896-4854-d2b7-0b4c336d94d9"
      },
      "execution_count": 26,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter the sentence/word : Acheive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "words = sentence.split()"
      ],
      "metadata": {
        "id": "ZXMrfhER4i7H"
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "correct_words = []\n",
        "for word in words:\n",
        "    corrected = sp.spell_correct(word)\n",
        "    correct_words.append(corrected['spell_corrected_text'])\n",
        "\n",
        "corrected_sentence = \" \".join(correct_words)"
      ],
      "metadata": {
        "id": "-tbz8jMx4k3A",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "836e67ee-c8ea-44c2-e917-46368acd5daa"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "DEBUG:spello.settings:Symspell suggestions: [('achieve', 1), ('achieve', 1), ('achieve', 1)]\n",
            "DEBUG:spello.settings:Phoneme suggestions: [('achieve', 1), ('achieve', 1), ('achieve', 1), ('acer', 4), ('acre', 4), ('acre', 4)]\n",
            "DEBUG:spello.settings:Suggestions dict from phoneme and symspell are: {'acheive': ['achieve', 'acer', 'acre']}\n",
            "DEBUG:spello.settings:text after context model: achieve\n",
            "DEBUG:spello.settings:Spell-correction Results {'original_text': 'Acheive', 'spell_corrected_text': 'achieve', 'correction_dict': {'Acheive': 'achieve'}}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "corrected_sentence"
      ],
      "metadata": {
        "id": "Lphf8zKV4sL1",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "outputId": "9b25ec63-c68e-44d5-d75e-341b3b985f68"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'achieve'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    }
  ]
}
