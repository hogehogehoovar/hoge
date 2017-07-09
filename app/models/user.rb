class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :trackable, :validatable
  enum gender: { male: 0, female: 1 }
  has_many :event_users
  has_many :events, through: :event_users
  has_many :group_users
  has_many :groups, through: :group_users

  def age
    date_format = "%Y%m%d"
    (Date.today.strftime(date_format).to_i - birthday.strftime(date_format).to_i) / 10000
  end

  def attend_group?(group_id)
    group_users.find_by(group_id: group_id) == 1
  end
end
