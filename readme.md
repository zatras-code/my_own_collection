# my_own_namespace.yandex_cloud_elk

Учебная Ansible Collection.

## Состав

### Module: my_own_module

Создаёт или обновляет текстовый файл на удалённом хосте.

### Role: my_role

Role-обёртка над модулем с defaults-переменными.

---

# Модуль my_own_module

## Параметры

| Parameter | Type | Required | Description |
|---|---|---|---|
| path | str | yes | Абсолютный путь к файлу |
| content | str | yes | Содержимое файла |

---

## Пример использования

```yaml
- name: Create file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/hello.txt
    content: "hello world"
````

---

# Role my_role

## Defaults

```yaml
module_path: "/tmp/hello.txt"
module_content: "hello from role"
```

---

# Playbook example

```yaml
---
- name: Test role
  hosts: localhost
  connection: local
  gather_facts: false

  roles:
    - role: my_own_namespace.yandex_cloud_elk.my_role
```

---

# Build collection

```bash
ansible-galaxy collection build
```

---

# Install collection

```bash
ansible-galaxy collection install my_own_namespace-yandex_cloud_elk-1.0.0.tar.gz
```

---

# Run playbook

```bash
ansible-playbook playbook.yml
```

```
```
