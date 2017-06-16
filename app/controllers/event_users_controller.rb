class EventUsersController < ApplicationController
  def create
    event = Event.find(params[:event_id])
    # ToDo 処理を書く
    redirect_to event_path(event)
  end
end
