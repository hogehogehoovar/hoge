class Event < ApplicationRecord
  belongs_to :location
  has_many :event_users
  has_many :users, through: :event_users
end
