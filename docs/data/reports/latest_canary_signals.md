# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T09:52:27.066710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `0.0179` n `237`; crypto_major avg `0.107` n `8`; equity avg `0.0081` n `152`; fx avg `0.0087` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0002` n `20`; unknown avg `-0.0183` n `1233`
- 1h: commodity avg `0.1381` n `13`; crypto_alt avg `-0.4549` n `237`; crypto_major avg `-0.401` n `8`; equity avg `-0.5406` n `152`; fx avg `-0.0299` n `6`; index avg `-0.0788` n `26`; metal avg `-0.0647` n `20`; unknown avg `1.2218` n `1207`
- 4h: commodity avg `0.1003` n `13`; crypto_alt avg `-0.2821` n `237`; crypto_major avg `-0.0848` n `8`; equity avg `0.2118` n `152`; fx avg `-0.0723` n `6`; index avg `-0.0524` n `26`; metal avg `-0.1467` n `20`; unknown avg `0.1705` n `1135`
- 24h: commodity avg `0.3135` n `13`; crypto_alt avg `-0.0974` n `237`; crypto_major avg `0.2148` n `8`; equity avg `-0.9844` n `152`; fx avg `-0.043` n `6`; index avg `-0.1263` n `26`; metal avg `-0.4414` n `20`; unknown avg `49.4533` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1976`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
