# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T02:22:26.138812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `13`; crypto_alt avg `-0.0579` n `237`; crypto_major avg `-0.0263` n `8`; equity avg `0.0626` n `152`; fx avg `0.0` n `6`; index avg `0.0088` n `26`; metal avg `0.0024` n `20`; unknown avg `-0.066` n `1226`
- 1h: commodity avg `-0.0509` n `13`; crypto_alt avg `-0.035` n `237`; crypto_major avg `0.0725` n `8`; equity avg `0.1189` n `152`; fx avg `-0.0032` n `6`; index avg `0.0162` n `26`; metal avg `0.0103` n `20`; unknown avg `1.8068` n `1226`
- 4h: commodity avg `-0.0371` n `13`; crypto_alt avg `-0.7299` n `237`; crypto_major avg `-0.6431` n `8`; equity avg `-0.0081` n `152`; fx avg `-0.044` n `6`; index avg `-0.022` n `26`; metal avg `-0.043` n `20`; unknown avg `4.0968` n `1214`
- 24h: commodity avg `0.3147` n `13`; crypto_alt avg `-1.3615` n `237`; crypto_major avg `-0.8402` n `8`; equity avg `0.9193` n `152`; fx avg `-0.0519` n `6`; index avg `0.1172` n `26`; metal avg `-0.1227` n `20`; unknown avg `206.0319` n `1014`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1919`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
