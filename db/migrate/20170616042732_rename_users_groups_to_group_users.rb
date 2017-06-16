class RenameUsersGroupsToGroupUsers < ActiveRecord::Migration[5.0]
  def change
    rename_table :users_groups, :group_users
  end
end
