# setup
- run from the command line:
pip install typer[all] loguru tqdm pandas datasets sentence-transformers einops
cd enocde_feuilletons

# Embeddings

Script runs one at a time -- or in batches -- and saves the (raw) output in data/raw

- To get embeddings, run: 
python src/process_articles.py --input-csv <path> --output-dir data/raw --model-name <comma-seperated-list>

the models used in our former runs were: 
- intfloat/multilingual-e5-large
- MiMe-MeMo/MeMo-BERT-03
- jinaai/jina-embeddings-v3
- Lajavaness/bilingual-embedding-large
- OrdalieTech/Solon-embeddings-large-0.1

# 2025-09-25 Embeddings

python src/process_articles.py \
    --input-csv data/20250925-0947_cleaned_annotations.csv \
    --output-dir data/raw \
    --model-name "intfloat/multilingual-e5-large,MiMe-MeMo/MeMo-BERT-03,jinaai/jina-embeddings-v3,JohanHeinsen/Old_News_Segmentation_SBERT_V0.1,BAAI/bge-m3,google/embeddinggemma-300m"


the models used in our runs were: 
- intfloat/multilingual-e5-large
- MiMe-MeMo/MeMo-BERT-03
- jinaai/jina-embeddings-v3
- JohanHeinsen/Old_News_Segmentation_SBERT_V0.1
- BAAI/bge-m3
- google/embeddinggemma-300m


# Pooling (to get the final embeddings)

run (specifying output dir and input embeddings)(each model tested below)
python src/mean_pooling.py data/raw/emb__intfloat__multilingual-e5-large_597369d1 data/pooled/e-5/
python src/mean_pooling.py data/raw/emb__MiMe-MeMo__MeMo-BERT-03_597369d1 data/pooled/memo/
python src/mean_pooling.py data/raw/emb__jinaai__jina-embeddings-v3_597369d1 data/pooled/jina/
python src/mean_pooling.py data/raw/emb__google__embeddinggemma-300m_597369d1 data/pooled/gemma/
python src/mean_pooling.py data/raw/emb__BAAI__bge-m3_597369d1 data/pooled/bge/
python src/mean_pooling.py data/raw/emb__JohanHeinsen__Old_News_Segmentation_SBERT_V0.1_597369d1 data/pooled/oldnews/


Script runs one at a time and saves the (pooled) output in data/pooled/<nickname>
