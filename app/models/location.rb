class Location < ApplicationRecord
  geocoded_by :address
  before_validation :geocode
  has_many :events
end
