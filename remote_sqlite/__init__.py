class RemoteSqlite:
    def __init__(self, fspath, always_download=False):
        import sqlite3
        self.fspath = fspath
        self.localpath = self.pull(fspath, always_download)
        self.con = sqlite3.connect(self.localpath, detect_types=sqlite3.PARSE_DECLTYPES)
        self.con.row_factory = sqlite3.Row
    def __del__(self):
        self.con.close()
    def pull(self, fspath, always_download=False):
        import fs
        queryparams = self.get_pathurlparameters(fspath)
        remotefs = fs.open_fs(fs.path.dirname(fspath)+queryparams)
        tempdir = self.get_tempdirectory()
        tempfs = fs.open_fs(tempdir,create=True)
        filename = fs.path.basename(fspath).split('?')[0]
        if always_download:
            fs.copy.copy_file(remotefs, filename, tempfs, filename)
        else:
            fs.copy.copy_file_if_newer(remotefs, filename, tempfs, filename)
        return tempfs.getsyspath(filename)
    def push(self, fspath, always_upload=False):
        import fs
        queryparams = self.get_pathurlparameters(fspath)
        remotefs = fs.open_fs(fs.path.dirname(fspath)+queryparams)
        tempdir = self.get_tempdirectory()
        tempfs = fs.open_fs(tempdir,create=True)
        filename = fs.path.basename(fspath).split('?')[0]
        if always_upload:
            fs.copy.copy_file(tempfs, filename, remotefs, filename)
        else:
            fs.copy.copy_file_if_newer(tempfs, filename, remotefs, filename)
        return fspath
    def get_tempdirectory(self):
        import os
        from pathlib import Path
        os_tempdir = os.environ.get('TEMP')
        if os_tempdir:
            tempdir = (Path(os.environ.get('TEMP')) / "RemoteSqlite").as_posix()
        else:
            tempdir = '/tmp/RemoteSqlite/'
        tempdir_fspath = 'osfs://{temp_dir}'.format(temp_dir=tempdir)
        return tempdir_fspath            
    def get_pathurlparameters(self, fspath):
        from urllib.parse import parse_qs, urlparse
        querystring = parse_qs(urlparse(fspath).query)
        queryparams = ''
        if querystring:
            for key in querystring:
                if queryparams:
                    queryparams+= "&{querykey}={queryvalue}".format(querykey=key, queryvalue=querystring[key][0])
                else:
                    queryparams+= "?{querykey}={queryvalue}".format(querykey=key, queryvalue=querystring[key][0])
        return queryparams
    def get_count(self, tbl_name):
        return self.select(f"""SELECT COUNT(*) FROM `{tbl_name}`""")[0]['COUNT(*)']
    def get_counts(self):
        tables = self.select("""SELECT tbl_name FROM sqlite_master WHERE type='table'""")
        return [{t['tbl_name']: self.get_count(t['tbl_name'])} for t in tables]
    def select(self, select_statement='SELECT * FROM sqlite_master'):
        cur = self.con.cursor()
        cur.execute(select_statement)
        records = [dict(row) for row in cur.fetchall()]
        return records
    def insert(self, tbl_name, records):
        cur = self.con.cursor()
        for record in records:
            field_names = ','.join([f'"{k}"' for k in record.keys()])
            placeholders = ','.join(['?' for k in record.keys()])
            insert_statement = f'INSERT INTO "{tbl_name}" ({field_names}) VALUES ({placeholders})'
            values = tuple(record.values())
            cur.execute(insert_statement, values)
        self.con.commit()
    def generate_create_table(self, tbl_name, records):
        columns = ', '.join([f'"{k}" TEXT' for k in records[0].keys()])
        return f'CREATE TABLE "{tbl_name}" ({columns})'
