class CreateRestaurants < ActiveRecord::Migration[5.0]
  def change
    create_table :restaurants do |t|
      t.string :name, null: false
      t.references :facility, foreign_key: true, null: false
      t.string :address, null: false
      t.string :phone_number
      t.string :url
      t.timestamps
    end
  end
end
