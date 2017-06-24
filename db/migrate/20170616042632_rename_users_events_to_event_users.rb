class RenameUsersEventsToEventUsers < ActiveRecord::Migration[5.0]
  def change
    rename_table :users_events, :event_users
  end
end
