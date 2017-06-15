class CreateUserGroups < ActiveRecord::Migration[5.0]
  def change
    create_table :users_groups do |t|
      t.references :user, foreign_key: true, null: false
      t.references :group, foreign_key: true, null: false
      t.boolean :attendance, default: false, null: false
      t.integer :evaluation
      t.timestamps
    end
  end
end
