class Group < ApplicationRecord
  has_many :group_users
  has_many :users, through: :group_users
  belongs_to :event
  belongs_to :restaurant
  scope :search_by_user_and_event, -> (user_id, event_id) { joins(:group_users).find_by("group_users.user_id = ? AND event_id = ?", user_id, event_id) }
end
