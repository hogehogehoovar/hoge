class Location < ApplicationRecord
  geocoded_by :address
  before_validation :geocode
  has_many :events

  def current_event
    events.find_by("(start_time <= ?) OR (end_time >= ?)", DateTime.now, DateTime.now)
  end
end
