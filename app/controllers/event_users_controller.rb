class EventUsersController < ApplicationController
  before_action :authenticate_user!

  def create
    @event = Event.find(params[:event_id])
    event_user = EventUser.new( { event_id: @event.id, user_id: current_user.id } )
    if event_user.save
      redirect_to event_path(@event)
    else
      redirect_to event_path(@event)
    end
  end
end
