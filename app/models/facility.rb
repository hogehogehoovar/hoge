class Facility < ApplicationRecord
  geocoded_by :address
  before_validation :geocode
  has_many :events
  has_many :restaurants

  def current_event
    events.find_by("(start_time <= ?) OR (end_time >= ?)", DateTime.now, DateTime.now)
  end
end
