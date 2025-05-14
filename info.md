# setup
- run from the command line:

pip install typer[all] loguru tqdm pandas datasets sentence-transformers einops
cd PascaleFrederikkeNikolineFeldkampMoreira#6762/feuilleton_novels

# Embeddings

- To get them, run: 
python src/process_articles.py --input-csv cleaned_feuilleton.csv --output-dir data/raw

# Pooling

run (specifying output dir and input embeddings)(each model tested below)
- python src/mean_pooling.py data/raw/emb__intfloat__multilingual-e5-large_597369d1 data/pooled/e-5/
- python src/mean_pooling.py data/raw/emb__MiMe-MeMo__MeMo-BERT-03_597369d1 data/pooled/memo/
- python src/mean_pooling.py data/raw/emb__jinaai__jina-embeddings-v3_597369d1 data/pooled/jina/
- python src/mean_pooling.py data/raw/emb__OrdalieTech__Solon-embeddings-large-0.1_597369d1 data/pooled/solon/

Final embeddings are the pooled version