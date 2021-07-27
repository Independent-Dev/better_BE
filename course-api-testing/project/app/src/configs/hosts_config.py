API_HOST = {
    'test': 'http://mystore.local/wp-json/wc/v3/'
}

WOO_API_HOST = {
    'test': 'http://mystore.local'
}

DB_HOST = {
    'machine1': {
        "test": {"host": "http://mystore.local/",
                 "database": "local",
                 "table_prefix": "wp_",
                 "socket": "/Users/jonathan/Library/Application Support/Local/run/8Tx4d8szF/mysql/mysqld.sock",
                 "port": 3306},
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
    },
    'docker': {
        "test": {
            "host": "host.docker.internal",
            "database": "wp398",
            "table_prefix": "wp2p_",
            "socket": None,
            "port": 3306
        },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
    },
    'machine2': {
        "test": {"host": "localhost",
                 "database": "local",
                 "table_prefix": "wp_",
                 "socket": "/Users/akinfu/Library/Application Support/Local/run/d84nqkpSm/mysql/mysqld.sock",
                 "port": 3306
                 },
        "dev": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
        "prod": {
            "host": "host.docker.internal",
            "database": "local",
            "table_prefix": "wp_",
            "socket": None,
            "port": 3306
        },
    }
}
