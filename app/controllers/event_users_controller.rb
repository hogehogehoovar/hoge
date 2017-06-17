class EventUsersController < ApplicationController
  def create
    @event = Event.find(params[:event_id])
    event_user = EventUser.new( { event_id: @event.id, user_id: current_user.id } )
    if event_user.save
      redirect_to event_path(@event)
    else
      render template: "events/show"
    end
  end
end
