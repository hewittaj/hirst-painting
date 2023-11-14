import colorgram
extracted_colors = colorgram.extract('hirst.jpg', 18)
color_values = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in extracted_colors]

print(color_values)