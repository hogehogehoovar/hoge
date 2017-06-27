class ChangeDatatypeLatAndLng < ActiveRecord::Migration[5.0]
  def change
    change_column :restaurants, :latitude, :double
    change_column :restaurants, :longitude, :double
    change_column :facilities, :latitude, :double
    change_column :facilities, :longitude, :double
  end
end
