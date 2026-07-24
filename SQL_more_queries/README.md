# SQL More Queries

This directory contains SQL scripts that demonstrate MySQL user privileges, database permissions, and advanced SQL queries.

## Files

### 0-privileges.sql

Lists all privileges granted to the MySQL users:
- `user_0d_1`@`localhost`
- `user_0d_2`@`localhost`

The script uses `SHOW GRANTS` to display the permissions assigned to each user.

## Usage

Run the script using:

```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
