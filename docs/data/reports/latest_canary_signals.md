# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T09:22:24.045325+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.2176` n `232`; crypto_major avg `0.2433` n `8`; equity avg `0.0328` n `134`; fx avg `0.0012` n `6`; index avg `0.0052` n `26`; metal avg `0.025` n `20`; unknown avg `0.0044` n `794`
- 1h: commodity avg `0.0143` n `12`; crypto_alt avg `0.3265` n `232`; crypto_major avg `0.2852` n `8`; equity avg `0.0385` n `134`; fx avg `-0.0146` n `6`; index avg `0.0073` n `26`; metal avg `0.0346` n `20`; unknown avg `331.7605` n `786`
- 4h: commodity avg `0.0166` n `12`; crypto_alt avg `-0.1032` n `232`; crypto_major avg `-0.007` n `8`; equity avg `0.1007` n `134`; fx avg `-0.0102` n `6`; index avg `0.0062` n `26`; metal avg `0.0208` n `20`; unknown avg `32.3593` n `766`
- 24h: commodity avg `0.1633` n `12`; crypto_alt avg `1.8744` n `232`; crypto_major avg `1.9751` n `8`; equity avg `0.4537` n `134`; fx avg `-0.049` n `6`; index avg `0.0954` n `26`; metal avg `0.0295` n `20`; unknown avg `493.2983` n `676`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
