##   ---------------------------------------  ##
##    The Impact of Test Anxiety on GAI Use   ##
##         Among University Students          ##
##                                            ##
##        Written in PyCharm 2026.2.4         ##
##            Using PsychoPy 2026.2.4         ##
##            Running on Python 3.11.9        ##
##                                            ##
##        Authored by Lisander Viaene, BSc    ##
##              Under supervision of          ##
##        Prof. Stijn Schelfhout, PhD, MSc    ##
##                                            ##
##  Research Project Experimental Psychology  ##
##              Ghent University              ##
##          Academic year 2026-2027           ##
##   ---------------------------------------  ##

# Import all relevant packages
import os
import time
import numpy as np
import pandas as pd
from psychopy import visual, event, core, gui, data

### Data file management
# Set working directory to save participant data to same location as experiment script
my_directory = os.getcwd() + "\\"

# GUI, gathers participant number, gender and age
info = {"Participant number": str(), "Gender": ('Female', 'Male', 'Other', 'Prefer not to say'), "Age": str()}

file_name = ""

already_exists = True

while already_exists:
    myDlg = gui.DlgFromDict(dictionary=info, sortKeys=True)
    folder = "ParticipantData"
    file_name = folder + "\\ParticipantData_id" + str(info["Participant number"])
    if not myDlg.OK:
        print("User pressed cancel, experiment will shut down")
        core.quit()
    if not os.path.isfile(my_directory + file_name + ".csv"):
        already_exists = False
    else:
        myDlg = gui.Dlg(title="Error")
        myDlg.addText("Try another participant number")
        myDlg.show()

# Initiate the experiment handler, this tracks and adds data to
thisExp = data.ExperimentHandler(dataFileName=f"{my_directory + file_name}", extraInfo=info)

### Stimuli creation
# General stimuli
win = visual.Window(size=(800, 600), units="norm", fullscr=True)

my_clock = core.Clock()

key_list = ['space', 'escape']

font = "Arial"

continue_text = "Press the space bar to continue"

text_screen = visual.TextStim(win, text="", font=font, alignText="left")

countdown_timer = visual.TextStim(win, text="", font=font, height=0.4)

break_screen = visual.TextStim(win, text="You can now take a short break before moving on to the questionnaire.\n\n"
                                         "To end your break, press the space bar.", font=font, alignText="left")

# Cognitive Test Anxiety Scale Revised (CTAR) stimuli setup
questionnaires_intro = visual.TextStim(win, text=("In the next part of the experiment you will complete some short "
                                                  "questionnaires.\n"
                                                  "You will first be shown a brief explanation of the questionnaire."
                                                  "\n\n"
                                                  + continue_text), font=font, alignText="left")

CTAR_explanation = visual.TextStim(win, text=("For every statement you see, please indicate how "
                                              "typical it is for you."
                                              "To choose an option, you must click on the corresponding option to "
                                              "register your answer. Be careful, once you select an answer you cannot "
                                              "go back and change it. \n\n"
                                              + "Press the space bar to start the questionnaire"), font=font,
                                   alignText="left")

CTAR_item = visual.TextStim(win=win, pos=(0, 0.25), text="", font=font)

CTAR_question = visual.TextStim(win=win, pos=(0, -0.15), text="How typical is this for you?", font=font)

CTAR_slider = visual.Slider(win=win, pos=(0, -0.35), style="radio", labels=[
    "Not at all", "Somewhat", "Quite", "Very"
], ticks=[1, 2, 3, 4], units="norm", font=font)

CTAR_response_options = {"Not at all": 0, "Somewhat": 1, "Quite": 2, "Very": 3}

