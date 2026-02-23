from yandex_ai_studio_sdk.search_indexes import (
    HybridSearchIndexType,
    ReciprocalRankFusionIndexCombinationStrategy,
    StaticIndexChunkingStrategy,
)

from config import sdk


def create_index(files: list) -> str:
    operation = sdk.search_indexes.create_deferred(
        files,
        index_type=HybridSearchIndexType(
            chunking_strategy=StaticIndexChunkingStrategy(
                max_chunk_size_tokens=1000,
                chunk_overlap_tokens=100,
            ),
            combination_strategy=ReciprocalRankFusionIndexCombinationStrategy(),
        ),
    )
    index = operation.wait()
    return index.id


def get_index(index_id: str):
    return sdk.search_indexes.get(index_id)
