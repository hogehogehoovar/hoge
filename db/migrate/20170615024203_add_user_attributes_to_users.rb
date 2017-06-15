class AddUserAttributesToUsers < ActiveRecord::Migration[5.0]
  def change
    add_column :users, :gender, :integer
    add_column :users, :birthday, :date
    add_column :users, :job, :string
    add_column :users, :university, :string
  end
end
