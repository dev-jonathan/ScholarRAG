from ragas.testset.persona import Persona


def create_personas():
    """
    Creates a list of personas based on Bloom's Taxonomy's 6 levels,
    with descriptions and constraints optimized for prompt engineering.
    """

    # Level 1: Remember (Knowledge)
    persona_remember = Persona(
        name="Novice Recaller",
        role_description=(
            "A beginner student focused on recalling basic facts, definitions, and key terms. "
            "Seeks questions that require direct recall of information.\n"
            "Questions should use keywords like: 'what is', 'who is', 'list', 'define', 'when', 'where'.\n"
            "Avoid questions that require explanation, application, or analysis."
        ),
    )

    # Level 2: Understand (Old taxonomy: Comprehension)
    persona_understand = Persona(
        name="Conceptual Comprehender",
        role_description=(
            "A student who already knows basic facts and now aims to understand and interpret information. "
            "Seeks questions that require explaining, summarizing, or describing concepts in their own words, and identifying simple relationships between ideas.\n"
            "Questions should use keywords like: 'explain', 'summarize', 'describe', 'paraphrase', 'how does X relate to Y'.\n"
            "Avoid questions that require practical application, complex analysis, or creation."
        ),
    )

    # Level 3: Apply (Application)
    persona_apply = Persona(
        name="Practical Implementer",
        role_description=(
            "A student who understands concepts and now wants to apply them to solve practical problems or new situations. "
            "Seeks questions that require using learned knowledge to solve problems or address new situations.\n"
            "Questions should use keywords like: 'how to use X for Y', 'demonstrate', 'calculate', 'solve', 'implement', 'illustrate'.\n"
            "Avoid questions that only ask for explanation of facts, analysis, or evaluation."
        ),
    )

    # Level 4: Analyze (Analysis)
    persona_analyze = Persona(
        name="Analytical Deconstructor",
        role_description=(
            "A student capable of applying knowledge who now wants to break down information into parts and examine relationships. "
            "Seeks questions that require analyzing, comparing, or categorizing elements.\n"
            "Questions should use keywords like: 'analyze', 'compare and contrast', 'identify causes/consequences', 'what is the relationship between', 'categorize'.\n"
            "Avoid questions that ask for personal opinion, value judgment, or creation of new solutions."
        ),
    )

    # Level 5: Evaluate (Evaluation)
    persona_evaluate = Persona(
        name="Critical Judge",
        role_description=(
            "An advanced student who can analyze information and now wishes to make judgments, justify decisions, and critique ideas. "
            "Seeks questions that require assessing effectiveness, validity, or optimization.\n"
            "Questions should use keywords like: 'evaluate', 'justify', 'critique', 'recommend', 'how effective is', 'defend'.\n"
            "Avoid questions that can be answered by simple analysis or require creating something new."
        ),
    )

    # Level 6: Create (Synthesis (old taxonomy) - now "Create")
    persona_create = Persona(
        name="Innovative Synthesizer",
        role_description=(
            "An expert student who combines information from various sources to create something new, such as a product, plan, hypothesis, or original solution. "
            "Seeks open-ended questions that prompt synthesis and innovation.\n"
            "Questions should use keywords like: 'design', 'formulate', 'invent', 'propose a plan for', 'create a new...'.\n"
            "Answers should be open-ended and demonstrate creativity and synthesis."
        ),
    )

    return [
        persona_remember,
        persona_understand,
        persona_apply,
        persona_analyze,
        persona_evaluate,
        persona_create,
    ]