CTAR_item_list = [
    "I lose sleep over worrying about examinations.",
    "While taking an important examination, I find myself wondering whether the other students are doing better than "
    "I am.",
    "I tend to freeze up on things like intelligence tests and final exams.",
    "During tests, I find myself thinking of the consequences of failing.",
    "At the beginning of a test, I am so nervous that I often can't think straight.",
    "My mind goes blank when I am pressured for an answer on a test.",
    "During tests, the thought frequently occurs to me that I may not be too bright.",
    "During a course examination, I get so nervous that I forget facts I really know.",
    "After taking a test, I feel I should have done better than I actually did.",
    # "I worry more about doing well on tests than I should.",
    "During tests, I have the feeling that I am not doing well.",
    "When I take a test that is difficult, I feel defeated before I even start.",
    "I am a poor test taker in the sense that my performance on a test does not show how much I really know about a "
    "topic.",
    "I am not good at taking tests.",
    # "I do not perform well on tests.",
    "When I first get my copy of a test, it takes me a while to calm down to the point where I can begin to think "
    "straight.",
    "When I take a test, my nervousness causes me to make careless errors.",
    ### Eliminated 2 items above because they're similar

    # "I get distracted from studying for tests by thoughts of failing.",
    # "I have difficulty remembering what I studied for tests.",
    # "While preparing for a test, I often think that I am likely to fail.",
    # "My test performances make me believe that I am not a good student.",
    # "I often realize mistakes I made right after turning in a test.",
    # "When I finish a hard test, I am afraid to see the score.",
    # "When I get a good grade on a test, it is usually because I got lucky.",
    # "I don't seem to have much control over my test scores.",

    ### eliminated 8 items due to https://doi.org/10.1080/10627197.2014.934604
]

GAIUS_explanation = visual.TextStim(win, text=("The second and last questionnaire consists of 5 statements. "
                                               "After reading a statement, you must indicate how much you disagree or "
                                               "agree with the statement."
                                               "To choose an option, you must click on the corresponding option to "
                                               "register your answer. Be careful, once you select an answer you "
                                               "cannot go back and change it. You can choose between the following "
                                               "four options: \n"
                                               "'Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly "
                                               "agree'\n\n"
                                               + "Press the space bar to start the questionnaire"), font=font,
                                    alignText="left")

GAIUS_item = visual.TextStim(win=win, pos=(0, 0.25), text="", font=font)
GAIUS_question = visual.TextStim(win=win, pos=(0, -0.15), text="Do you agree with this statement?", font=font)
GAIUS_slider = visual.Slider(win=win, pos=(0, -0.35), style="radio", labels=[
    "Strongly  disagree", "Disagree ", "Neutral", "Agree", "Strongly  agree"
], ticks=[1, 2, 3, 4, 5], units="norm", font=font)

GAIUS_response_options = {"Strongly  disagree": -2, "Disagree ": -1, "Neutral": 0, "Agree": 1, "Strongly  agree": 2}

GAIUS_item_list = [
    "GenAI tools (e.g. ChatGPT) should be integrated into the classroom.",
    "GenAI tools (e.g. ChatGPT) can help me save time.",
    "GenAI tools (e.g. ChatGPT) can provide me with new ideas that I may not have thought of myself.",
    "GenAI tools (e.g. ChatGPT) can provide me with feed-back on my assignments.",
    "I use GenAI tools (e.g. ChatGPT) because it can provide academic support services (e.g. answer my questions, "
    "summarise readings, etc.)",

    # "Students must learn how to use GenAI tools well for their careers.",
    # "GenAI tools (e.g. ChatGPT) can improve my digital competence.",
    # "I use GenAI tools (e.g. ChatGPT) because it is available and accessible 24/7.",
    # "I use GenAI tools (e.g. ChatGPT) for my assignments because it is anonymous.",
    # "I use GenAI tools because it provides accurate and reliable information.",
    # "I use GenAI tools (e.g. ChatGPT) for my assignments to improve my English grammar and spelling.",
    # "I use GenAI tools (e.g. ChatGPT) in writing tasks.",
    # "I use GenAI tools (e.g. ChatGPT) in my verbal contribution in the class.",
    # "I submit a full paper generated by GenAI tools (e.g. ChatGPT) as my own work.",
    # "I paraphrase and edit a work generated by GenAI tools (e.g. ChatGPT) and submit it as my own work.",
    # "I cite information generated by GenAI tools (e.g. ChatGPT) in my work.",
    # "GenAI tools (e.g. ChatGPT) encourage and facilitate academic misconduct.",
    # "I use GenAI tools (e.g. ChatGPT) in class activities without the instructor’s permission.",
    # "I use GenAI tools (e.g. ChatGPT) for class activities without acknowledging the help of the GenAI tools.",
]

