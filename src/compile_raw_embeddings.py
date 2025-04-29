# %%
# 
from datasets import Dataset

# %%

processed_articles = []
all_processed_articles = []
chunk_size = 1000

for row in tqdm(df.itertuples(), total=len(df), desc="Processing articles"):
    article_id = row.article_id
    text = row.text

    # Preprocessing and inference steps here...
    # Add processed article to the current chunk
    processed_articles.append({
        "article_id": article_id,
        "text": text,
        # Add any other fields or transformations here
    })
    
    # Save data in chunks
    if len(processed_articles) >= chunk_size:
        dataset = Dataset.from_list(processed_articles)
        all_processed_articles.append(dataset)  # Append chunk to all_processed_articles
        logger.info(f"Saved batch {len(all_processed_articles)} to disk.")
        processed_articles = []  # Reset after saving

# Save any remaining data
if processed_articles:
    dataset = Dataset.from_list(processed_articles)
    all_processed_articles.append(dataset)  # Append last chunk to all_processed_articles
    logger.info(f"Saved final batch to disk.")

# Combine all chunks into one dataset
final_dataset = Dataset.concatenate(*all_processed_articles)  # Concatenate all chunks

# Save the final combined dataset
final_dataset.save_to_disk(output_path / "final_combined_dataset")
logger.info(f"Saved final combined dataset to {output_path}")

print(f"Saved processed dataset to {output_path}")