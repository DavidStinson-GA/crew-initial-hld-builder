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

    # Inputs gathered from:
    # https://docs.google.com/presentation/d/1rVhaBA8aGMDBL7h2xpniqiv_bwVCmri9/edit

    inputs = {
        'product_title': 'UX for Engineers',
        'client_name': 'M&T Bank',
        'course_delivery_method': 'Instructor-led',
        'course_delivery_modality': 'remote',
        'course_duration_h': 30,
        'course_description': 'This course equips developers with practical UX skills through hands-on exercises with real-world applications. With a strong focus on collaboration, participants will improve communication with UX teams and gain actionable strategies they can use right away.',
        'course_business_outcomes': [
            'Expand the mindset and steps in UX process to entire tech team include low and high fidelity technical design skills and UX research methodologies.',
            'Making developers more self-reliant; speeding up design and development collaboration and process.'
        ],
        'client_priorities': [
            'The course should provide an understanding of baseline research techniques, methodologies and best practices for better cross-discipline collaboration.',
            'Engineers should be able to use tools like Miro to wireframe and communicate ideas and collaborate with the broader team.',
            'Understanding the end-to-end design process will help engineers incorporate UX concepts and approaches into in their decision making and workflow.',
            'Exposure and practice with collaborative tools like the Currency Design System can improve efficiency, velocity and reinforce cohesive product design.'
        ],
        'primary_persona_job_role': 'Software Engineer',
        'learner_persona_description': 'A software engineer with 3+ years of experience in software development, specializing in building web applications using modern JavaScript frameworks and libraries.',
        'learner_persona_attributes_and_background': [
            'Strong foundation in JavaScript, React, and Node.js',
            'Experience building web applications',
            'Familiar with modern web development practices and tools',
            'Strong interest in learning new technologies and approaches'
        ],
        'learner_persona_existing_knowledge': [
            'Familiar with implementing UI designs using HTML and CSS',
        ],
        'course_learning_outcomes': [
            'Create polished, professional, and complete designs; and articulate design decisions made to peers and other UX professionals.',
            'Utilize foundational visual design techniques to enhance the overall design of digital products.'
            'Design product interactions with easy-to-use navigation that are logically structured using information architecture methodologies.',
            'Collaborate with a team of fellow designers to solve real-world design challenges using advanced technical design skills.',
            'Evaluate business requirements, metrics, key stakeholders, and technical constraints; and employ product management techniques to design products.'
        ],
        'course_software_and_tools': [
            'Slack',
            'Zoom',
            'Visual Studio Code',
            'Miro',
            'Currency Design System',
        ]
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
