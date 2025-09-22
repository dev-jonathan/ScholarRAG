```bash
(env_ragas) C:\Users\Jonathan\Desktop\pet\ragas-evaluation>python -m data.testsets.scripts.process_label_studio
Loading JSON dataset...

=== Statistical Validation ===
ragas_faithfulness: n=119, mean=0.953, std=0.141, missing=1
  Missing indices for ragas_faithfulness: [95]
  Missing percentage: 0.8%
ragas_answer_relevancy: n=120, mean=0.799, std=0.173, missing=0
ragas_question_quality: n=120, mean=4.950, std=0.339, missing=0
human_faithfulness: n=120, mean=4.567, std=0.914, missing=0
human_response_relevancy: n=120, mean=4.367, std=0.961, missing=0
human_question_quality: n=120, mean=4.542, std=0.952, missing=0

=== Detailed Exclusion Analysis ===
Samples <=60% in RAGAS but NOT by human: 4
Details of samples with low RAGAS scores but kept due to human evaluation:
  Sample 51:
    RAGAS scores - Faithfulness: 0.500, Answer Relevancy: 0.978, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 4, Question Quality: 5
    User Input: What does one need per pixel for black-and-white images in terms of bits?...
    Response: For black-and-white images, you need 1 bit per pixel....

  Sample 52:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.521, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 5, Question Quality: 5
    User Input: Based on the provided information, how might I design a plan to effectively utilize the [Advice](htt...
    Response: To effectively utilize the [Advice](https://cs50.harvard.edu/x/2024/psets/4/#advice) section, begin ...

  Sample 62:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.471, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 4, Question Quality: 5
    User Input: I wanna create a new plan to check my code, what do I do with staff.txt?...
    Response: To check if your program is outputting the correct misspelled words, you can redirect your program's...

  Sample 63:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.585, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 4, Question Quality: 5
    User Input: How do I implement size to count the words loaded in the dictionary?...
    Response: To implement the `size` function, you have two main approaches. The first approach involves counting...

Samples excluded by human but NOT by RAGAS: 23
Details of human-only exclusions:
  Sample 1:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.822, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 5, Question Quality: 3
    Human Comments: A project can be a generic word in the major context of the course, but in the context of that document is especific and relevant.
    User Input: Describe the requirements for a project in the CS50 course....
    Response: In the CS50 course, your project must be implemented in Scratch and should meet specific requirement...

  Sample 4:
    RAGAS scores - Faithfulness: 0.600, Answer Relevancy: 0.726, Question Quality: 5.000
    Human scores - Faithfulness: 3, Response Relevancy: 3, Question Quality: 4
    Human Comments: The context used is too poor for the use case.
    User Input: How can I use the concept of "Community!" in this context?...
    Response: In this context, "Community!" is a section heading within a lecture. It likely signifies a focus on ...

  Sample 6:
    RAGAS scores - Faithfulness: 0.947, Answer Relevancy: 0.518, Question Quality: 5.000
    Human scores - Faithfulness: 4, Response Relevancy: 2, Question Quality: 5
    Human Comments: The answer is wrong based on the question, is more like a copy of the context.
    User Input: I wanna create a new program, but I'm not sure where to start. Can you propose a plan for using Visu...
    Response: Alright, so you wanna get started with coding, and that's great! When you're ready to write code, we...

  Sample 10:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.707, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 5, Question Quality: 2
    Human Comments: Generic question, ambiguous
    User Input: WHAT IS CORRECTNESS IN THIS CONTEXT, AND HOW DO I CHECK IT?...
    Response: Correctness, in this context, refers to whether your program functions as intended. To check the cor...

  Sample 15:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.811, Question Quality: 5.000
    Human scores - Faithfulness: 4, Response Relevancy: 2, Question Quality: 5
    Human Comments:
    User Input: What are conditionals?...
    Response: Conditionals are mentioned in the context of learning how to use variables, conditionals, and loops ...

  Sample 23:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.000, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 2, Question Quality: 4
    Human Comments: The primary data (context) is too poor and short.
    User Input: How effective is the provided context in offering a comprehensive overview of Cybersecurity?...
    Response: The provided context offers a starting point for understanding Cybersecurity. It includes links to
v...

  Sample 40:
    RAGAS scores - Faithfulness: 0.158, Answer Relevancy: 0.693, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 4, Question Quality: 3
    Human Comments: The context only briefly mentions the Electoral College, but the Q&A fabricates details about its shortcomings and potential reforms
    User Input: Create a new plan for a voting system that incorporates elements of the Electoral College, but aims ...
    Response: The United States uses a multi-step Electoral College process where citizens vote on how each state ...

  Sample 48:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.408, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 2, Question Quality: 1
    Human Comments: Very poor/short (compromised context)


    User Input: How can we use the tool kit to write code?...
    Response: The tool kit includes big O, which represents the upper bound, and Omega, which represents the lower...

  Sample 70:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.678, Question Quality: 5.000
    Human scores - Faithfulness: 4, Response Relevancy: 2, Question Quality: 1
    Human Comments: incoherent question, because of poor/short context.
    User Input: I'm designing a new system for submitting assignments. Can you formulate a plan, incorporating the '...
    Response: To ensure successful submissions, let's formulate a plan based on the provided information. First,
w...

  Sample 71:
    RAGAS scores - Faithfulness: 0.657, Answer Relevancy: 0.739, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 3, Question Quality: 2
    Human Comments: Out of context. The context describes a programming problem in which the student must implement an existing STR-based DNA identification algorithm, given specific input data. The question, by asking for a "plan to create a new method" that "goes beyond current STR analysis," demands a level of innovation and biotechnology/forensic science knowledge that is not, in any way, the focus or content of the provided text. The text provides no basis for discussing SNPs, machine learning, or advanced visualizations.
This was likely caused by the "Innovative Synthesizer" persona.
    User Input: Considering the use of a sequence of DNA in forensic investigations, formulate a plan to create a ne...
    Response: To create a new method for identifying individuals using DNA, we can build upon the existing STR ana...

  Sample 74:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.793, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 2, Question Quality: 2
    Human Comments: The short/poor context compromised the samples
    User Input: What is style?...
    Response: Style is a section in the provided context....

  Sample 75:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.877, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 5, Question Quality: 3
    Human Comments: is accurate to the context. However, the question, being too short and using generic words, creates a lot of ambiguity and wouldn't make sense within the RAG system. Therefore, it was eliminated.
    User Input: When should the problem set be submitted?...
    Response: The problem set should be submitted by 2024-12-31T23:59:00-05:00....

  Sample 79:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.000, Question Quality: 2.000
    Human scores - Faithfulness: 2, Response Relevancy: 2, Question Quality: 2
    Human Comments: Poor/short context
    User Input: Create a new plan using Object-Oriented Programming, yeah?...
    Response: I can't create a plan using Object-Oriented Programming based on this information. The context only ...

  Sample 82:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.594, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 3, Question Quality: 5
    Human Comments:
    User Input: Considering the instructions, how effective is the use of `answers.txt` for reflecting on the provid...
    Response: The instructions require you to reflect on specific questions within `answers.txt`. These questions ...

  Sample 86:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.751, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 2, Question Quality: 4
    Human Comments: Poor/short context compromised the samples
    User Input: WHAT ARE indexes, and WHERE ARE THEY DISCUSSED in this stuff?...
    Response: Indexes are mentioned in the context of a lecture. The lecture is titled "Lecture 7" and the specifi...

  Sample 91:
    RAGAS scores - Faithfulness: 0.182, Answer Relevancy: 0.844, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 2, Question Quality: 2
    Human Comments: hallucination
    User Input: How effective is the deadline of 2024-12-31T23:59:00-05:00 for completing the problem set, and what ...
    Response: The deadline for completing the problem set is 2024-12-31T23:59:00-05:00. The effectiveness of this ...

  Sample 95:
    RAGAS scores - Faithfulness: nan, Answer Relevancy: 0.792, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 3, Question Quality: 4
    Human Comments: Poor/short context compromised the samples
    User Input: Create a plan to learn HTML....
    Response: To learn HTML, you should start by understanding its role in web development. HTML is a core technol...

  Sample 98:
    RAGAS scores - Faithfulness: 0.800, Answer Relevancy: 0.000, Question Quality: 4.000
    Human scores - Faithfulness: 2, Response Relevancy: 2, Question Quality: 2
    Human Comments:
    User Input: How is HTTP used in the context of the internet, as discussed in this lecture?...
    Response: The lecture mentions HTTP at 23:35, within a discussion about the internet. While the lecture provid...

  Sample 107:
    RAGAS scores - Faithfulness: 0.567, Answer Relevancy: 0.886, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 2, Question Quality: 4
    Human Comments: context is disconnected, therefore it does not add knowledge
    User Input: How can I implement Forms within a Flask web application, based on the concepts discussed in this le...
    Response: While this lecture introduces Forms within the context of Flask web applications, it doesn't provide...

  Sample 108:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.926, Question Quality: 3.000
    Human scores - Faithfulness: 3, Response Relevancy: 4, Question Quality: 3
    Human Comments:
    User Input: How effective are APIs in the context of web application development, as discussed in this material?...
    Response: APIs are mentioned in the context of web application development. The material indicates that APIs
a...

  Sample 110:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.874, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 2, Question Quality: 3
    Human Comments: Poor Context
    User Input: Can you describe what Image Generation is?...
    Response: Image Generation is a topic within the broader context of Artificial Intelligence....

  Sample 111:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.747, Question Quality: 5.000
    Human scores - Faithfulness: 2, Response Relevancy: 3, Question Quality: 2
    Human Comments: poor context
    User Input: Considering the provided context, what is the relationship between Generative AI and the other liste...
    Response: Within the context provided, Generative AI is presented as a distinct topic, alongside others such
a...

  Sample 113:
    RAGAS scores - Faithfulness: 1.000, Answer Relevancy: 0.969, Question Quality: 5.000
    Human scores - Faithfulness: 5, Response Relevancy: 5, Question Quality: 3
    Human Comments: poor context
    User Input: What are the topics covered in the context related to Artificial Intelligence?...
    Response: The context covers the following topics related to Artificial Intelligence: Image Generation, ChatGP...

Samples excluded by human score-based criteria but NOT explicitly marked: 0

=== Dataset Processing Summary ===
Original samples: 120
Explicitly excluded by human: 23
RAGAS low scores (<=60%) but kept due to human evaluation: 15
Automatically excluded by human metrics: 23
Total excluded (final): 23
Final cleaned dataset size: 97
Retention rate: 80.8%

=== Detailed Exclusion Breakdown ===
Exclusion by specific criteria:
  - Human explicit exclusion only: 23
  - RAGAS low scores (<=60%) but kept due to human evaluation: 4
  - Human score-based exclusion only: 0
  - Human explicit exclusion (RAGAS exclusion disabled): 23
  - Both human explicit AND human score-based exclusion: 23
  - RAGAS exclusion disabled - no samples excluded by RAGAS criteria
Cleaned dataset saved to: data\testsets\human_eval\testset_human_eval_cleaned.csv

=== Correlation Analysis ===
Faithfulness: 119 samples
Response Relevancy: 120 samples
Question Quality: 120 samples
Spearman correlation (RAGAS vs Human Faithfulness): 0.447 (p=0.000)
Spearman correlation (RAGAS vs Human Response Relevancy): 0.434 (p=0.000)
Spearman correlation (RAGAS vs Human Question Quality): 0.323 (p=0.000)

=== Statistical Significance ===
Faithfulness: r=0.447, p=0.000 (significant at α=0.05)
Response Relevancy: r=0.434, p=0.000 (significant at α=0.05)
Question Quality: r=0.323, p=0.000 (significant at α=0.05)

Generating correlation plots...
Faithfulness
(RAGAS vs Human): 119 samples plotted (from 119 total)
Response Relevancy
(RAGAS vs Human): 120 samples plotted (from 120 total)
Question Quality
(RAGAS vs Human): 120 samples plotted (from 120 total)

Combined correlation analysis:
- Faithfulness: r=0.447 (p=0.000)
- Response Relevancy: r=0.434 (p=0.000)
- Question Quality: r=0.323 (p=0.000)

=== Low Correlation Analysis ===

Top 5 samples with largest deviations in Faithfulness:
  1. Sample 111:
     RAGAS: 1.000, Human: 2, Predicted: 4.74, Deviation: 2.74
     User Input: Considering the provided context, what is the relationship between Generative AI...
     Response: Within the context provided, Generative AI is presented as a distinct topic, alo...

  2. Sample 79:
     RAGAS: 1.000, Human: 2, Predicted: 4.74, Deviation: 2.74
     User Input: Create a new plan using Object-Oriented Programming, yeah?...
     Response: I can't create a plan using Object-Oriented Programming based on this informatio...

  3. Sample 86:
     RAGAS: 1.000, Human: 2, Predicted: 4.74, Deviation: 2.74
     User Input: WHAT ARE indexes, and WHERE ARE THEY DISCUSSED in this stuff?...
     Response: Indexes are mentioned in the context of a lecture. The lecture is titled "Lectur...

  4. Sample 74:
     RAGAS: 1.000, Human: 2, Predicted: 4.74, Deviation: 2.74
     User Input: What is style?...
     Response: Style is a section in the provided context....

  5. Sample 48:
     RAGAS: 1.000, Human: 2, Predicted: 4.74, Deviation: 2.74
     User Input: How can we use the tool kit to write code?...
     Response: The tool kit includes big O, which represents the upper bound, and Omega, which ...


Top 5 samples with largest deviations in Response Relevancy:
  1. Sample 107:
     RAGAS: 0.886, Human: 2, Predicted: 4.62, Deviation: 2.62
     User Input: How can I implement Forms within a Flask web application, based on the concepts ...
     Response: While this lecture introduces Forms within the context of Flask web applications...

  2. Sample 110:
     RAGAS: 0.874, Human: 2, Predicted: 4.59, Deviation: 2.59
     User Input: Can you describe what Image Generation is?...
     Response: Image Generation is a topic within the broader context of Artificial Intelligenc...

  3. Sample 91:
     RAGAS: 0.844, Human: 2, Predicted: 4.50, Deviation: 2.50
     User Input: How effective is the deadline of 2024-12-31T23:59:00-05:00 for completing the pr...
     Response: The deadline for completing the problem set is 2024-12-31T23:59:00-05:00. The ef...

  4. Sample 15:
     RAGAS: 0.811, Human: 2, Predicted: 4.40, Deviation: 2.40
     User Input: What are conditionals?...
     Response: Conditionals are mentioned in the context of learning how to use variables, cond...

  5. Sample 74:
     RAGAS: 0.793, Human: 2, Predicted: 4.35, Deviation: 2.35
     User Input: What is style?...
     Response: Style is a section in the provided context....


Top 5 samples with largest deviations in Question Quality:
  1. Sample 70:
     RAGAS: 5.000, Human: 1, Predicted: 4.59, Deviation: 3.59
     User Input: I'm designing a new system for submitting assignments. Can you formulate a plan,...
     Response: To ensure successful submissions, let's formulate a plan based on the provided i...

  2. Sample 48:
     RAGAS: 5.000, Human: 1, Predicted: 4.59, Deviation: 3.59
     User Input: How can we use the tool kit to write code?...
     Response: The tool kit includes big O, which represents the upper bound, and Omega, which ...

  3. Sample 91:
     RAGAS: 5.000, Human: 2, Predicted: 4.59, Deviation: 2.59
     User Input: How effective is the deadline of 2024-12-31T23:59:00-05:00 for completing the pr...
     Response: The deadline for completing the problem set is 2024-12-31T23:59:00-05:00. The ef...

  4. Sample 111:
     RAGAS: 5.000, Human: 2, Predicted: 4.59, Deviation: 2.59
     User Input: Considering the provided context, what is the relationship between Generative AI...
     Response: Within the context provided, Generative AI is presented as a distinct topic, alo...

  5. Sample 71:
     RAGAS: 5.000, Human: 2, Predicted: 4.59, Deviation: 2.59
     User Input: Considering the use of a sequence of DNA in forensic investigations, formulate a...
     Response: To create a new method for identifying individuals using DNA, we can build upon ...

=== Extreme Score Differences Analysis ===

Top 5 samples with extreme score differences in Faithfulness:
  1. Sample 111:
     RAGAS: 1.000, Human: 2, Normalized Difference: 0.000
     User Input: Considering the provided context, what is the relationship between Generative AI...
     Response: Within the context provided, Generative AI is presented as a distinct topic, alo...

  2. Sample 79:
     RAGAS: 1.000, Human: 2, Normalized Difference: 0.750
     User Input: Create a new plan using Object-Oriented Programming, yeah?...
     Response: I can't create a plan using Object-Oriented Programming based on this informatio...

  3. Sample 86:
     RAGAS: 1.000, Human: 2, Normalized Difference: 0.750
     User Input: WHAT ARE indexes, and WHERE ARE THEY DISCUSSED in this stuff?...
     Response: Indexes are mentioned in the context of a lecture. The lecture is titled "Lectur...

  4. Sample 74:
     RAGAS: 1.000, Human: 2, Normalized Difference: 0.750
     User Input: What is style?...
     Response: Style is a section in the provided context....

  5. Sample 48:
     RAGAS: 1.000, Human: 2, Normalized Difference: 0.750
     User Input: How can we use the tool kit to write code?...
     Response: The tool kit includes big O, which represents the upper bound, and Omega, which ...


Top 5 samples with extreme score differences in Response Relevancy:
  1. Sample 107:
     RAGAS: 0.886, Human: 2, Normalized Difference: 0.636
     User Input: How can I implement Forms within a Flask web application, based on the concepts ...
     Response: While this lecture introduces Forms within the context of Flask web applications...

  2. Sample 110:
     RAGAS: 0.874, Human: 2, Normalized Difference: 0.624
     User Input: Can you describe what Image Generation is?...
     Response: Image Generation is a topic within the broader context of Artificial Intelligenc...

  3. Sample 91:
     RAGAS: 0.844, Human: 2, Normalized Difference: 0.594
     User Input: How effective is the deadline of 2024-12-31T23:59:00-05:00 for completing the pr...
     Response: The deadline for completing the problem set is 2024-12-31T23:59:00-05:00. The ef...

  4. Sample 15:
     RAGAS: 0.811, Human: 2, Normalized Difference: 0.561
     User Input: What are conditionals?...
     Response: Conditionals are mentioned in the context of learning how to use variables, cond...

  5. Sample 74:
     RAGAS: 0.793, Human: 2, Normalized Difference: 0.543
     User Input: What is style?...
     Response: Style is a section in the provided context....


Top 5 samples with extreme score differences in Question Quality:
  1. Sample 70:
     RAGAS: 5.000, Human: 1, Normalized Difference: 4.000
     User Input: I'm designing a new system for submitting assignments. Can you formulate a plan,...
     Response: To ensure successful submissions, let's formulate a plan based on the provided i...

  2. Sample 48:
     RAGAS: 5.000, Human: 1, Normalized Difference: 4.000
     User Input: How can we use the tool kit to write code?...
     Response: The tool kit includes big O, which represents the upper bound, and Omega, which ...

  3. Sample 91:
     RAGAS: 5.000, Human: 2, Normalized Difference: 3.000
     User Input: How effective is the deadline of 2024-12-31T23:59:00-05:00 for completing the pr...
     Response: The deadline for completing the problem set is 2024-12-31T23:59:00-05:00. The ef...

  4. Sample 111:
     RAGAS: 5.000, Human: 2, Normalized Difference: 3.000
     User Input: Considering the provided context, what is the relationship between Generative AI...
     Response: Within the context provided, Generative AI is presented as a distinct topic, alo...

  5. Sample 71:
     RAGAS: 5.000, Human: 2, Normalized Difference: 3.000
     User Input: Considering the use of a sequence of DNA in forensic investigations, formulate a...
     Response: To create a new method for identifying individuals using DNA, we can build upon ...


=== Contingency Analysis ===
Contingency Table (Human Explicit Exclusion vs. RAGAS Low Scores):
Any RAGAS Metric Below Threshold  False  True
Explicitly Excluded by Human
False                                93      4
True                                 12     11
Chi-square test: χ²=28.592, p=0.000, df=1
Significant association between human exclusion and RAGAS scores

Contingency Chart Analysis:
- Samples NOT excluded by human: 97
- Samples EXCLUDED by human: 23
- RAGAS missed 12 problems that humans detected
- RAGAS correctly flagged 11 problems
- RAGAS agreement rate: 47.8%

=== Processing Complete ===

```
