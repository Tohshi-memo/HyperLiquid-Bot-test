# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T21:52:30.052635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0243` n `12`; crypto_alt avg `-0.2003` n `234`; crypto_major avg `-0.1202` n `8`; equity avg `-0.0323` n `141`; fx avg `-0.0024` n `6`; index avg `0.0014` n `26`; metal avg `-0.0058` n `20`; unknown avg `6.93` n `961`
- 1h: commodity avg `0.0346` n `12`; crypto_alt avg `0.8344` n `234`; crypto_major avg `0.5285` n `8`; equity avg `0.0631` n `141`; fx avg `-0.0033` n `6`; index avg `0.0025` n `26`; metal avg `0.0049` n `20`; unknown avg `6.9652` n `959`
- 4h: commodity avg `0.0251` n `12`; crypto_alt avg `-1.0334` n `234`; crypto_major avg `-0.3025` n `8`; equity avg `-0.0404` n `141`; fx avg `-0.0164` n `6`; index avg `-0.0171` n `26`; metal avg `0.0058` n `20`; unknown avg `-0.4277` n `953`
- 24h: commodity avg `0.2953` n `12`; crypto_alt avg `1.2917` n `234`; crypto_major avg `-0.3917` n `8`; equity avg `-0.0533` n `141`; fx avg `0.0148` n `6`; index avg `-0.0605` n `26`; metal avg `-0.036` n `20`; unknown avg `4.3007` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
