class CreateEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :events do |t|
      t.string :name, null: false
      t.datetime :start_time, null: false
      t.datetime :end_time, null: false
      t.string :image
      t.references :location, foreign_key: true, null: false
      t.string :category
      t.string :address
      t.timestamps
    end
  end
end