# https://doi.org/10.1080/14703297.2025.2603622

# Test phase setup

test_intro = visual.TextStim(win, text=(
        f"You will now complete the multiple choice exam based on the texts you studied. There are 20 questions "
        f"in total. For each question, you will get the opportunity to use AI to help you solve the question. "
        f"However, please be aware that the AI can make mistakes.\n"
        f"Before the exam starts, an example question will be shown so you can try asking the AI for help.\n"
        + continue_text), font=font, alignText="left")

test_practice = visual.TextStim(win, text=f"", font=font, alignText="left")

test_question = visual.TextStim(win=win, pos=(0, 0.50), text="", font=font)

test_label_A = visual.TextStim(win=win, pos=(-0.75, 0.15), height=0.10, text="A", font=font)
test_label_B = visual.TextStim(win=win, pos=(-0.25, 0.15), height=0.10, text="B", font=font)
test_label_C = visual.TextStim(win=win, pos=(0.25, 0.15), height=0.10, text="C", font=font)
test_label_D = visual.TextStim(win=win, pos=(0.75, 0.15), height=0.10, text="D", font=font)

test_halfway_break = visual.TextStim(win=win, font=font)

test_answers = visual.TextStim(win=win, pos=(-0.25, -0.75), height=0.065, text="", font=font)

ai_slider = visual.Slider(win=win, pos=(0, 0), style="radio",
                          labels=["Yes", "No"],
                          ticks=[1, 2], units="norm", font=font, labelHeight=0.085, labelWrapWidth=0.45,
                          size=(0.52, 0.15))

yes_ai_use = visual.TextStim(win=win, pos=(0, -0.75), height=0.065, text="", font=font)

questions = [['What brain regions were primarily involved in decision-making?'],
             ['What is the "framing effect"?'],
             ["How did cognitive effort differ when participants made gain-related decisions?"],
             ['What theoretical explanation does the paper propose for the framing effect?'],
             ['What does the theory of self efficacy primarily aim to explain?'],
             ['What determines whether a person will initiate coping behavior?'],
             ['Which of the following is NOT one of the four principal sources of self-efficacy?'],
             ['What is the effect of persisting in activities that are subjectively threatening but actually safe?'],
             ['What are the three components of adaptability in the EEG study on decision making?'],
             ['What main concept is studied in relation to decision making in the EEG study?'],
             ['What did the EEG findings suggest about theta power during the task performed by professionals?'],
             ['What did the decrease in alpha activity in frontal regions compared to temporoparietal regions indicate?'],
             ['What type of component, in addition to general information processing, contributes to g estimates?'],
             ['Does using elementary cognitive tasks (ECTs) significantly change the predictive power of g for '
              'scholastic performance?'],
             ['What was the nature of the additional processing component found to contribute to g estimates?'],
             ['What conclusion was drawn about defining g with elementary cognitive tasks (ECTs) alongside '
              'traditional psychometric tasks?'],
             ['What type of treatment produced the largest effect sizes for specific phobia?'],
             ['Were placebo treatments more effective than no treatments for specific phobia?'],
             ['Which statement best describes the effectiveness of in vivo exposure compared to other exposure methods?'],
             ['What did the meta-analysis find regarding the influence of phobia type on treatment outcomes?']]

