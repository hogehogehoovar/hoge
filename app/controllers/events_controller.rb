class EventsController < ApplicationController
  def index
  end

  def search
    # ユーザーの現在位置から半径50km圏内にある施設のうち、最も近い施設を入手
    location = Location.near(coordinate, 50, :units => :km).first
    event = location.current_event
    render :index
  end

  private

  def coordinate
    lat = params.require(:coordinate).require(:latitude)
    lon = params.require(:coordinate).require(:longitude)
    return [lat, lon]
  end
end
