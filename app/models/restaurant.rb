class Restaurant < ApplicationRecord
  geocoded_by :address
  before_validation :geocode
  has_many :groups
end
