from ragas.testset.synthesizers.single_hop.specific import (
    SingleHopSpecificQuerySynthesizer,
)

# from ragas.testset.synthesizers.multi_hop import (
#     MultiHopAbstractQuerySynthesizer,
#     MultiHopSpecificQuerySynthesizer,
# )

# from custom_single_hop import CustomSingleHopSynthesizer


def create_query_distribution(llm):
    query_distribution = [
        (
            SingleHopSpecificQuerySynthesizer(
                llm=llm,
                property_name="keyphrases",
            ),
            1.0,
        ),
        # Examples of adding more synthesizers with weights
        # (
        #     SingleHopSpecificQuerySynthesizer(
        #         llm=llm,
        #         property_name="headlines",
        #     ),
        #     0.3,
        # ),
        # (
        #     SingleHopSpecificQuerySynthesizer(
        #         llm=llm,
        #         property_name="keyphrases",
        #     ),
        #     0.7,
        # ),
        # (
        #     MultiHopAbstractQuerySynthesizer(
        #         llm=llm,
        #     ),
        #     0.35,
        # ),
        # (
        #     MultiHopSpecificQuerySynthesizer(
        #         llm=llm,
        #     ),
        #     0.35,
        # ),
    ]
    return query_distribution
