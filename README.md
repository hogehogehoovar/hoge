# README

## DATABASE_DESIGN

### テーブル設計

- 一つのカラムが一つのテーブルを表している
- userが位置情報を送信->users_events作成
- アルゴリズムで仮グループを作成->users_groups作成
- userが本参加意思表明->users_groupsのattendance=1
- locationはイベント開催施設（東京ドームなど）を表し、eventとrestaurantを仲介する

| users | groups | events | restaurants | facility | group_users | event_users |
|---:|---:|---:|---:|---:|---:|---:|
| name       | event_id      | name        | name         | name      | user_id    | user_id  |
| email      | restaurant_id | start_time  | facility_id  | address   | group_id   | event_id |
| gender     |               | end_time    | address      | latitude  | attendance |          |
| birthday   |               | image       | phone_number | longitude | evaluation |          |
| job        |               | facility_id | url          |           |            |          |
| university |               | category    |              |           |            |          |
| image      |               |             |              |           |            |          |


### Associations

- user has many [groups, events]
- group has many [users], belongs to [event, restaurant]
- event has many [groups, users], belongs to [facility], has many restaurants through facility
- restaurant has many [group], belongs to [facility], has many events through facility
- facility has many [events, restaurants]

