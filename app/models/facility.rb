class Facility < ApplicationRecord
  geocoded_by :address
  before_validation :geocode
  has_many :events
  has_many :restaurants

  def current_event
    # OR じゃなくて AND だけど、デモとして動く状態を保つ為このままにする
    events.find_by("(start_time <= ?) OR (end_time >= ?)", DateTime.now, DateTime.now)
  end
end
