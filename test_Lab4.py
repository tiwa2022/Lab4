import functions as f

def test_months():
    aMonths = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sept","Oct","Nov","Dec"]
    assert "Jul"== aMonths[6]


def test_avg():
    my_list =[20,22,20,21,11,4,50,19,15,7,19,27,96,10,30,3,20,19,20,5]
    avg = f. sum (my_list) / len (my_list)
    assert avg == 21.9
    

def test_rainfall():
    aRainfall = [63,57,54,69,83,75,65,81,87,61,87,60]
    sum = f. sum(aRainfall)
    assert sum == 842