correct_answers = [['Prefrontal and parietal cortices'],
                   ['People make different decisions depending on whether options are framed as gains or losses'],
                   ['Choosing a sure gain required less cognitive effort than choosing a risky gain'],
                   ['Individuals seek to make good decisions while minimizing cognitive effort'],
                   ['How psychological changes occur through different treatments'],
                   ['Expectations of personal efficacy'],
                   ['Social comparison'],
                   ['Enhancement of self-efficacy through mastery experiences'],
                   ['Flexibility, proactivity, innovativeness'],
                   ['Adaptability'],
                   ['It increased in the right hemisphere, indicating creative processing'],
                   ['Sustained engagement and higher cognitive load'],
                   ['Memory processing component'],
                   ['No'],
                   ['Nonchronometric and memory-based'],
                   ['It does not significantly alter the axis of g relative to scholastic performance'],
                   ['Exposure-based treatment'],
                   ['Yes'],
                   ['In vivo exposure outperformed other methods at post-treatment but not at follow-up'],
                   ['Treatment effectiveness was not moderated by type of specific phobia']]

incorrect_column_1 = [['Occipital and temporal cortices'],
                      ['People make identical decisions regardless of how options are described'],
                      ['Choosing a risky gain required less cognitive effort than choosing a sure gain'],
                      ['Emotional responses completely override cognitive processing'],
                      ['How biological changes affect behavior'],
                      ['External rewards'],
                      ['Vicarious experience'],
                      ['Increased anxiety and reduced motivation'],
                      ['Intelligence, memory, attention'],
                      ['Memory capacity'],
                      ['It decreased equally in both hemispheres'],
                      ['Reduced cognitive engagement during the task'],
                      ['Emotional processing component'],
                      ['Yes'],
                      ['Chronometric and perception-based'],
                      ['It shifts the axis of g significantly in factorial space'],
                      ['No treatment'],
                      ['No'],
                      ['In vivo exposure was less effective than imaginal exposure at all times'],
                      ['Only animal phobias showed improvement']]

incorrect_column_2 = [[''],
                      [''],
                      ['Both risky and sure gains required equal cognitive effort'],
                      ['Individuals aim to maximize outcomes without regard to effort'],
                      [''],
                      [''],
                      ['Performance accomplishments'],
                      ['Decrease in physiological arousal only'],
                      [''],
                      [''],
                      ['It increased in the left hemisphere only'],
                      ['Increased emotional stress only'],
                      [''],
                      [''],
                      ['Language-specific and social'],
                      ['It weakens the relationship between g and scholastic performance'],
                      [''],
                      [''],
                      ['In vivo exposure had no significant effect compared to virtual reality'],
                      ['Treatment outcomes were strongly dependent on phobia type']]

incorrect_column_3 = [[''],
                      [''],
                      ['Cognitive effort was only measured for loss-related decisions'],
                      ['Decisions are made randomly when uncertainty is high'],
                      [''],
                      [''],
                      ['Physiological states'],
                      ['Elimination of all defensive behaviors immediately'],
                      [''],
                      [''],
                      ['It showed no significant change across regions'],
                      ['Lack of involvement in decision-making'],
                      [''],
                      [''],
                      ['Motor-based and time-dependent'],
                      ['It eliminates the need for traditional psychometric measures'],
                      [''],
                      [''],
                      ['In vivo exposure was only effective in single-session treatments'],
                      ['Certain phobia types responded significantly better than others']]

difficulty = np.array(
    [["easy"], ["easy"], ["hard"], ["hard"], ["easy"], ["easy"], ["hard"], ["hard"], ["easy"], ["easy"], ["hard"],
     ["hard"], ["easy"], ["easy"], ["hard"], ["hard"], ["easy"], ["easy"], ["hard"], ["hard"], ],
    dtype=np.dtypes.StringDType)

ai_correctness = np.array([
    ["correct"],
    ["correct"],
    ["correct"],
    ["correct"],
    ["correct"],
    ["incorrect"],
    ["incorrect"],
    ["incorrect"],
    ["incorrect"],
    ["incorrect"],
])

rng = np.random.default_rng()

n_test_items = len(questions)

test_score = int()

