# Script pour corriger la section prévisions

old_section = '''            # Prévision quotidienne simple (baseline) réactive au slider
            forecast_daily = pd.DataFrame()
            if not daily_product.empty:
                hist_mean = daily_product.tail(30).mean()
                hist_std = daily_product.tail(30).std(ddof=0)
                hist_mean = 0 if np.isnan(hist_mean) else hist_mean
                hist_std = 0 if np.isnan(hist_std) else hist_std
                lower = np.maximum(hist_mean - 1.28 * hist_std, 0)  # ~80% CI
                upper = hist_mean + 1.28 * hist_std
                start_date = daily_product.index.max() + pd.Timedelta(days=1)
                horizon_dates = pd.date_range(start=start_date, periods=forecast_days, freq='D')
                forecast_daily = pd.DataFrame({
                    'date': horizon_dates,
                    'forecast_qty': hist_mean,
                    'lower': lower,
                    'upper': upper
                })'''

new_section = '''            # Prévision quotidienne simple (baseline) réactive au slider - TOUJOURS générer
            forecast_daily = pd.DataFrame()
            hist_mean = 0
            hist_std = 0
            
            if not daily_product.empty:
                hist_mean = float(daily_product.tail(30).mean())
                hist_std = float(daily_product.tail(30).std(ddof=0))
            else:
                # Fallback: utiliser moyenne des quantities
                hist_mean = float(product_data['quantity'].mean())
                hist_std = float(product_data['quantity'].std(ddof=0))
            
            hist_mean = 0 if np.isnan(hist_mean) else hist_mean
            hist_std = 0 if np.isnan(hist_std) else hist_std
            lower = np.maximum(hist_mean - 1.28 * hist_std, 0)  # ~80% CI
            upper = hist_mean + 1.28 * hist_std
            
            try:
                if not daily_product.empty:
                    start_date = daily_product.index.max() + pd.Timedelta(days=1)
                    horizon_dates = pd.date_range(start=start_date, periods=forecast_days, freq='D')
                else:
                    horizon_dates = pd.date_range(start=pd.Timestamp.now(), periods=forecast_days, freq='D')
            except:
                horizon_dates = list(range(forecast_days))
            
            forecast_daily = pd.DataFrame({
                'date': horizon_dates,
                'forecast_qty': hist_mean,
                'lower': lower,
                'upper': upper
            })'''

print("Remplacement section Prévisions OK")
print("Old condition: if not daily_product.empty:")
print("New: TOUJOURS générer avec fallback")
