*запуск миграций через liquibase:*
```
docker run --rm -w /app -v <path-to-repository>/migrations:/app --network "gptnotes-network" liquibase/liquibase:4.19.0 update --changelog-file=changelog.xml --url=jdbc:postgresql://172.17.0.1:5432/postgres --username=postgres --password=postgres
```
