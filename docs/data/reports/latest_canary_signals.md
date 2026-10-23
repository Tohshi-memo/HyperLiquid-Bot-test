# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T12:22:33.864540+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0289` n `13`; crypto_alt avg `0.0888` n `237`; crypto_major avg `0.0755` n `8`; equity avg `0.0498` n `152`; fx avg `-0.0006` n `6`; index avg `0.0096` n `26`; metal avg `-0.0614` n `20`; unknown avg `0.0048` n `1233`
- 1h: commodity avg `0.1291` n `13`; crypto_alt avg `0.207` n `237`; crypto_major avg `0.1797` n `8`; equity avg `-0.0879` n `152`; fx avg `-0.0277` n `6`; index avg `-0.0165` n `26`; metal avg `-0.098` n `20`; unknown avg `-0.1917` n `1225`
- 4h: commodity avg `0.1091` n `13`; crypto_alt avg `-0.1682` n `237`; crypto_major avg `-0.3214` n `8`; equity avg `-1.1183` n `152`; fx avg `-0.0711` n `6`; index avg `-0.1605` n `26`; metal avg `-0.0451` n `20`; unknown avg `2.2227` n `1201`
- 24h: commodity avg `0.3299` n `13`; crypto_alt avg `0.1298` n `237`; crypto_major avg `0.1843` n `8`; equity avg `-1.7185` n `152`; fx avg `-0.0678` n `6`; index avg `-0.2245` n `26`; metal avg `-0.3852` n `20`; unknown avg `49.6407` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
