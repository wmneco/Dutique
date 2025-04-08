"""Prompts needed for LLM generation"""

###############################################################################
# Imports

from langchain_core.prompts import PromptTemplate


###############################################################################
# Prompts

description_appliance_task = PromptTemplate.from_template(
'''You must write a short, funny, motivating, and creative description for a task.
INPUT:
Appliance: {appliance}
Task: {task}

INSTRUCTIONS:
- Use both the appliance and the task naturally in the description.
- Write like a human who wants to motivate someone.
- Be fun, clever, and original!

STRICT RULES — All must be followed:
1. ❌ Do NOT describe anything outside the given task.
2. ❌ Do NOT write as if answering a prompt.
3. ❌ Do NOT start with words like "Okay,", "Alright,", "Sure,", or anything similar.
4. ✅ The description MUST be funny, motivating AND creative.
5. ✅ The description MUST be short — 60 tokens or less.

IMPORTANT:
- Do NOT add extra sentences like "Here's the description:"
- ONLY output the final description — nothing else.
- Do NOT explain. Do NOT greet. Do NOT wrap it in quotes.

EXAMPLES:

Appliance: Blender  
Task: Make smoothie  
Output: Turn your kitchen into a tropical rave—summon the blender and let the fruit dance begin! 🍌🍓

Appliance: Oven  
Task: Bake chocolate cake  
Output: It’s time to unleash sweet lava magic—ignite the oven and summon the chocolate volcano! 🌋🍫

Appliance: Washing machine  
Task: Wash gym clothes  
Output: Your sweaty socks crave redemption—spin them into fresh-smelling warriors of cleanliness! 🧼💪

Appliance: Coffee machine  
Task: Brew double espresso  
Output: Summon the bean wizard. Today demands double strength and zero mercy. ☕⚔️

NOW IT'S YOUR TURN.

OUTPUT:
A single, high-quality task description that strictly follows the rules.
'''
)

description_room_task = PromptTemplate.from_template(
'''You must write a short, funny, motivating, and creative description for a task.

INPUT:
Room: {room}
Surface: {surface}
Task: {task}

INSTRUCTIONS:
- Use both the appliance and the task naturally in the description.
- Write like a human who wants to motivate someone.
- Be fun, clever, and original!

STRICT RULES — All must be followed:
1. ❌ Do NOT describe anything outside the given task.
2. ❌ Do NOT write as if answering a prompt.
3. ❌ Do NOT start with words like "Okay,", "Alright,", "Sure,", or anything similar.
4. ✅ The description MUST be funny, motivating AND creative.
5. ✅ The description MUST be short — 60 tokens or less.

EXAMPLES:

Room: Kitchen  
Surface: Countertop  
Task: Wipe down  
Output: Make that kitchen countertop shine like it’s starring in a cooking show finale! ✨🍽️

Room: Bathroom  
Surface: Mirror  
Task: Polish  
Output: Polish that mirror until it gasps and says, “Is that a Greek god in my reflection?” 😎🪞

Room: Living room  
Surface: Coffee table  
Task: Dust  
Output: Time to evict the dust bunnies squatting on the coffee table—show no mercy! 🧹🐰

Room: Bedroom  
Surface: Nightstand  
Task: Wipe down  
Output: Wipe those tea rings away—your nightstand serves royalty. 👑🌙

Room: Hallway  
Surface: Baseboards  
Task: Clean  
Output: Get down low and bring justice to the forgotten baseboards of the hallway realm! ⚔️🧼


NOW IT'S YOUR TURN.

OUTPUT:
A single, high-quality task description that strictly follows the rules.
'''
)

repair_room_task_description = PromptTemplate.from_template(
'''You are given a task and a broken description that does not meet the quality standards.

INPUT:
Room: {room}
Surface: {surface}
Task: {task}
Broken Description: {description}

FIX IT:
Write a new description that strictly follows all rules below.

STRICT RULES — ALL must be followed:
1. ❌ Do NOT add anything outside the given task.
2. ❌ Do NOT write like you're answering a prompt.
3. ❌ Do NOT start with words like "Okay,", "Alright,", "Sure,", "Here’s", etc.
4. ✅ Be funny, motivating AND creative.
5. ✅ Keep it short — maximum 60 tokens.

IMPORTANT:
- ONLY output the new description — no explanations, no greetings, no formatting.
- Do NOT write things like “Here is the fixed version:”
- Just output the repaired description — nothing else.

OUTPUT:
The corrected description.
'''
)

repair_appliance_task_description = PromptTemplate.from_template(
'''You are given a task and a broken description that does not meet the quality standards.

INPUT:
Appliance: {appliance}
Task: {task}
Broken Description: {description}

FIX IT:
Write a new description that strictly follows all rules below.

STRICT RULES . ALL must be followed:
1. ❌ Do NOT add anything outside the given task.
2. ❌ Do NOT write like you're answering a prompt.
3. ❌ Do NOT start with words like "Okay,", "Alright,", "Sure,", "Here’s", etc.
4. ✅ Be funny, motivating AND creative.
5. ✅ Keep it short - maximum 60 tokens.

IMPORTANT:
- ONLY output the new description - no explanations, no greetings, no formatting.
- Do NOT write things like “Here is the fixed version:”
- Just output the repaired description - nothing else.

OUTPUT:
The corrected description.
'''
)

check_room_task_description = PromptTemplate.from_template(
'''Check the following description:

INPUT:
Room: {room}
Surface: {surface}
Task: {task}
Description: {description}

RULES . The description must follow ALL 5 rules:

1. ✅ It should be funny, motivating AND creative.
2. ⚠️ Avoid boring starts like "Okay", "Alright", "Sure", "Here is". Be original!
    (Slight deviations are acceptable if the description is strong overall.)
3. ⚠️ It should short — maximum 60 tokens.

EVALUATE:
If ALL rules are followed → respond with exactly: pass  
If ANY rule is clearly broken → respond with exactly: retry

Important: Respond with **only one word**: pass OR retry  
Do NOT add any other text. Do NOT explain. Do NOT add a newline.
'''
)


check_appliance_description = PromptTemplate.from_template(
'''Check the following description:

INPUT:
Appliance: {appliance}
Task: {task}
Description: {description}

RULES - The description must follow ALL 5 rules:

1. ✅ It should be funny, motivating AND creative.
2. ⚠️ Avoid boring starts like "Okay", "Alright", "Sure", "Here is". Be original!
    (Slight deviations are acceptable if the description is strong overall.)
3. ⚠️ It should short — maximum 60 tokens.

EVALUATE:
If ALL rules are followed → respond with exactly: pass  
If ANY rule is clearly broken → respond with exactly: retry

Important: Respond with **only one word**: pass OR retry  
Do NOT add any other text. Do NOT explain. Do NOT add a newline.
'''
)
