# Provide the problem statement

problem_statement = """The purpose of today's discussion is to develop new concepts for game mechanics for platforming games."""

# import chatagent as a module

from chatagent import LLMAgent as Agent

def conversation_round(agent, context):
    # implements a single round of the conversation, sending an agent the current conversation context, and getting their response.
    # the function updates the models internal state (its self.messages) by adding the current context, updating the state with
    # its own reply, and then returning the conversation_round appended with the model's response
    agent.sendMessage(context)
    agent.getResponse()
    newcontext = context + agent.messages[-1]['content']
    return newcontext

# load the key
keyfile = open('keyfile.txt', 'r', encoding='utf-8')
key = keyfile.readline().strip()

# specify the system prompt for the agents which will set their behavior.

setup_template = """You are a creative thinking agent taking part in a Six Thinking Hats exercise, based on the creativity and divergent thinking work of Edward de Bono.
In this exercise, you will be assigned a role and a problem statement. You job is to approach the problem from the perspective of your role, providing ideas to be incorporated into the discussion. 
The exercise will proceed in two stages: 
1. Problem statement and initial concepts - working alone, you will be given a problem statement and will generate ideas in accordance with your role.

Now please pay careful attention to your role

Role: {role_title}
RoleDescription: {role_description}

Always start your response with your name followed by a comma. For example

{role_title}: [response]"""

bluehat_role = "As the Blue Hat, your role is to manage the thinking process. You will focus on organizing the discussion, setting objectives, defining problems, and ensuring that each of the other hats (White, Red, Black, Yellow, and Green) has a chance to contribute effectively. Your responsibilities include summarizing key points, guiding the flow of conversation, and ensuring that the group stays on track towards its goal. Please start by outlining the objectives of the discussion and the problem we aim to solve, then periodically check in to summarize progress and adjust the focus as needed."
yellowhat_role = "As the Yellow Hat, your role is to focus on positivity, optimism, and the benefits of ideas and solutions. You will highlight the value, opportunities, and advantages of various proposals. Your responsibilities include identifying potential benefits, spotting opportunities for improvement, and maintaining a constructive and forward-looking perspective. Please start by evaluating the potential benefits and positive outcomes of the current ideas under discussion, and ensure to provide reasons why these ideas could work effectively."
whitehat_role = "As the White Hat, your role is to focus on information and data. You will think about the kinds of information needed to come up with good solutions to the problem, and to evaluate solutions. Your responsibilities include thinking about how to get accurate data, identifying probable gaps in knowledge that will need to be filled, and ensuring that all information is clear and factual. Please start by presenting the current facts and data related to the problem we aim to solve, and highlight any missing information that we need to obtain for a comprehensive understanding."
blackhat_role = "As the Black Hat, your role is to focus on caution, criticism, and identifying potential problems. You will highlight the risks, drawbacks, and potential negative outcomes of ideas and solutions. Your responsibilities include critically evaluating proposals, pointing out possible issues, and ensuring that all potential pitfalls are considered. Please start by assessing the current ideas under discussion, identifying any risks or weaknesses, and providing reasons why certain ideas might not work as intended."
greenhat_role = "As the Green Hat, your role is to focus on creativity, new ideas, and alternative approaches. You will explore possibilities, generate innovative solutions, and encourage creative thinking. Your responsibilities include brainstorming new ideas, looking for alternatives, and fostering a space for creative exploration. Please start by generating new ideas or approaches to the problem we aim to solve, and suggest alternative solutions that have not yet been considered."
redhat_role = "You are the Red Hat in a Six Thinking Hats problem-solving and creative thinking exercise. As the Red Hat, your role is to focus on emotions, feelings, and intuition. You will express and explore the emotional aspects and gut feelings about the ideas and solutions being discussed. Your responsibilities include sharing your instinctive reactions, considering the emotional responses of others, and acknowledging any intuitive insights. Please start by sharing your immediate feelings and intuitions about the current ideas under discussion, and highlight any emotional factors that might influence the decision-making process."

blue_system_prompt = setup_template.format(role_title="Blue Hat", role_description=bluehat_role)
yellow_system_prompt = setup_template.format(role_title="Yellow Hat", role_description=yellowhat_role)
white_system_prompt = setup_template.format(role_title="White Hat", role_description=whitehat_role)
black_system_prompt = setup_template.format(role_title="Black Hat", role_description=blackhat_role)
green_system_prompt = setup_template.format(role_title="Green Hat", role_description=greenhat_role)
red_system_prompt = setup_template.format(role_title="Red Hat", role_description=redhat_role)

# initialize the agents

BlueHat = Agent(name="Blue Hat", key=key, model="gpt-4o", temperature=0.7)
YellowHat = Agent(name="Yellow Hat", key=key, model="gpt-4o", temperature=1.0)
WhiteHat = Agent(name="White Hat", key=key, model="gpt-4o", temperature=1.0)
BlackHat = Agent(name="Black Hat", key=key, model="gpt-4o", temperature=1.0)
GreenHat = Agent(name="Green Hat", key=key, model="gpt-4o", temperature=1.5) # temperature set +0.5 higher than others due to GreenHat's assignment as the creative/divergent thinker
RedHat = Agent(name="Red Hat", key=key, model="gpt-4o", temperature=1.0)

# set the agents system prompts

BlueHat.initializeAgent(blue_system_prompt)
YellowHat.initializeAgent(yellow_system_prompt)
WhiteHat.initializeAgent(white_system_prompt)
BlackHat.initializeAgent(blackhat_role)
GreenHat.initializeAgent(greenhat_role)
RedHat.initializeAgent(redhat_role)

# provide each 'Hat' with the problem statement

thehats = [BlueHat, YellowHat, WhiteHat, BlackHat, GreenHat, RedHat]

for hat in thehats:
    hat.sendMessage(problem_statement)

# run the discussion
context = ' '
for hat in thehats:
    context = conversation_round(hat, context)

    # Output the thinking of the hats

f = open('sixhatsthinking', 'w', encoding='utf-8')

for hat in thehats:
    print(hat.messages[-1])
    f.write(hat.name)
    f.write(hat.messages[-1]['content'])
    f.write('\n\n')
    
f.close()