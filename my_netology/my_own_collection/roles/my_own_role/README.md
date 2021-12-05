Role Name
=========

Роль для создания и заполнения файла

Requirements
------------

None

Role Variables
--------------

| Variable name | Default | Description |
|-----------------------|----------|-------------------------|
| default_path | "tmp/1.txt" | Путь для файла |
| dafault_content | "hello world" | Содержимое файла |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: my_own_role }

License
-------

BSD

Author Information
------------------

Olga Ivanova, devops-10
