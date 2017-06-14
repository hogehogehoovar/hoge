# README

## DATABASE_DESIGN

### テーブル設計

- 一つのカラムが一つのテーブルを示している
- userが位置情報を送信->users_events作成
- アルゴリズムで仮グループを作成->users_groups作成
- userが本参加意思表明->users_groupsのattendance=1

| users | groups | events | restaurants | location | category | users_groups | users_events |
|---:|---:|---:|---:|---:|---:|---:|---:|
| name       | event_id      | name        | name        | name | name | user_id    | user_id  |
| email      | restaurant_id | start_time  | location_id |      |      | group_id   | event_id |
| gender     |               | end_time    |             |      |      | attendance |          |
| birthday   |               | image       |             |      |      | evaluation |          |
| job        |               | location_id |             |      |      |            |          |
| university |               | category_id |             |      |      |            |          |


### Associations

- user has many [groups, events]
- group has many [users], belongs to [event, restaurant]
- event has many [groups, users], belongs to [location, category]
- restaurant has many [group], belongs to [location]
- location has many [events, restaurants]
- category has many [events]
