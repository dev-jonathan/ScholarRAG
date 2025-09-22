# from ragas.testset.synthesizers.single_hop import SingleHopQuerySynthesizer
# from ragas.testset.synthesizers.prompts import (
#     ThemesPersonasInput,
#     ThemesPersonasMatchingPrompt,
# )
# from dataclasses import dataclass


# @dataclass
# class CustomSingleHopSynthesizer(SingleHopQuerySynthesizer):
#     theme_persona_matching_prompt = ThemesPersonasMatchingPrompt()

#     async def _generate_scenarios(self, n, knowledge_graph, persona_list, callbacks):
#         property_name = "keyphrases"  # ou "headlines", etc.
#         styles = ["Web search like queries", "Conversational", "Academic"]  # customize!
#         lengths = ["short", "medium", "long"]

#         nodes = [
#             node for node in knowledge_graph.nodes if node.get_property(property_name)
#         ]
#         number_of_samples_per_node = max(1, n // len(nodes))

#         scenarios = []
#         for node in nodes:
#             if len(scenarios) >= n:
#                 break
#             themes = node.properties.get(property_name, [""])
#             prompt_input = ThemesPersonasInput(themes=themes, personas=persona_list)
#             persona_concepts = await self.theme_persona_matching_prompt.generate(
#                 data=prompt_input, llm=self.llm, callbacks=callbacks
#             )
#             # Aqui você gera todas as combinações possíveis
#             for style in styles:
#                 for length in lengths:
#                     base_scenarios = self.prepare_combinations(
#                         node,
#                         themes,
#                         personas=persona_list,
#                         persona_concepts=persona_concepts.mapping,
#                         style=style,
#                         length=length,
#                     )
#                     scenarios.extend(
#                         self.sample_combinations(
#                             base_scenarios, number_of_samples_per_node
#                         )
#                     )
#         return scenarios


from ragas.testset.synthesizers.single_hop.specific import (
    SingleHopSpecificQuerySynthesizer,
)
from ragas.testset.synthesizers.base import QueryStyle, QueryLength


class CustomSingleHopSynthesizer(SingleHopSpecificQuerySynthesizer):
    def prepare_combinations(self, node, terms, personas, persona_concepts):
        sample = super().prepare_combinations(node, terms, personas, persona_concepts)[
            0
        ]
        sample["styles"] = [
            QueryStyle.WEB_SEARCH_LIKE,
            QueryStyle.PERFECT_GRAMMAR,
            QueryStyle.POOR_GRAMMAR,
        ]
        sample["lengths"] = [QueryLength.SHORT, QueryLength.MEDIUM, QueryLength.LONG]
        return [sample]
