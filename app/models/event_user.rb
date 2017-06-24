class EventUser < ApplicationRecord
  validates_uniqueness_of :event_id, scope: :user_id
  belongs_to :user
  belongs_to :event
end
