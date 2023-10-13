import csv
from category import Category
from question import Question

def import_csv(filename: str) -> [Category]: # type: ignore
    """
    Imports questions and categories from a CSV file.
    Format: [question,answer,category], no whitespace, comma is separator.
    """
    categories_dict = {}
    with open(file=filename, newline='') as csvfile:
        csv_reader = csv.reader(csvfile,delimiter=',',quotechar="|")
        for item in csv_reader:
            it_question = Question(item[0],item[1])
            # it_category = Category(item[2])
            # it_category.add_question(it_question)
            if categories_dict.get(item[2]) is None:
                categories_dict[item[2]] = [it_question]
            else:
                categories_dict[item[2]].append(it_question)
        return [Category(category_name,questions) for category_name, questions in categories_dict.items()]