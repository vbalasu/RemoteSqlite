jupyter nbconvert RemoteSqlite.ipynb --to html
pandoc -o README.md RemoteSqlite.html
rm RemoteSqlite.html
