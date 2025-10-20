

from calc.calc_funcs import block_volume, with_gap, count_item_in_total_v
brick_lwh = (250, 120, 65)
wall_lwh = (10000, 510, 3000)
mortar = 10

wall_v = block_volume(*wall_lwh[:2], height=wall_lwh[2])
print(f"Об'єм стіни {wall_v / 1000000000:.2f}м3")
bricks_count= count_item_in_total_v(wall_lwh, with_gap(brick_lwh, mortar))
print(f"Потрібно {bricks_count}кирпічів.")
bricks_v = bricks_count * block_volume(*brick_lwh[:2], height=brick_lwh[2])
mortar_v = wall_v - bricks_v
print(f"Потрібно {mortar_v / 1000000000:.2f}м3 розчину.")
