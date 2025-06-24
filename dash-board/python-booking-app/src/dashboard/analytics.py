from db.connection import get_db_connection

def generate_dashboard_data():
    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
    SELECT COUNT(*) AS total_bookings, 
           DATE(Booking_Time) AS booking_date 
    FROM Booking 
    GROUP BY booking_date 
    ORDER BY booking_date;
    """
    
    cursor.execute(query)
    results = cursor.fetchall()
    print("Dashboard query results:", results)  # Add this line

    dashboard_data = {
        "total_bookings": [],
        "booking_dates": []
    }

    for row in results:
        dashboard_data["total_bookings"].append(row[0])
        dashboard_data["booking_dates"].append(row[1].strftime('%Y-%m-%d'))

    cursor.close()
    connection.close()

    print("Dashboard data:", dashboard_data)  # Add this line
    return dashboard_data