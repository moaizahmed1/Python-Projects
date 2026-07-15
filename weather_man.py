def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("-e", "--extreme", metavar="YYYY")
    parser.add_argument("-a", "--average", metavar="YYYY/M")
    parser.add_argument("-c", "--chart", metavar="YYYY/M")
    args = parser.parse_args()

    parser_obj, calc, repo = WeatherParser(), WeatherCalculator(), ReportGenerator()
    month_map = {"1":"Jan","2":"Feb","3":"Mar","4":"Apr","5":"May","6":"Jun","7":"Jul","8":"Aug","9":"Sep","10":"Oct","11":"Nov","12":"Dec"}
    full_month_map = {"1":"January","2":"February","3":"March","4":"April","5":"May","6":"June","7":"July","8":"August","9":"September","10":"October","11":"November","12":"December"}

    # 1. Extreme Report (Independent)
    if args.extreme:
        readings = []
        for f in os.listdir(args.path):
            if args.extreme in f:
                readings.extend(parser_obj.get_readings_from_file(os.path.join(args.path, f)))
        if readings: 
            repo.print_yearly(calc.get_yearly_stats(readings))

    # 2. Average Report (Independent)
    if args.average:
        y, m = args.average.split('/')
        m_str = month_map[str(int(m))]
        target_file = next((f for f in os.listdir(args.path) if y in f and m_str in f), None)
        if target_file:
            readings = parser_obj.get_readings_from_file(os.path.join(args.path, target_file))
            repo.print_monthly(calc.get_monthly_avgs(readings))

    # 3. Chart Report (Independent)
    if args.chart:
        y, m = args.chart.split('/')
        m_str = month_map[str(int(m))]
        full_m = full_month_map[str(int(m))]
        target_file = next((f for f in os.listdir(args.path) if y in f and m_str in f), None)
        if target_file:
            readings = parser_obj.get_readings_from_file(os.path.join(args.path, target_file))
            repo.draw_chart(readings, full_m, y)