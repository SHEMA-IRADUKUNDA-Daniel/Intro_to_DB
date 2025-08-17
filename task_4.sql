-- Print full description of the table 'books'
SELECT COLUMN_NAME AS 'Column',
      COLUMN_TYPE AS 'Type',
      IS_NULLABLE AS 'Nullable',
      COLUMN_KEY AS 'Key',
      COLUMN_DEFAULT AS 'Default',
      EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()  -- Uses the current database
  AND TABLE_NAME = 'books';
