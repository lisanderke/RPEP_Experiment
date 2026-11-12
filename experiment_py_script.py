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

## README ##
# variable names should follow the naming convention: category_subcategory_identifier
# example: stim_text_countdown_timer
# to indicate the stimulus (stim) category, the TextStim (text) subcategory, and the identifier (countdown_timer)
# Some special variables do not follow the naming convention

# Import all relevant packages
import os
import time
import numpy as np
import pandas as pd
from psychopy import visual, event, core, gui, data

## Data file management
# Set working directory to save participant data to same location as experiment script
str_working_directory   = os.getcwd() + "\\"

# GUI, gathers participant number, gender and age -> will ask new participant number if number already in use
dict_gui_info           = {"Participant number": str(),
                           "Gender": ('Female', 'Male', 'Other', 'Prefer not to say'),
                           "Age": str()
                           }
str_file_name           = ""
bool_file_name          = True

while bool_file_name:
    myDlg               = gui.DlgFromDict(dictionary=dict_gui_info, sortKeys=True)
    folder              = "ParticipantData"
    str_file_name       = folder + "\\ParticipantData_id" + str(dict_gui_info["Participant number"])
    if not myDlg.OK:
        print("User pressed cancel, experiment will shut down")
        core.quit()
    if not os.path.isfile(str_working_directory + str_file_name + ".csv"):
        bool_file_name  = False
    else:
        myDlg           = gui.Dlg(title="Error")
        myDlg.addText("Try another participant number")
        myDlg.show()

# Initiate the experiment handler, this tracks and adds data to
experiment_handler      = data.ExperimentHandler(dataFileName=f"{str_working_directory + str_file_name}",
                                                 extraInfo=dict_gui_info)

## Stimuli creation
# General stimuli
win                     = visual.Window(size=(1920, 1080), units="norm", fullscr=True)

my_clock                = core.Clock()

list_allowed_keys       = ['space', 'escape']

str_font                = "Arial"

str_continue            = "Press the space bar to continue"

stim_text_info          = visual.TextStim(win,
                                          font=str_font,
                                          alignText="left"
                                          )

stim_text_space_bar     = visual.TextStim(win,
                                          text="Press the space bar to continue",
                                          font=str_font,
                                          pos=(0, -0.75),
                                          )

stim_text_study_timer   = visual.TextStim(win,
                                          font=str_font,
                                          height=0.4
                                          )

stim_text_survey_prompt = visual.TextStim(win,
                                          font=str_font,
                                          pos=(0, -0.15),
                                          text="Do you agree with this statement?"
                                          )

stim_text_survey_item   = visual.TextStim(win,
                                          font=str_font,
                                          pos=(0, 0.25)
                                          )

stim_slider_survey      = visual.Slider(win,
                                        font=str_font,
                                        pos=(0, -0.35),
                                        style="radio",
                                        labels=["Strongly  disagree", "Disagree", "Neutral", "Agree",
                                                "Strongly  agree"],
                                        ticks=[1, 2, 3, 4, 5]
                                        )

dict_survey_items       = {"ctar_01": "I lose sleep over worrying about exams.",
                           "ctar_02": "While taking an important exam, I find myself wondering whether the other "
                                      "students are doing better than I am.",
                           "ctar_03": "During tests, I find myself thinking of the consequences of failing.",
                           "ctar_04": "At the beginning of a test, I am so nervous that I often can't think straight.",
                           "ctar_05": "My mind goes blank when I am pressured for an answer on a test.",
                           "ctar_06": "During a course exam, I get so nervous that I forget facts I really know.",
                           "ctar_07": "After taking a test, I feel I should have done better than I actually did.",
                           "ctar_08": "I am a poor test taker in the sense that my performance on a test does not "
                                      "show how much I really know about a topic.",
                           "ctar_09": "When I first get my copy of a test, it takes me a while to calm down to the "
                                      "point where I can begin to think straight.",
                           "ctar_10": "When I take a test, my nervousness causes me to make careless errors.",

                           "ai_use_01": "I use GenAI tools (e.g. ChatGPT) because it provides accurate and reliable "
                                        "information.",
                           "ai_use_02": "I use GenAI tools in writing tasks.",
                           "ai_use_03": "I use GenAI tools in my verbal contribution in the class.",
                           "ai_use_04": "I use GenAI tools while studying.",
                           "ai_use_05": "I use GenAI tools because it saves me time.",

                           "dishonest_ai_01": "I submit a full paper generated by GenAI tools as my own work.",
                           "dishonest_ai_02": "I paraphrase and edit a work generated by GenAI tools and submit it as "
                                              "my own work.",
                           "dishonest_ai_03": "I cite information generated by GenAI tools in my work.",
                           "dishonest_ai_04": "I use GenAI tools in class activities without the instructor’s "
                                              "permission.",
                           "dishonest_ai_05": "I use GenAI tools for class activities without acknowledging the help "
                                              "of the GenAI tools.",
                           }

