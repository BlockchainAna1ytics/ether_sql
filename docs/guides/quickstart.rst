Quickstart
==========
This quickstart is a follow up of the `Installation <../installation>`_ instructions.

Syncing the blockchain
----------------------

The easiest method to start syncing the sql database to the connected node is using the following command.

.. code:: shell

  $ ether_sql scrape_data

This command will check the last block number in your sql database and node and start pushing the remaining blocks into your sql server.
To sync blocks in a particular range use the options :code:`--start_block_number` or :code:`--end_block_number` or use the :code:`--help` option to know more about the above command.

.. code:: shell

  $ ether_sql scrape_data --help

To get the current status of sync progress you can use the following command to get the highest block number in the sql.

.. code:: shell

  $ ether_sql sql blocknumber

For more details refer to the API doc on `CLI's <../api/cli>`_.

Connecting to Postgresql
------------------------
Once the database is filled with some blocks you can connect to the psql database using the following command.

.. code:: shell

  $ psql ether_sql

Once connected to the Postgresql you can start quickly querying the database.
Below is a simple code to get the maximum block number in the sql database.

.. code:: sql

  ether_sql=# SELECT max(block_number) from blocks;

More sample sql examples and their results are available in `sql examples <basic-sql>`_.
TO know more details about the different tables and their columns refer to `sql table api docs <../api/models>`_.
