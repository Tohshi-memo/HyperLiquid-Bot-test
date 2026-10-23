# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T20:37:31.157885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `0.22` n `237`; crypto_major avg `0.1301` n `8`; equity avg `0.0301` n `152`; fx avg `-0.0116` n `6`; index avg `0.0056` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.0805` n `1226`
- 1h: commodity avg `-0.0193` n `13`; crypto_alt avg `-0.4211` n `237`; crypto_major avg `-0.0254` n `8`; equity avg `0.0758` n `152`; fx avg `-0.0303` n `6`; index avg `0.016` n `26`; metal avg `-0.031` n `20`; unknown avg `109.4304` n `1150`
- 4h: commodity avg `0.0593` n `13`; crypto_alt avg `-1.3014` n `237`; crypto_major avg `-0.7643` n `8`; equity avg `-0.4228` n `152`; fx avg `-0.0503` n `6`; index avg `-0.0278` n `26`; metal avg `-0.0915` n `20`; unknown avg `0.1875` n `1141`
- 24h: commodity avg `0.4377` n `13`; crypto_alt avg `0.5317` n `237`; crypto_major avg `0.5775` n `8`; equity avg `1.3216` n `152`; fx avg `-0.1022` n `6`; index avg `0.0882` n `26`; metal avg `-0.1184` n `20`; unknown avg `-0.1828` n `1022`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2018`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1784`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1533`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
