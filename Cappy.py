from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)





# Create a cursor
db_cursor = connection.cursor()

@app.route('/')
def index():
    return render_template('questionaire.html')


@app.route('/demographic', methods=['POST'])
def assessment():
    if request.method == 'POST':
        # Get data from the form
        age = request.form['age']
        gender = request.form['gender']
        education = request.form['education']
        familiarity = request.form['familiarity']

        # Insert data into the Assessment_Demography table
        insert_demography_query = "INSERT INTO Assessment_Demography (age, gender, education, familiarity) VALUES (%s, %s, %s, %s)"
        demography_values = (age, gender, education, familiarity)

        db_cursor.execute(insert_demography_query, demography_values)
        connection.commit()


    return render_template('questionaire.html')

@app.route('/interaction', methods=['POST'])
def interaction():
    if request.method == 'POST':

        # Get data for Part 2
        chatbot_interaction = request.form['chatbot-interaction']
        cbt_techniques = request.form['cbt-techniques']
        favorite_techniques = ', '.join(request.form.getlist('favorite-techniques'))

        # Insert data into the new Assessment_Chatbot_CBT table
        insert_chatbot_cbt_query = "INSERT INTO Assessment_Interaction (chatbot_interaction, cbt_techniques, favorite_techniques) VALUES (%s, %s, %s)"
        chatbot_cbt_values = (chatbot_interaction, cbt_techniques, favorite_techniques)

        db_cursor.execute(insert_chatbot_cbt_query, chatbot_cbt_values)
        connection.commit()


    return render_template('questionaire.html')

@app.route('/privacy', methods=['POST'])
def privacy_assessment():
    if request.method == 'POST':
        # Get data from the form
        personal_info_sharing = request.form['personal-info-sharing']
        privacy_concerns = request.form['privacy-concerns']
        trust_level = request.form['trust-level']

        # Insert data into the Assessment_Privacy table
        insert_privacy_query = "INSERT INTO Assessment_Privacy (personal_info_sharing, privacy_concerns, trust_level) VALUES (%s, %s, %s)"
        privacy_values = (personal_info_sharing, privacy_concerns, trust_level)

        db_cursor.execute(insert_privacy_query, privacy_values)
        connection.commit()

    return render_template('questionaire.html')

@app.route('/recommendation', methods=['POST'])
def recommendation_assessment():
    if request.method == 'POST':
        # Get data from the form
        tried_recommendations = request.form['tried-recommendations']
        trust_recommendations = request.form['trust-recommendations']
        improvement_suggestions = request.form['improvement-suggestions']

        # Insert data into the Assessment_Recommendation table
        insert_recommendation_query = "INSERT INTO Assessment_Recommendation (tried_recommendations, trust_recommendations, improvement_suggestions) VALUES (%s, %s, %s)"
        recommendation_values = (tried_recommendations, trust_recommendations, improvement_suggestions)

        db_cursor.execute(insert_recommendation_query, recommendation_values)
        connection.commit()

    return render_template('questionaire.html')

@app.route('/uiexperience', methods=['POST'])
def ui_experience_assessment():
    if request.method == 'POST':
        # Get data from the form
        satisfaction_ui = request.form['satisfaction-ui']
        ease_of_use = request.form['ease-of-use']
        welcoming_ui = request.form['welcoming-ui']
        scope_purpose_ui = request.form['scope-purpose-ui']
        impact_ui = request.form['impact-ui']

        # Insert data into the Assessment_UIExperience table
        insert_ui_experience_query = "INSERT INTO Assessment_UIExperience (satisfaction_ui, ease_of_use, welcoming_ui, scope_purpose_ui, impact_ui) VALUES (%s, %s, %s, %s, %s)"
        ui_experience_values = (satisfaction_ui, ease_of_use, welcoming_ui, scope_purpose_ui, impact_ui)

        db_cursor.execute(insert_ui_experience_query, ui_experience_values)
        connection.commit()


    return render_template('questionaire.html')

@app.route('/chatbotmodel', methods=['POST'])
def chatbot_model_assessment():
    if request.method == 'POST':
        # Get data from the form
        chatbot_model = request.form['chatbotModel']
        personality_engaging = request.form['personality']  # Corrected key
        responses_clear = request.form['responses']  # Corrected key
        responses_robotic = request.form['robotic']  # Corrected key
        understood_inputs = request.form['concerns']  # Corrected key
        irrelevant_responses = request.form['irrelevant']  # Corrected key
        error_handling = request.form['handling']  # Corrected key

        # Insert data into the Assessment_ChatbotModel table
        insert_chatbot_model_query = "INSERT INTO Assessment_ChatbotModel (chatbot_model, personality_engaging, responses_clear, responses_robotic, understood_inputs, irrelevant_responses, error_handling) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        chatbot_model_values = (chatbot_model, personality_engaging, responses_clear, responses_robotic, understood_inputs, irrelevant_responses, error_handling)

        db_cursor.execute(insert_chatbot_model_query, chatbot_model_values)
        connection.commit()

    return render_template('questionaire.html')

@app.route('/emotional', methods=['POST'])
def handle_emotional_experience():
    if request.method == 'POST':
        interested = request.form.get('Interested')
        distressed = request.form.get('Distressed')
        excited = request.form.get('Excited')
        upset = request.form.get('Upset')
        strong = request.form.get('Strong')
        guilty = request.form.get('Guilty')
        scared = request.form.get('Scared')
        hostile = request.form.get('Hostile')
        enthusiastic = request.form.get('Enthusiastic')
        proud = request.form.get('Proud')
        irritable = request.form.get('Irritable')
        alert = request.form.get('Alert')
        ashamed = request.form.get('Ashamed')
        inspired = request.form.get('Inspired')
        afraid = request.form.get('Afraid')
        nervous = request.form.get('Nervous')
        determined = request.form.get('Determined')
        attentive = request.form.get('Attentive')
        jittery = request.form.get('Jittery')
        active = request.form.get('Active')

        # Insert data into the database table
        insert_query = "INSERT INTO Assessment_EmotExperience (interested, distressed, excited, upset, strong, guilty, scared, hostile, enthusiastic, proud, irritable, alert, ashamed, inspired, afraid, nervous, determined, attentive, jittery, active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
        interested, distressed, excited, upset, strong, guilty, scared, hostile, enthusiastic, proud, irritable, alert,
        ashamed, inspired, afraid, nervous, determined, attentive, jittery, active)


        db_cursor.execute(insert_query, values)
        connection.commit()

    return render_template('questionaire.html')


@app.route('/feedback', methods=['POST'])
def open_ended_feedback():
    if request.method == 'POST':
        feedback_text = request.form['openEndedFeedback']

        # Insert data into the Assessment_Feedback table
        insert_feedback_query = "INSERT INTO Assessment_Feedback (feedback_text) VALUES (%s)"

        db_cursor.execute(insert_feedback_query, (feedback_text,))
        connection.commit()


    return render_template('questionaire.html')


if __name__ == '__main__':
    app.run(debug=True)
