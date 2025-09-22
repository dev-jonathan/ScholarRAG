from ragas.testset import TestsetGenerator
from .personas import create_personas
from .query_distribution_factory import create_query_distribution
from ragas.run_config import RunConfig


def generate_questions(kg, llm, embedding_model, testset_size, output_csv):
    personas = create_personas()
    query_distribution = create_query_distribution(llm)
    generator = TestsetGenerator(
        llm=llm,
        embedding_model=embedding_model,
        knowledge_graph=kg,
        persona_list=personas,
    )
    run_config = RunConfig(
        max_workers=1,
        timeout=60,
        max_retries=5,
        max_wait=30,
        log_tenacity=True,
    )
    testset = generator.generate(
        testset_size=testset_size,
        query_distribution=query_distribution,
        run_config=run_config,
    )
    df_pandas = testset.to_pandas()
    df_pandas.to_csv(output_csv, index=False)
    return df_pandas
