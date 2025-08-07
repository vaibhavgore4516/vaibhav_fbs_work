radius=20
length=50
breadth=40
wire_round=5
cost_wire=35
semicircle_perimeter=3.14*radius
rectangle_perimeter=length+breadth+radius
single_round=semicircle_perimeter+rectangle_perimeter
wire_length=single_round*wire_round
total_cost=wire_length*cost_wire

print("total cost of facing,",round(total_cost,2))
