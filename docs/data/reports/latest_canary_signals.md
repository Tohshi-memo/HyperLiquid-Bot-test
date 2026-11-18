# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-18T23:07:29.745840+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.16` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0021` n `13`; crypto_alt avg `0.71` n `239`; crypto_major avg `0.6893` n `8`; equity avg `0.6843` n `164`; fx avg `-0.003` n `6`; index avg `0.0891` n `27`; metal avg `0.0906` n `20`; unknown avg `1.1718` n `1259`
- 1h: commodity avg `-0.022` n `13`; crypto_alt avg `0.0744` n `239`; crypto_major avg `0.2139` n `8`; equity avg `0.4297` n `164`; fx avg `0.002` n `6`; index avg `0.077` n `27`; metal avg `0.0706` n `20`; unknown avg `4.093` n `1261`
- 4h: commodity avg `-0.0188` n `13`; crypto_alt avg `-0.2646` n `239`; crypto_major avg `-0.3191` n `8`; equity avg `0.5336` n `164`; fx avg `0.0007` n `6`; index avg `0.0965` n `27`; metal avg `0.0524` n `20`; unknown avg `4.0969` n `1217`
- 24h: commodity avg `-0.2498` n `13`; crypto_alt avg `-1.7438` n `239`; crypto_major avg `-2.6655` n `8`; equity avg `-2.4148` n `164`; fx avg `-0.1589` n `6`; index avg `-0.1843` n `27`; metal avg `-1.1696` n `20`; unknown avg `47.7988` n `1128`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
