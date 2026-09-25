# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T02:07:28.245336+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0345` n `12`; crypto_alt avg `0.3173` n `234`; crypto_major avg `0.2984` n `8`; equity avg `0.0575` n `141`; fx avg `-0.0261` n `6`; index avg `0.0026` n `26`; metal avg `0.0433` n `20`; unknown avg `-0.192` n `944`
- 1h: commodity avg `-0.0774` n `12`; crypto_alt avg `-0.1482` n `234`; crypto_major avg `0.136` n `8`; equity avg `0.2423` n `141`; fx avg `-0.0623` n `6`; index avg `0.0689` n `26`; metal avg `0.0464` n `20`; unknown avg `-0.1467` n `944`
- 4h: commodity avg `-0.2867` n `12`; crypto_alt avg `0.3272` n `234`; crypto_major avg `0.5075` n `8`; equity avg `0.3467` n `141`; fx avg `-0.0847` n `6`; index avg `0.0769` n `26`; metal avg `0.0497` n `20`; unknown avg `2.6838` n `898`
- 24h: commodity avg `0.3946` n `12`; crypto_alt avg `4.5042` n `234`; crypto_major avg `2.1925` n `8`; equity avg `0.3512` n `141`; fx avg `-0.0684` n `6`; index avg `0.0168` n `26`; metal avg `0.0995` n `20`; unknown avg `21.8744` n `815`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1522`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
