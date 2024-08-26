from sqlalchemy import create_engine, MetaData, Table, inspect
from sqlalchemy.schema import CreateTable, DropTable
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base

from logger.app_logger import logger

Base = declarative_base()


class DatabaseSynchronizer:
    def __init__(self, source_db_url, target_db_url):
        self.source_engine = create_engine(source_db_url)
        self.target_engine = create_engine(target_db_url)
        self.source_metadata = MetaData()
        self.target_metadata = MetaData()
        self.source_metadata.reflect(bind=self.source_engine)
        self.target_metadata.reflect(bind=self.target_engine)

    def get_missing_tables(self):
        source_tables = set(self.source_metadata.tables.keys())
        target_tables = set(self.target_metadata.tables.keys())
        missing_tables = source_tables - target_tables
        return missing_tables

    def get_extra_tables(self):
        source_tables = set(self.source_metadata.tables.keys())
        target_tables = set(self.target_metadata.tables.keys())
        extra_tables = target_tables - source_tables
        return extra_tables

    def create_missing_tables(self):
        missing_tables = self.get_missing_tables()
        with self.target_engine.connect() as connection:
            for table_name in missing_tables:
                table = self.source_metadata.tables[table_name]
                try:
                    connection.execute(CreateTable(table))
                    logger.info(f"Created table: {table_name}")
                    connection.commit()
                except Exception as e:
                    logger.error(f"Error creating table {table_name}: {e}")

    def drop_extra_tables(self):
        extra_tables = self.get_extra_tables()
        with self.target_engine.connect() as connection:
            for table_name in extra_tables:
                table = self.target_metadata.tables[table_name]
                try:
                    connection.execute(DropTable(table))
                    logger.info(f"Dropped table: {table_name}")
                    connection.commit()
                except Exception as e:
                    logger.error(f"Error dropping table {table_name}: {e}")

    def synchronize(self):
        logger.info("Starting synchronization...")
        self.create_missing_tables()
        self.drop_extra_tables()
        logger.info("Synchronization complete.")
