import os
from pathlib import Path
from csv_import import import_csv
from category import Category
from question import Question

class Test_io(object):
    def test_import_of_dummy_csv(self):
        tests_directory = Path(os.getcwd())
        path_to_csv_data = Path.joinpath(tests_directory.parent, "questions.csv")
        categories = import_csv(str(path_to_csv_data))
        assert categories == self.mock_data()

    @property
    def mock_data(self) -> [Category]:
        scads = Category(title="ScaDS")
        question1 = Question(title="When was ScaDS founded?", answer="2014")
        question2 = Question(title="How many employees does ScaDS have?", answer="250")
        question3 = Question(title="When did the last summer school take place?", answer="July")
        scads.add_questions([question1, question2, question3])

        seminar_trip = Category(title="Seminar Trip")
        question4 = Question(title="Who organizes the pub quiz?", answer="Anne and ...")
        question5 = Question(title="Where does the seminar trip go?", answer="Cottbus")
        question6 = Question(title="How many people are we at the trip?", answer="45")
        seminar_trip.add_questions([question4, question5, question6])
        return [scads, seminar_trip]