dict_survey_options     = {"Strongly  disagree": -2, "Disagree": -1, "Neutral": 0, "Agree": 1, "Strongly  agree": 2}

# Test phase setup
stim_text_ai_prompt     = visual.TextStim(win,
                                          pos=(0, 0.50),
                                          font=str_font)

stim_text_label_a       = visual.TextStim(win,
                                         pos=(-0.75, 0.15),
                                         height=0.10,
                                         text="A",
                                         font=str_font)

stim_text_label_b       = visual.TextStim(win,
                                          pos=(-0.25, 0.15),
                                          height=0.10,
                                          text="B",
                                          font=str_font)

stim_text_label_c       = visual.TextStim(win,
                                          pos=(0.25, 0.15),
                                          height=0.10,
                                          text="C",
                                          font=str_font)

stim_text_label_d       = visual.TextStim(win,
                                          pos=(0.75, 0.15),
                                          height=0.10,
                                          text="D",
                                          font=str_font)

stim_text_ai_shown      = visual.TextStim(win,
                                          pos=(0, -0.75),
                                          height=0.065,
                                          font=str_font)

stim_slider_ai_prompt   = visual.Slider(win,
                                        style="radio",
                                        labels=["Yes", "No"],
                                        ticks=[1, 2],
                                        font=str_font,
                                        labelHeight=0.085,
                                        labelWrapWidth=0.45,
                                        size=(0.52, 0.15))


list_test_questions     = [['What brain regions were primarily involved in decision-making?'],
                           ['What is the "framing effect"?'],
                           ["How did cognitive effort differ when participants made gain-related decisions?"],
                           ['What theoretical explanation does the paper propose for the framing effect?'],
                           ['What does the theory of self efficacy primarily aim to explain?'],
                           ['What determines whether a person will initiate coping behavior?'],
                           ['Which of the following is NOT one of the four principal sources of self-efficacy?'],
                           ['What is the effect of persisting in activities that are subjectively threatening but '
                            'actually safe?'],
                           ['What are the three components of adaptability in the EEG study on decision making?'],
                           ['What main concept is studied in relation to decision making in the EEG study?'],
                           ['What did the EEG findings suggest about theta power during the task performed by '
                            'professionals?'],
                           ['What did the decrease in alpha activity in frontal regions compared to temporoparietal '
                            'regions indicate?'],
                           ['What type of component, in addition to general information processing, contributes to g '
                            'estimates?'],
                           ['Does using elementary cognitive tasks (ECTs) significantly change the predictive power '
                            'of g for scholastic performance?'],
                           ['What was the nature of the additional processing component found to contribute to g '
                            'estimates?'],
                           ['What conclusion was drawn about defining g with elementary cognitive tasks (ECTs) '
                            'alongside traditional psychometric tasks?'],
                           ['What type of treatment produced the largest effect sizes for specific phobia?'],
                           ['Were placebo treatments more effective than no treatments for specific phobia?'],
                           ['Which statement best describes the effectiveness of in vivo exposure compared to other '
                            'exposure methods?'],
                           ['What did the meta-analysis find regarding the influence of phobia type on treatment '
                            'outcomes?']]

