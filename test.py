import open3d as o3d

print("Testing IO for point cloud ...")
mesh = o3d.io.read_point_cloud("D:/youvision/photoneo_hd/result/SampleFrame.ply")
print(mesh)