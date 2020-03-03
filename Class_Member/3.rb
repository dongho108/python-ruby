class Cs
  @@count = 0
  def initialize()
    @@count = @@count + 1
  end
  def Cs.getCount()
    return @@count
  end
end


i1 = Cs.new()
p Cs.getCount()
i2 = Cs.new()
p Cs.getCount()
i3 = Cs.new()
p Cs.getCount()
i4 = Cs.new()
p Cs.getCount()
