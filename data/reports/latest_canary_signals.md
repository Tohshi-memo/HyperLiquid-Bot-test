# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T12:22:36.005294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `13`; crypto_alt avg `0.2931` n `237`; crypto_major avg `0.188` n `8`; equity avg `0.1674` n `152`; fx avg `0.0017` n `6`; index avg `0.0249` n `26`; metal avg `0.0098` n `20`; unknown avg `0.4139` n `1230`
- 1h: commodity avg `0.0806` n `13`; crypto_alt avg `0.117` n `237`; crypto_major avg `0.1171` n `8`; equity avg `0.1567` n `152`; fx avg `-0.0056` n `6`; index avg `0.0167` n `26`; metal avg `0.0075` n `20`; unknown avg `1.3002` n `1224`
- 4h: commodity avg `0.1064` n `13`; crypto_alt avg `-0.0561` n `237`; crypto_major avg `-0.1918` n `8`; equity avg `0.1261` n `152`; fx avg `0.002` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0158` n `20`; unknown avg `12.147` n `1206`
- 24h: commodity avg `0.2574` n `13`; crypto_alt avg `-2.5871` n `237`; crypto_major avg `-1.9841` n `8`; equity avg `-0.2295` n `152`; fx avg `0.0219` n `6`; index avg `0.0352` n `26`; metal avg `-0.1344` n `20`; unknown avg `193.9773` n `1053`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1972`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1948`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1923`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1598`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
