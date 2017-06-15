class RemoveAddressFromEvents < ActiveRecord::Migration[5.0]
  def change
    remove_column :events, :address, :string
  end
end
