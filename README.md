<div id="notebook" class="border-box-sizing" tabindex="-1">

<div id="notebook-container" class="container">

<div class="cell border-box-sizing text_cell rendered">

<div class="prompt input_prompt">

</div>

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

RemoteSqlite[¶](#RemoteSqlite){.anchor-link} {#RemoteSqlite}
============================================

</div>

</div>

</div>

<div class="cell border-box-sizing text_cell rendered">

<div class="prompt input_prompt">

</div>

<div class="inner_cell">

<div class="text_cell_render border-box-sizing rendered_html">

RemoteSqlite is a way to easily access a remote Sqlite database and
perform queries, including SELECT and INSERT operations

The remote database is referenced through a
[PyFilesystem2](https://docs.pyfilesystem.org/en/latest/) url, such as:

-   `osfs://path/to/file`
-   `s3://path/to/file`

You can perform `pull` and `push` operations that transfer the database
to a local temp directory

See below for examples of how to use

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[1\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    from remote_sqlite import RemoteSqlite
    db = RemoteSqlite('osfs:///Users/vbalasubramaniam/Downloads/Northwind_large.sqlite', always_download=True)
    db.get_counts()

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[1\]:

</div>

<div class="output_text output_subarea output_execute_result">

    [{'Employee': 9},
     {'Category': 8},
     {'Customer': 91},
     {'Shipper': 3},
     {'Supplier': 29},
     {'Order': 16818},
     {'Product': 77},
     {'OrderDetail': 621883},
     {'CustomerCustomerDemo': 0},
     {'CustomerDemographic': 0},
     {'Region': 4},
     {'Territory': 53},
     {'EmployeeTerritory': 49},
     {'posts': 0},
     {'posts_data': 2},
     {'posts_idx': 0},
     {'posts_content': 0},
     {'posts_docsize': 0},
     {'posts_config': 1},
     {'order_search': 16818},
     {'order_search_data': 226},
     {'order_search_idx': 474},
     {'order_search_content': 16818},
     {'order_search_docsize': 16818},
     {'order_search_config': 1}]

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[2\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.select("""SELECT * FROM Shipper""")

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[2\]:

</div>

<div class="output_text output_subarea output_execute_result">

    [{'Id': 1, 'CompanyName': 'Speedy Express', 'Phone': '(503) 555-9831'},
     {'Id': 2, 'CompanyName': 'United Package', 'Phone': '(503) 555-3199'},
     {'Id': 3, 'CompanyName': 'Federal Shipping', 'Phone': '(503) 555-9931'}]

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[3\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    new_records = [{'Id': 4, 'CompanyName': 'Speedy Express', 'Phone': '(503) 555-9831'},
     {'Id': 5, 'CompanyName': 'United Package', 'Phone': '(503) 555-3199'},
     {'Id': 6, 'CompanyName': 'Federal Shipping', 'Phone': '(503) 555-9931'}]

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[4\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.insert('Shipper', new_records)

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[5\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.con.execute('DELETE FROM Shipper WHERE Id >3')

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[5\]:

</div>

<div class="output_text output_subarea output_execute_result">

    <sqlite3.Cursor at 0x10535bab0>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[6\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    create_statement = """CREATE TABLE test (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      t TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )"""

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[7\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.con.execute(create_statement)

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[7\]:

</div>

<div class="output_text output_subarea output_execute_result">

    <sqlite3.Cursor at 0x1053a43b0>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[8\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.insert('test', [{'name': 'John'},{'name':'Matt'}])

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[9\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.select('SELECT * FROM test')

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[9\]:

</div>

<div class="output_text output_subarea output_execute_result">

    [{'id': 1, 'name': 'John', 't': datetime.datetime(2020, 3, 7, 22, 12, 45)},
     {'id': 2, 'name': 'Matt', 't': datetime.datetime(2020, 3, 7, 22, 12, 45)}]

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[10\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.con.execute('DROP TABLE test')

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[10\]:

</div>

<div class="output_text output_subarea output_execute_result">

    <sqlite3.Cursor at 0x1053a42d0>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[11\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.generate_create_table('Shipper2', [{'Id': 1, 'CompanyName': 'Speedy Express', 'Phone': '(503) 555-9831'},
     {'Id': 2, 'CompanyName': 'United Package', 'Phone': '(503) 555-3199'},
     {'Id': 3, 'CompanyName': 'Federal Shipping', 'Phone': '(503) 555-9931'}])

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[11\]:

</div>

<div class="output_text output_subarea output_execute_result">

    'CREATE TABLE "Shipper2" ("Id" TEXT, "CompanyName" TEXT, "Phone" TEXT)'

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[12\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.con.execute('CREATE TABLE "Shipper2" ("Id" TEXT, "CompanyName" TEXT, "Phone" TEXT)')

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[12\]:

</div>

<div class="output_text output_subarea output_execute_result">

    <sqlite3.Cursor at 0x1053a4340>

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[13\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.insert('Shipper2', [{'Id': 1, 'CompanyName': 'Speedy Express', 'Phone': '(503) 555-9831'},
     {'Id': 2, 'CompanyName': 'United Package', 'Phone': '(503) 555-3199'},
     {'Id': 3, 'CompanyName': 'Federal Shipping', 'Phone': '(503) 555-9931'}])

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[14\]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

    db.select('SELECT * FROM Shipper2')

</div>

</div>

</div>

</div>

<div class="output_wrapper">

<div class="output">

<div class="output_area">

<div class="prompt output_prompt">

Out\[14\]:

</div>

<div class="output_text output_subarea output_execute_result">

    [{'Id': '1', 'CompanyName': 'Speedy Express', 'Phone': '(503) 555-9831'},
     {'Id': '2', 'CompanyName': 'United Package', 'Phone': '(503) 555-3199'},
     {'Id': '3', 'CompanyName': 'Federal Shipping', 'Phone': '(503) 555-9931'}]

</div>

</div>

</div>

</div>

</div>

<div class="cell border-box-sizing code_cell rendered">

<div class="input">

<div class="prompt input_prompt">

In \[ \]:

</div>

<div class="inner_cell">

<div class="input_area">

<div class="highlight hl-ipython3">

     

</div>

</div>

</div>

</div>

</div>

</div>

</div>