indexes = np.array([[f"{x}"] for x in range(20)])
exp_indexes = indexes
text_id = [[0], [0], [0], [0], [1], [1], [1], [1], [2], [2], [2], [2], [3], [3], [3], [3], [4], [4], [4], [4]]
text_id = np.array(text_id, dtype=np.dtypes.StringDType)
questions = np.array(questions, dtype=np.dtypes.StringDType)
correct_answers = np.array(correct_answers, dtype=np.dtypes.StringDType)
incorrect_column_1 = np.array(incorrect_column_1, dtype=np.dtypes.StringDType)
incorrect_column_2 = np.array(incorrect_column_2, dtype=np.dtypes.StringDType)
incorrect_column_3 = np.array(incorrect_column_3, dtype=np.dtypes.StringDType)

answers = np.column_stack([correct_answers, incorrect_column_1, incorrect_column_2, incorrect_column_3])

for idx in range(20):
    rng.shuffle(answers[idx], axis=0)

rng.shuffle(ai_correctness, axis=0)
ai_correctness_first_half = ai_correctness
rng.shuffle(ai_correctness, axis=0)
ai_correctness_second_half = ai_correctness

test_full = np.column_stack([text_id, indexes, questions, answers, correct_answers, difficulty])

test_first_half, test_second_half = test_full[0::2], test_full[1::2]

test_first_half = np.column_stack([test_first_half, ai_correctness_first_half])
test_second_half = np.column_stack([test_second_half, ai_correctness_second_half])
rng.shuffle(test_first_half, axis=0)
rng.shuffle(test_second_half, axis=0)

test_full = np.vstack([test_first_half, test_second_half])

test_full = np.column_stack([test_full, exp_indexes])

### Design matrix
design_matrix = test_full

trialsDF = pd.DataFrame.from_records(design_matrix)
trialsDF.columns = ["text_id", "indexes", "test_question", "test_answer_A", "test_answer_B", "test_answer_C",
                    "test_answer_D", "test_correct_answer", "test_difficulty", "ai_accuracy", "exp_indexes"]

trial_list = pd.DataFrame.to_dict(trialsDF, orient="records")

trials = data.TrialHandler(trial_list, nReps=1, method='sequential')

### Start of the experiment
# Introduction

total_time = core.Clock()
start_time = time.strftime("%H:%M:%S", time.localtime())

text_screen.text = (
        f"Hello and welcome to this experiment! Please read all instructions carefully. In this experiment, "
        f"you will study a few texts, complete a questionnaire, and then take part in an exam. You will get 20 "
        f"minutes to study.\n\n"
        + "Press the space bar to receive the next part of the instructions")
text_screen.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

text_screen.text = (
        f"During the exam, you will have the opportunity to use generative artificial intelligence (AI). For each "
        f"question, you can choose to solve the question with or without AI. While using AI could help you solve "
        f"the questions, please be aware that the AI can make mistakes. \n\n"
        + continue_text)
text_screen.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

text_screen.text = (f"If anything is unclear at this time or if you have questions at any point during the experiment,"
                    f" raise your hand and the researcher will come to you. If you would like to stop "
                    f"the experiment at any point, please let the researcher know.\n\n"
                    + continue_text)
text_screen.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

# Study phase start
text_screen.text = (f"In this part of the experiment, "
                    f"you will study the content of five scientific texts. "
                    "These texts are turned face down on your desk. Don't look at the texts yet. "
                    "On the next screen a timer will start. You will get 20 minutes to study "
                    "the texts. Afterwards, you are expected to complete a knowledge test "
                    "(multiple choice exam) on the content of these texts. Please turn over the texts after the timer "
                    "starts. You will be alerted when the timer runs out. \n\nPress the space bar to start the timer")
text_screen.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

minutes = 0
seconds = 3
duration = minutes * 60 + seconds
remaining_time = duration
flashes = 3

for _ in range(duration):
    countdown_timer.text = (f"{remaining_time // 60 if remaining_time // 60 >= 10 else f'0{remaining_time // 60}'}:"
                            f"{remaining_time % 60 if remaining_time % 60 >= 10 else f'0{remaining_time % 60}'}")
    countdown_timer.draw()
    win.flip()
    key_press = event.waitKeys(keyList="escape", maxWait=1)
    if key_press and key_press[0] == 'escape':
        win.close()
        core.quit()
    remaining_time -= 1

