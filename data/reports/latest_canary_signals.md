# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T02:37:12.192482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0211` n `12`; crypto_alt avg `0.1735` n `228`; crypto_major avg `0.1251` n `8`; equity avg `0.0542` n `65`; fx avg `0.0` n `5`; index avg `-0.0034` n `23`; metal avg `0.0008` n `18`; unknown avg `-0.2306` n `376`
- 1h: commodity avg `-0.0316` n `12`; crypto_alt avg `0.5682` n `228`; crypto_major avg `0.3779` n `8`; equity avg `0.049` n `65`; fx avg `0.0` n `5`; index avg `0.0364` n `23`; metal avg `0.0222` n `18`; unknown avg `0.3273` n `376`
- 4h: commodity avg `-0.0345` n `12`; crypto_alt avg `-0.5832` n `228`; crypto_major avg `-0.2403` n `8`; equity avg `0.0707` n `65`; fx avg `0.0011` n `5`; index avg `0.1279` n `23`; metal avg `0.0348` n `18`; unknown avg `-0.0805` n `376`
- 24h: commodity avg `0.3703` n `12`; crypto_alt avg `-1.6391` n `228`; crypto_major avg `-0.798` n `8`; equity avg `0.6757` n `65`; fx avg `-0.0074` n `5`; index avg `0.285` n `23`; metal avg `0.1145` n `18`; unknown avg `-0.6639` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
