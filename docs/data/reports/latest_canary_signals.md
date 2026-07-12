# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T03:22:26.504824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0859` n `12`; crypto_alt avg `0.1418` n `230`; crypto_major avg `0.0821` n `8`; equity avg `0.0151` n `92`; fx avg `-0.0038` n `6`; index avg `-0.0091` n `25`; metal avg `0.0036` n `20`; unknown avg `-0.0521` n `765`
- 1h: commodity avg `-0.1395` n `12`; crypto_alt avg `0.1509` n `230`; crypto_major avg `-0.0032` n `8`; equity avg `0.0404` n `92`; fx avg `-0.0015` n `6`; index avg `-0.0099` n `25`; metal avg `0.0096` n `20`; unknown avg `0.1463` n `765`
- 4h: commodity avg `0.0037` n `12`; crypto_alt avg `0.1602` n `230`; crypto_major avg `-0.2061` n `8`; equity avg `-0.0144` n `92`; fx avg `-0.0029` n `6`; index avg `-0.0732` n `25`; metal avg `-0.0295` n `20`; unknown avg `-0.0514` n `765`
- 24h: commodity avg `0.3942` n `12`; crypto_alt avg `-0.523` n `229`; crypto_major avg `-0.3487` n `8`; equity avg `0.0792` n `92`; fx avg `0.0167` n `6`; index avg `-0.1118` n `25`; metal avg `-0.102` n `20`; unknown avg `0.0813` n `727`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
