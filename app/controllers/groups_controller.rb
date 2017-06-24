class GroupsController < ApplicationController
  def show
    @group = Group.find(params[:id])
    @event = Event.find(params[:event_id])
  end

  def create
    event = Event.find(params[:event_id])
    group = Group.new
    group.event = event
    group.users = event.users
    group.restaurant = Restaurant.first # ToDo ここの処理を書く

    # ToDo Pythonに処理を移す
    if group.save
      redirect_to event_group_path(event, group)
    else
      redirect_to event_path(event)
    end
  end
end
