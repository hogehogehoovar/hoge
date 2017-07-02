class EventsController < ApplicationController
  include AjaxHelper

  def index
    # jsで位置情報を取得し、searchアクションへ遷移
  end

  def show
    @event = Event.find(params[:id])
  end

  def search
    # ユーザーの現在位置から半径50km圏内にある施設のうち、最も近い施設を入手
    facility = Facility.near(coordinate, 50, :units => :km).first
    # ToDo: 施設が見つからない時の例外処理
    event = facility.current_event

    respond_to do |format|
      format.html { redirecti_to root_path }
      format.js   { render ajax_redirect_to(event_path(event)) }
    end
  end

  private

  def coordinate
    lat = params.require(:coordinate).require(:latitude)
    lon = params.require(:coordinate).require(:longitude)
    return [lat, lon]
  end
end
