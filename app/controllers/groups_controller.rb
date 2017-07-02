class GroupsController < ApplicationController
  def index
  end

  def show
    @group = Group.find(params[:id])
    @users = @group.users
    @group_user = GroupUser.find_by(group_id: @group.id, user_id: current_user.id)
    @event = Event.find(params[:event_id])
    @restaurant = @group.restaurant
    @facility = @event.facility
    locations = [@restaurant, @facility]
    @hash = Gmaps4rails.build_markers(locations) do |location, marker|
      marker.lat location.latitude
      marker.lng location.longitude
      marker.infowindow location.name
    end
  end
end
