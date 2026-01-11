def tamgiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            loaiTamGiac = 'Tam giác đều'  # Equilateral triangle
        elif a == b or a == c or b == c:
            loaiTamGiac = 'Tam giác cân'  # Isosceles triangle
        else:
            loaiTamGiac = 'Tam giác thường'  # Scalene triangle
    else:
        loaiTamGiac = 'Không phải là tam giác'  # Not a triangle
    return loaiTamGiac

