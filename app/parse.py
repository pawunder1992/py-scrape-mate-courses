from dataclasses import dataclass


import requests
from bs4 import BeautifulSoup

BASE_URL = "https://mate.academy/"


@dataclass
class Course:
    name: str
    short_description: str
    duration: str


def get_single_course(course: Course) -> Course:
    return Course(
        name=course.select_one(".ProfessionCard_title__m7uno").text,
        short_description=course.select_one(
            ".ProfessionCard_description__K8weo"
        ).text,
        duration=course.select_one(".ProfessionCard_text___l0Du").text,
    )


def get_all_courses() -> list[Course]:

    html_content = requests.get(BASE_URL).content
    soup = BeautifulSoup(html_content, "html.parser")
    courses = soup.select(".ProfessionCard_content__mPiVi")
    return [get_single_course(course) for course in courses]
