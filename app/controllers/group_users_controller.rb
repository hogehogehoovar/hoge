class GroupUsersController < ApplicationController
  def attend
    group = Group.find(params[:group_id])
    group_user = GroupUser.find_by(group_id: group.id, user_id: current_user.id)
    group_user.attendance = 1
    group_user.save
  end
end
