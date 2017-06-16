# README

## DATABASE_DESIGN

### テーブル設計

- 一つのカラムが一つのテーブルを表している
- userが位置情報を送信->users_events作成
- アルゴリズムで仮グループを作成->users_groups作成
- userが本参加意思表明->users_groupsのattendance=1
- locationはイベント開催施設（東京ドームなど）を表し、eventとrestaurantを仲介する

| users | groups | events | restaurants | location | group_users | event_users |
|---:|---:|---:|---:|---:|---:|---:|
| name       | event_id      | name        | name         | name      | user_id    | user_id  |
| email      | restaurant_id | start_time  | location_id  | address   | group_id   | event_id |
| gender     |               | end_time    | address      | latitude  | attendance |          |
| birthday   |               | image       | phone_number | longitude | evaluation |          |
| job        |               | location_id | url          |           |            |          |
| university |               | category    |              |           |            |          |
| image      |               |             |              |           |            |          |


### Associations

- user has many [groups, events]
- group has many [users], belongs to [event, restaurant]
- event has many [groups, users], belongs to [location], has many restaurants through location
- restaurant has many [group], belongs to [location], has many events through location
- location has many [events, restaurants]