for _ in range(flashes):
    win.color = (1, -1, -1)
    win.flip()
    core.wait(0.5)
    win.color = (0, 0, 0)
    win.flip()
    core.wait(0.5)

text_screen.text = (
    "Please hand over your texts to the researcher. You can now take a short break before moving on to the next part "
    "of the experiment.\n\n"
    "To end your break, press the space bar.")
text_screen.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

questionnaires_intro.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

CTAR_explanation.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

idx = 0
total_score = 0
for item in CTAR_item_list:
    CTAR_item.text = item
    idx += 1
    CTAR_slider.reset()
    my_clock.reset()
    while not CTAR_slider.rating:  # this loop shows the slider until a response has been selected
        CTAR_item.draw()
        CTAR_question.draw()
        CTAR_slider.draw()
        win.flip()
    reaction_time = round(my_clock.getTime(), 3)  # round to 1 millisecond

    item_score = CTAR_response_options[CTAR_slider.rating]
    total_score += item_score
    thisExp.addData('CTAR_idx', idx)
    thisExp.addData('CTAR_item', item)
    thisExp.addData('CTAR_response', CTAR_slider.rating)
    thisExp.addData('CTAR_response_score', item_score)
    thisExp.addData('CTAR_total', total_score)
    thisExp.addData('CTAR_rt_s', reaction_time)
    thisExp.nextEntry()

text_screen.text = ("You can now take a short break before moving on to the next part of the experiment.\n\n"
                    "To end your break, press the space bar.")
text_screen.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

test_intro.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
if key_press[0] == 'escape':
    win.close()
    core.quit()

test_score = 0
score = 0
total_ai_use = 0
ai_use = 0
total_answer_rt = 0
total_ai_use_rt = 0
options = ["A", "B", "C", "D"]

answer_A, answer_B, answer_C, answer_D = "", "", "", ""
show_correct_idx = 0
number = 0

#
# test_question.text = (f"The next question should be 'hard' to solve. It contains 4 answer options.\n\n Do you want to use AI to solve "
#                           f"this question?")
# ai_slider.reset()
# my_clock.reset()
# while not ai_slider.rating:  # this loop shows the slider until a response has been selected
#     test_question.draw()
#     ai_slider.draw()
#     win.flip()
# ai_use_rt = round(my_clock.getTime(), 3)  # round to 1 millisecond
#
# ai_use = 1 if ai_slider.rating == 'Yes' else 0
#
# test_question.text = 'test_question'
#
# if trial["test_difficulty"] == "easy":
#     answers = [trial["test_answer_A"], trial["test_answer_B"], trial["test_answer_C"], trial["test_answer_D"]]
#     answer_A, answer_B, answer_C, answer_D = "", "", "", ""
#     while not answer_A:
#         answer_A = answers.pop(0)
#     while not answer_B:
#         answer_B = answers.pop(0)
#     test_slider = visual.Slider(win=win, pos=(0, 0), style="radio",
#                                     labels=[answer_A, answer_B],
#                                     ticks=[1, 2], units="norm", font=font, labelHeight=0.085, labelWrapWidth=0.45,
#                                     size=(0.52, 0.15))
#
#     answers = [answer_A, answer_B]
#
#     yes_ai_use.text = f"AI says the correct answer is: {trial['test_correct_answer']}"
#     my_clock.reset()
#     while not test_slider.rating:  # this loop shows the slider until a response has been selected
#         test_question.draw()
#         test_slider.draw()
#         if ai_use:
#             yes_ai_use.draw()
#         win.flip()


# Give feedback after 10 questions of the test
#show score gathered from the first 10 questions

