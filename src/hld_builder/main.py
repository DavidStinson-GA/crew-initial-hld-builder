#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from hld_builder.crew import HldBuilder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'product_title': 'Modern Engineering Fundamentals',
        'client_name': '',
        'client_priorities': [
            'Retrain and upskill existing employees',
            'Move to the cloud',
            'Containerize new apps'
        ],
        'learner_persona': 'Junior developer, tech lead, or experienced coder',
        'learning_outcomes': [
            'Upskill existing coders to learn JavaScript',
            'Upskill existing coders to learn Node',
            'Upskill existing coders to learn Express'
            ],
        'business_goals': [
            'Reskill existing employees'
        ],
        'course_delivery_method': 'remote',
        'course_modality': 'online',
        'course_duration_h': '40',
        'current_year': str(datetime.now().year)
    }
    
    try:
        HldBuilder().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        HldBuilder().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        HldBuilder().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        HldBuilder().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
