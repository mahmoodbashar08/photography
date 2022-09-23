CREATE TABLE IF NOT EXISTS photos (
	id integer primary key,
   	file_name VARCHAR(255) NOT NULL,
	file_download_id VARCHAR(255) NOT NULL,
	file_path VARCHAR(400) NOT NULL,
          owner_id INT NOT NULL DEFAULT 0,
          is_deleted BOOLEAN DEFAULT false 
) ;