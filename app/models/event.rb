class Event < ApplicationRecord
  belongs_to :location
  # ToDO 命名規則
  # has_many :users_events
  # has_many :users, through: :users_events
end
