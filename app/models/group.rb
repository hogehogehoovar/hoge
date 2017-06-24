class Group < ApplicationRecord
  has_many :group_users
  has_many :users, through: :group_users
  belongs_to :event
  belongs_to :restaurant
end
