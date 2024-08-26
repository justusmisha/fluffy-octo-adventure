from corrector.base_corrector import DatabaseSynchronizer

if __name__ == "__main__":
    source_db_url = "postgresql+psycopg2://postgres:postgres@localhost:5432/source_db"  # Образец
    target_db_url = "postgresql+psycopg2://postgres:postgres@localhost:5432/target_db"  # Корректируемая

    synchronizer = DatabaseSynchronizer(source_db_url, target_db_url)
    synchronizer.synchronize()
