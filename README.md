# README

## DATABASE_DESIGN

### テーブル設計

- 一つのカラムが一つのテーブルを表している
- userが位置情報を送信->users_events作成
- アルゴリズムで仮グループを作成->users_groups作成
- userが本参加意思表明->users_groupsのattendance=1
- locationはイベント開催施設（東京ドームなど）を表し、eventとrestaurantを仲介する

| users | groups | events | restaurants | location | category | users_groups | users_events |
|---:|---:|---:|---:|---:|---:|---:|---:|
| name       | event_id      | name        | name        | name    | name | user_id    | user_id  |
| email      | restaurant_id | start_time  | location_id |         |      | group_id   | event_id |
| gender     |               | end_time    | address     |         |      | attendance |          |
| birthday   |               | image       |             |         |      | evaluation |          |
| job        |               | location_id |             |         |      |            |          |
| university |               | category_id |             |         |      |            |          |
|            |               | address     |             |         |      |            |          |


### Associations

- user has many [groups, events]
- group has many [users], belongs to [event, restaurant]
- event has many [groups, users], belongs to [location, category], has many restaurants through location
- restaurant has many [group], belongs to [location], has many events through location
- location has many [events, restaurants]
- category has many [events]
