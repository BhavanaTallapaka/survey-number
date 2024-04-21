{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMeB2+JCmpH6HbA8E+O6PZo",
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
        "<a href=\"https://colab.research.google.com/github/BhavanaTallapaka/survey-number/blob/main/survey_no.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "eZZvohxROOUa"
      },
      "outputs": [],
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "\n",
        "def get_survey_numbers(district_id, mandal_id, village_id):\n",
        "    base_url = \"https://dharani.telangana.gov.in/knowLandStatus\"\n",
        "    params = {\n",
        "        'districtID': district_id,\n",
        "        'mandalID': mandal_id,\n",
        "        'villageID': village_id\n",
        "    }\n",
        "    headers = {\n",
        "        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'\n",
        "    }\n",
        "\n",
        "    try:\n",
        "        response = requests.get(base_url, params=params, headers=headers, timeout=60)\n",
        "        if response.status_code == 200:\n",
        "            soup = BeautifulSoup(response.content, 'html.parser')\n",
        "            survey_select = soup.find('select', {'id': 'surveyIdselect'})\n",
        "            survey_numbers = []\n",
        "            if survey_select:\n",
        "                for option in survey_select.find_all('option'):\n",
        "                    value = option.get('value')\n",
        "                    if value != '0' and value:\n",
        "                        survey_numbers.append(value)\n",
        "            return survey_numbers\n",
        "        else:\n",
        "            print(f\"Failed to retrieve data. Status code: {response.status_code}\")\n",
        "            return []\n",
        "\n",
        "    except requests.exceptions.RequestException as e:\n",
        "        print(f\"Connection error: {e}\")\n",
        "        return []"
      ],
      "metadata": {
        "id": "qFJLELjBRNzb"
      },
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "district_id = \"3\"\n",
        "mandal_id = \"2\"\n",
        "village_id = \"23\""
      ],
      "metadata": {
        "id": "LEdoCPk92q82"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "survey_numbers = get_survey_numbers(district_id, mandal_id, village_id)"
      ],
      "metadata": {
        "id": "lsKQbaqc2w39"
      },
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Survey numbers for District: {district_id}, Mandal: {mandal_id}, Village: {village_id}:\")\n",
        "for survey_number in survey_numbers:\n",
        "    print(survey_number)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7vwLF0Ay21ko",
        "outputId": "070bb5bc-07b0-4a78-d188-da7987f56088"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Survey numbers for District: 3, Mandal: 2, Village: 23:\n"
          ]
        }
      ]
    }
  ]
}