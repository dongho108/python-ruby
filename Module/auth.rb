

module Auth
  module_function()
  def login(_id)
    members = ['egoing', 'k8805', 'leezche']
    for member in members do
        if _id == member
            return true
        end
    end
    return false
  end
end