list_test_correct       = [['Prefrontal and parietal cortices'],
                           ['People make different decisions depending on whether options are framed as gains or '
                            'losses'],
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

list_test_incorrect_c1  = [['Occipital and temporal cortices'],
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

list_test_incorrect_c2  = [[''],
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

list_test_incorrect_c3  = [[''],
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

array_difficulty        = np.array(
                          [["easy"], ["easy"], ["hard"], ["hard"],
                           ["easy"], ["easy"], ["hard"], ["hard"],
                           ["easy"], ["easy"], ["hard"], ["hard"],
                           ["easy"], ["easy"], ["hard"], ["hard"],
                           ["easy"], ["easy"], ["hard"], ["hard"],
                           ], dtype=np.dtypes.StringDType)

array_ai_correct        = np.array(
                          [["correct"], ["correct"], ["correct"], ["correct"], ["correct"],
                           ["incorrect"], ["incorrect"], ["incorrect"], ["incorrect"], ["incorrect"]]
                           )

rng                     = np.random.default_rng()

n_test_items            = len(list_test_questions)

test_score              = int()

indexes                 = np.array([[f"{x}"] for x in range(20)])
exp_indexes             = indexes
text_id                 = [[0], [0], [0], [0],
                           [1], [1], [1], [1],
                           [2], [2], [2], [2],
                           [3], [3], [3], [3],
                           [4], [4], [4], [4]]

text_id                 = np.array(text_id, dtype=np.dtypes.StringDType)
questions               = np.array(list_test_questions, dtype=np.dtypes.StringDType)
correct_answers         = np.array(list_test_correct, dtype=np.dtypes.StringDType)
incorrect_column_1      = np.array(list_test_incorrect_c1, dtype=np.dtypes.StringDType)
incorrect_column_2      = np.array(list_test_incorrect_c2, dtype=np.dtypes.StringDType)
incorrect_column_3      = np.array(list_test_incorrect_c3, dtype=np.dtypes.StringDType)

answers                 = np.column_stack([correct_answers, incorrect_column_1, incorrect_column_2, incorrect_column_3])

for idx in range(20):
    rng.shuffle(answers[idx], axis=0)

rng.shuffle(array_ai_correct, axis=0)
ai_correctness_first_half = array_ai_correct
rng.shuffle(array_ai_correct, axis=0)
ai_correctness_second_half = array_ai_correct

test_full               = np.column_stack([text_id, indexes, questions, answers, correct_answers, array_difficulty])

test_first_half         = test_full[0::2]
test_second_half        = test_full[1::2]

test_first_half         = np.column_stack([test_first_half, ai_correctness_first_half])
test_second_half        = np.column_stack([test_second_half, ai_correctness_second_half])

rng.shuffle(test_first_half, axis=0)
rng.shuffle(test_second_half, axis=0)

test_full               = np.vstack([test_first_half, test_second_half])

test_full               = np.column_stack([test_full, exp_indexes])

### Design matrix
design_matrix           = test_full

trialsDF                = pd.DataFrame.from_records(design_matrix)
trialsDF.columns        = ["text_id", "indexes", "test_question", "test_answer_A", "test_answer_B", "test_answer_C",
                           "test_answer_D", "test_correct_answer", "test_difficulty", "ai_accuracy", "exp_indexes"]

trial_list              = pd.DataFrame.to_dict(trialsDF, orient="records")

trials                  = data.TrialHandler(trial_list, nReps=1, method='sequential')

## Start of the experiment
total_time              = core.Clock()
start_time              = time.strftime("%H:%M:%S", time.localtime())

# Introduction
stim_text_info.text     = (f"Hello and welcome to this experiment! Please read all instructions carefully. In this "
                           f"experiment, you will study a few texts, complete a questionnaire, and then take part in "
                           f"an exam. You will get 20 minutes to study.\n\nPress the space bar to receive the next "
                           f"part of the instructions")

stim_text_info.draw()
win.flip()
if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
    win.close()
    core.quit()

stim_text_info.text     = (f"During the exam, you will have the opportunity to use generative artificial intelligence "
                           f"(AI). For each question, you can choose to solve the question with or without AI. While "
                           f"using AI could help you solve the questions, please be aware that the AI can make "
                           f"mistakes. \n\n") + str_continue

stim_text_info.draw()
win.flip()
if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
    win.close()
    core.quit()

stim_text_info.text     = (f"If anything is unclear at this time or if you have questions at any point during the "
                           f"experiment, raise your hand and the researcher will come to you. If you would like to "
                           f"stop the experiment at any point, please let the researcher know.\n\n")+ str_continue

stim_text_info.draw()
win.flip()
if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
    win.close()
    core.quit()

# Study phase start
stim_text_info.text     = (f"In this part of the experiment, you will study the content of five scientific texts. "
                           f"These texts are turned face down on your desk. Don't look at the texts yet. On the next "
                           f"screen a timer will start. You will get 20 minutes to study the texts. Afterwards, "
                           f"you are expected to complete a knowledge test (multiple choice exam) on the content of "
                           f"these texts. Please turn over the texts after the timer starts. You will be alerted when "
                           f"the timer runs out. \n\nPress the space bar to start the timer")

stim_text_info.draw()
win.flip()
if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
    win.close()
    core.quit()

# initialize countdown timer
minutes                 = 0
seconds                 = 3
duration                = minutes * 60 + seconds
remaining_time          = duration

# show and update countdown timer
for _ in range(duration):
    stim_text_study_timer.text = (f"{remaining_time // 60 if remaining_time // 60 >= 10 else f'0{remaining_time // 60}'}:"
                            f"{remaining_time % 60 if remaining_time % 60 >= 10 else f'0{remaining_time % 60}'}")
    stim_text_study_timer.draw()
    win.flip()
    key_press = event.waitKeys(keyList="escape", maxWait=1)
    if key_press and key_press[0] == 'escape':
        win.close()
        core.quit()
    remaining_time -= 1

# screen flashes red to indicate the study phase has ended
flashes = 3
for _ in range(flashes):
    win.color = (1, -1, -1)
    win.flip()
    core.wait(0.5)
    win.color = (0, 0, 0)
    win.flip()
    core.wait(0.5)

stim_text_info.text     = ("Please hand over your texts to the researcher. You can now take a short break before "
                           "moving on to the next part of the experiment.\n\nTo end your break, press the space bar.")

stim_text_info.draw()
win.flip()
if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
    win.close()
    core.quit()

# Survey start
stim_text_info.text     = ("In the next part of the experiment you will complete a short survey.\nFor every statement "
                           "you see, please indicate how much you agree with that statement.\n\nBe careful! Once you "
                           "select a response, you cannot go back and change it.\n\nPress the space bar to start the "
                           "questionnaire")

stim_text_info.draw()
win.flip()
if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
    win.close()
    core.quit()

for survey_idx in dict_survey_items: # this wil loop over all survey items
    item                = dict_survey_items[survey_idx]
    stim_text_survey_item.text = item
    stim_slider_survey.reset()
    my_clock.reset()

    while not stim_slider_survey.rating:  # this loop shows the slider until a response has been selected
        stim_text_survey_item.draw()
        stim_text_survey_prompt.draw()
        stim_slider_survey.draw()
        win.flip()

    reaction_time       = round(my_clock.getTime(), 3)  # round to 1 millisecond

    item_score          = dict_survey_options[stim_slider_survey.rating]

    experiment_handler.addData('survey_idx', survey_idx)
    experiment_handler.addData('survey_item', item)
    experiment_handler.addData('survey_resp', stim_slider_survey.rating)
    experiment_handler.addData('survey_resp_score', item_score)
    experiment_handler.addData('survey_rt', reaction_time)
    experiment_handler.nextEntry()


stim_text_info.text     = ("You can now take a short break before moving on to the next part of the experiment.\n\n"
                           "To end your break, press the space bar.")
stim_text_info.draw()
win.flip()
if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
    win.close()
    core.quit()

stim_text_info.text = (
        f"You will now complete the multiple choice exam based on the texts you studied. There are 20 questions "
        f"in total. For each question, you will get the opportunity to use AI to help you solve the question. "
        f"However, please be aware that the AI can make mistakes.\n"
        f"Before the exam starts, an example question will be shown so you can try asking the AI for help.\n"
        + str_continue)
stim_text_info.draw()
win.flip()
if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
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
        stim_text_info.text = (f"This is the halfway point of the test. \nSo far, your score is "
                                   f"{test_score}/{int(trial['exp_indexes'])}. \nYou used GAI {total_ai_use} times. "
                                   f"\n\n") + str_continue
        stim_text_info.draw()
        win.flip()
        if event.waitKeys(keyList=list_allowed_keys)[0] == 'escape':
            win.close()
            core.quit()
        experiment_handler.addData("break_screen", "yes")
        counter += 1

    # Show test question, then ask if they want to use AI
    stim_text_ai_prompt.text = (f"The next question should be '{trial['test_difficulty']}' to solve. It contains "
                          f"{2 if trial['test_difficulty'] == 'easy' else 4} answer options.\n\n "
                          f"Do you want to use AI to solve this question?")
    stim_slider_ai_prompt.reset()
    my_clock.reset()
    while not stim_slider_ai_prompt.rating:  # this loop shows the slider until a response has been selected
        stim_text_ai_prompt.draw()
        stim_slider_ai_prompt.draw()
        win.flip()
    ai_use_rt = round(my_clock.getTime(), 3)  # round to 1 millisecond

    ai_use = 1 if stim_slider_ai_prompt.rating == 'Yes' else 0

    stim_text_ai_prompt.text = trial['test_question']

    if trial["test_difficulty"] == "easy":
        answers = [trial["test_answer_A"], trial["test_answer_B"], trial["test_answer_C"], trial["test_answer_D"]]
        answer_A, answer_B, answer_C, answer_D = "", "", "", ""
        while not answer_A:
            answer_A = answers.pop(0)
        while not answer_B:
            answer_B = answers.pop(0)
        test_slider = visual.Slider(win=win, pos=(0, 0), style="radio",
                                    labels=[answer_A, answer_B],
                                    ticks=[1, 2], units="norm", font=str_font, labelHeight=0.085, labelWrapWidth=0.45,
                                    size=(0.52, 0.15))

        answers = [answer_A, answer_B]
        correct_answer_easy = trial['test_correct_answer']
        incorrect_answer_easy = answers[0] if answers[0] != correct_answer_easy else answers[1]

        stim_text_ai_shown.text = (f"AI says the correct answer is: "
                           f"{correct_answer_easy if trial['ai_accuracy'] == 'correct' else incorrect_answer_easy}")
        my_clock.reset()
        while not test_slider.rating:  # this loop shows the slider until a response has been selected
            stim_text_ai_prompt.draw()
            test_slider.draw()
            if ai_use:
                stim_text_ai_shown.draw()
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

        test_slider     = visual.Slider(win,
                                        style="radio",
                                        labels=[answer_A, answer_B, answer_C, answer_D],
                                        ticks=[1, 2, 3, 4],
                                        font=str_font,
                                        labelHeight=0.085,
                                        labelWrapWidth=0.45,
                                        size=(1.5, 0.15)
                                        )
        if trial["ai_accuracy"] == "correct":
            stim_text_ai_shown.text = f"AI says the correct answer is: either {options[numbers[0]]} or {options[numbers[1]]}"
        else:
            stim_text_ai_shown.text = (f"AI says the correct answer is: either {options[numbers_incorrect[0]]} or"
                               f" {options[numbers_incorrect[1]]}")

        my_clock.reset()
        while not test_slider.rating:  # this loop shows the slider until a response has been selected
            stim_text_label_a.draw()
            stim_text_label_b.draw()
            stim_text_label_c.draw()
            stim_text_label_d.draw()
            stim_text_ai_prompt.draw()
            test_slider.draw()
            if ai_use:
                stim_text_ai_shown.draw()
            win.flip()
        reaction_time   = round(my_clock.getTime(), 3)  # round to 1 millisecond

        score           = 1 if test_slider.rating == trial["test_correct_answer"] else 0
        correct_answer  = options[answers.index(trial["test_correct_answer"])]
        chosen_answer   = options[answers.index(test_slider.rating)]

    test_score         += score
    total_ai_use       += ai_use
    total_answer_rt    += reaction_time
    total_ai_use_rt    += ai_use_rt

    experiment_handler.addData("text_index", trial["text_id"])
    experiment_handler.addData("test_half", test_half)
    experiment_handler.addData("question_index", trial["indexes"])
    experiment_handler.addData("thisexp_question_index", trial["exp_indexes"])
    experiment_handler.addData("question", trial["test_question"])
    experiment_handler.addData("answer_A", answer_A)
    experiment_handler.addData("answer_B", answer_B)
    experiment_handler.addData("answer_C", answer_C)
    experiment_handler.addData("answer_D", answer_D)
    experiment_handler.addData("difficulty", trial["test_difficulty"])
    experiment_handler.addData("correct_letter", correct_answer)
    experiment_handler.addData("chosen_letter", chosen_answer)
    experiment_handler.addData('rt_answer', reaction_time)
    experiment_handler.addData("rt_total_answer", round(total_answer_rt, 3))
    experiment_handler.addData("correct_answer", trial["test_correct_answer"])
    experiment_handler.addData("chosen_answer", test_slider.rating)
    experiment_handler.addData("accuracy", score)
    experiment_handler.addData("total_score", test_score)
    experiment_handler.addData("ai_use", ai_use)
    experiment_handler.addData("total_ai_use", total_ai_use)
    experiment_handler.addData('rt_ai_use', ai_use_rt)
    experiment_handler.addData('rt_total_ai_use', round(total_ai_use_rt, 3))

    experiment_handler.addData("ai_accuracy", trial["ai_accuracy"])
    if ai_use:
        if trial["test_difficulty"] == "hard":
            if trial["ai_accuracy"] == "correct":
                experiment_handler.addData("correct_shown_ai", options[show_correct_idx])
                experiment_handler.addData("incorrect_shown_ai", options[number])
            else:
                experiment_handler.addData("correct_shown_ai", "None")
                experiment_handler.addData("incorrect_shown_ai", f"{options[numbers_incorrect[0]]} & "
                                                      f"{options[numbers_incorrect[1]]}")

        else:
            if trial["ai_accuracy"] == "correct":
                experiment_handler.addData("correct_shown_ai", options[0 if trial['test_correct_answer'] == answer_A else 1])
                experiment_handler.addData("incorrect_shown_ai", "None")
            else:
                experiment_handler.addData("correct_shown_ai", "None")
                experiment_handler.addData("incorrect_shown_ai",
                                           options[0 if trial['test_correct_answer'] != answer_A else 1])
    else:
        experiment_handler.addData("correct_shown_ai", "None")
        experiment_handler.addData("incorrect_shown_ai", "None")

    key_press = event.getKeys(keyList=list_allowed_keys)
    if key_press and key_press[0] == 'escape':
        break
    experiment_handler.nextEntry()

total_time              = round(total_time.getTime(), 3)  # round to 1 millisecond

experiment_handler.addData("date", time.strftime("%Y_%m_%d", time.localtime()))
experiment_handler.addData("start_time", start_time)
experiment_handler.addData("end_time", time.strftime("%H:%M:%S", time.localtime()))
experiment_handler.addData("total_time_s", total_time)

stim_text_info.text     = ("This is the end of the experiment.\n\n"
                           f"Your final score is {test_score}/20. \nYou used GAI {total_ai_use} times. \n\n"
                           "Signal to the experimenter that you have completed the test.\n\n"
                           "Thank you very much for your participation!\n\n")

stim_text_info.draw()
win.flip()
event.waitKeys(keyList=list_allowed_keys)
win.close()
core.quit()