counter = 0
numbers_incorrect = []
for trial in trials:
    if int(trial["exp_indexes"]) < 10:
        test_half = "first_half"
    else:
        test_half = "second_half"
    if test_half == "second_half" and counter == 0:
        test_halfway_break.text = (f"This is the halfway point of the test. \nSo far, your score is "
                                   f"{test_score}/{int(trial['exp_indexes'])}. \nYou used GAI {total_ai_use} times. "
                                   f"\n\n") + continue_text
        test_halfway_break.draw()
        win.flip()
        key_press = event.waitKeys(keyList=key_list)
        if key_press[0] == 'escape':
            win.close()
            core.quit()
        thisExp.addData("break_screen", "yes")
        counter += 1

    # Show test question, then ask if they want to use AI
    test_question.text = (f"The next question should be '{trial['test_difficulty']}' to solve. It contains "
                          f"{2 if trial['test_difficulty'] == 'easy' else 4} answer options.\n\n "
                          f"Do you want to use AI to solve this question?")
    ai_slider.reset()
    my_clock.reset()
    while not ai_slider.rating:  # this loop shows the slider until a response has been selected
        test_question.draw()
        ai_slider.draw()
        win.flip()
    ai_use_rt = round(my_clock.getTime(), 3)  # round to 1 millisecond

    ai_use = 1 if ai_slider.rating == 'Yes' else 0

    test_question.text = trial['test_question']

    if trial["test_difficulty"] == "easy":
        answers = [trial["test_answer_A"], trial["test_answer_B"], trial["test_answer_C"], trial["test_answer_D"]]
        answer_A, answer_B, answer_C, answer_D = "", "", "", ""
        while not answer_A:
            answer_A = answers.pop(0)
        while not answer_B:
            answer_B = answers.pop(0)
        test_slider = visual.Slider(win=win, pos=(0, 0), style="radio",
                                    labels=[answer_A, answer_B],
                                    ticks=[1, 2], units="norm", font=font, labelHeight=0.085, labelWrapWidth=0.45,
                                    size=(0.52, 0.15))

        answers = [answer_A, answer_B]
        correct_answer_easy = trial['test_correct_answer']
        incorrect_answer_easy = answers[0] if answers[0] != correct_answer_easy else answers[1]

        yes_ai_use.text = (f"AI says the correct answer is: "
                           f"{correct_answer_easy if trial['ai_accuracy'] == 'correct' else incorrect_answer_easy}")
        my_clock.reset()
        while not test_slider.rating:  # this loop shows the slider until a response has been selected
            test_question.draw()
            test_slider.draw()
            if ai_use:
                yes_ai_use.draw()
            win.flip()
        reaction_time = round(my_clock.getTime(), 3)  # round to 1 millisecond

        score = 1 if test_slider.rating == trial["test_correct_answer"] else 0
        correct_answer = options[answers.index(trial["test_correct_answer"])]
        chosen_answer = options[answers.index(test_slider.rating)]

    else:
        answers = [trial["test_answer_A"], trial["test_answer_B"], trial["test_answer_C"], trial["test_answer_D"]]
        answer_A, answer_B, answer_C, answer_D = answers[0], answers[1], answers[2], answers[3]
        correct_answer = trial["test_correct_answer"]

        show_correct_idx = answers.index(correct_answer)
        incorrect_answer = correct_answer
        while incorrect_answer == correct_answer:
            number = np.random.randint(0, 3)
            incorrect_answer = answers[number]
        numbers = [show_correct_idx, number]

        incorrect_answer_second = incorrect_answer
        while incorrect_answer_second == incorrect_answer or incorrect_answer_second == correct_answer:
            number = np.random.randint(0, 3)
            incorrect_answer_second = answers[number]

        numbers_incorrect = [numbers[1], number]

        numbers.sort()
        numbers_incorrect.sort()

        test_slider = visual.Slider(win=win, pos=(0, 0), style="radio",
                                    labels=[answer_A, answer_B, answer_C, answer_D],
                                    ticks=[1, 2, 3, 4], units="norm", font=font, labelHeight=0.085, labelWrapWidth=0.45,
                                    size=(1.5, 0.15))
        if trial["ai_accuracy"] == "correct":
            yes_ai_use.text = f"AI says the correct answer is: either {options[numbers[0]]} or {options[numbers[1]]}"
        else:
            yes_ai_use.text = (f"AI says the correct answer is: either {options[numbers_incorrect[0]]} or"
                               f" {options[numbers_incorrect[1]]}")

        my_clock.reset()
        while not test_slider.rating:  # this loop shows the slider until a response has been selected
            test_label_A.draw()
            test_label_B.draw()
            test_label_C.draw()
            test_label_D.draw()
            test_question.draw()
            test_slider.draw()
            if ai_use:
                yes_ai_use.draw()
            win.flip()
        reaction_time = round(my_clock.getTime(), 3)  # round to 1 millisecond

        score = 1 if test_slider.rating == trial["test_correct_answer"] else 0
        correct_answer = options[answers.index(trial["test_correct_answer"])]
        chosen_answer = options[answers.index(test_slider.rating)]

    test_score += score
    total_ai_use += ai_use
    total_answer_rt += reaction_time
    total_ai_use_rt += ai_use_rt

    thisExp.addData("text_index", trial["text_id"])
    thisExp.addData("test_half", test_half)
    thisExp.addData("question_index", trial["indexes"])
    thisExp.addData("thisexp_question_index", trial["exp_indexes"])
    thisExp.addData("question", trial["test_question"])
    thisExp.addData("answer_A", answer_A)
    thisExp.addData("answer_B", answer_B)
    thisExp.addData("answer_C", answer_C)
    thisExp.addData("answer_D", answer_D)
    thisExp.addData("difficulty", trial["test_difficulty"])
    thisExp.addData("correct_letter", correct_answer)
    thisExp.addData("chosen_letter", chosen_answer)
    thisExp.addData('rt_answer', reaction_time)
    thisExp.addData("rt_total_answer", round(total_answer_rt, 3))
    thisExp.addData("correct_answer", trial["test_correct_answer"])
    thisExp.addData("chosen_answer", test_slider.rating)
    thisExp.addData("accuracy", score)
    thisExp.addData("total_score", test_score)
    thisExp.addData("ai_use", ai_use)
    thisExp.addData("total_ai_use", total_ai_use)
    thisExp.addData('rt_ai_use', ai_use_rt)
    thisExp.addData('rt_total_ai_use', round(total_ai_use_rt, 3))

    thisExp.addData("ai_accuracy", trial["ai_accuracy"])
    if ai_use:
        if trial["test_difficulty"] == "hard":
            if trial["ai_accuracy"] == "correct":
                thisExp.addData("correct_shown_ai", options[show_correct_idx])
                thisExp.addData("incorrect_shown_ai", options[number])
            else:
                thisExp.addData("correct_shown_ai", "None")
                thisExp.addData("incorrect_shown_ai", f"{options[numbers_incorrect[0]]} & "
                                                      f"{options[numbers_incorrect[1]]}")

        else:
            if trial["ai_accuracy"] == "correct":
                thisExp.addData("correct_shown_ai", options[0 if trial['test_correct_answer'] == answer_A else 1])
                thisExp.addData("incorrect_shown_ai", "None")
            else:
                thisExp.addData("correct_shown_ai", "None")
                thisExp.addData("incorrect_shown_ai",
                                options[0 if trial['test_correct_answer'] != answer_A else 1])
    else:
        thisExp.addData("correct_shown_ai", "None")
        thisExp.addData("incorrect_shown_ai", "None")

    key_press = event.getKeys(keyList=key_list)
    if key_press and key_press[0] == 'escape':
        break
    thisExp.nextEntry()

total_time = round(total_time.getTime(), 3)  # round to 1 millisecond
thisExp.addData("date", time.strftime("%Y_%m_%d", time.localtime()))
thisExp.addData("start_time", start_time)
thisExp.addData("end_time", time.strftime("%H:%M:%S", time.localtime()))
thisExp.addData("total_time_s", total_time)

text_screen.text = ("This is the end of the experiment.\n\n"
                    f"Your final score is {test_score}/20. \nYou used GAI {total_ai_use} times. \n\n"
                    "Signal to the experimenter that you have completed the test.\n\n"
                    "Thank you very much for your participation!\n\n")
text_screen.draw()
win.flip()
key_press = event.waitKeys(keyList=key_list)
win.close()
core.quit()
