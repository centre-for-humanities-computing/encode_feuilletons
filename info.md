# setup
- run from the command line:

pip install typer[all] loguru tqdm pandas datasets sentence-transformers
cd PascaleFrederikkeNikolineFeldkampMoreira#6762/feuilleton_novels

# Embeddings

- To get them, run: 
python src/process_articles.py --input-csv cleaned_feuilleton.csv --output-dir data/raw

# Pooling

- run: 
python src/pool_embeddings.py --input-ds <path_to_raw_embeddings_directory> --output-ds <path_to_output_directory>


python src/mean_pooling.py data/raw/emb__intfloat__multilingual-e5-large_597369d1 data/pooled


Final embeddings are the pooled version