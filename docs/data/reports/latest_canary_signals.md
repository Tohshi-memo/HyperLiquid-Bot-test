# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T18:07:32.750013+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0762` n `12`; crypto_alt avg `-0.034` n `230`; crypto_major avg `-0.033` n `8`; equity avg `0.0174` n `92`; fx avg `0.0058` n `6`; index avg `0.0021` n `25`; metal avg `-0.0049` n `20`; unknown avg `-0.0159` n `767`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `-0.1306` n `230`; crypto_major avg `0.1068` n `8`; equity avg `0.141` n `92`; fx avg `-0.0142` n `6`; index avg `0.0115` n `25`; metal avg `0.0311` n `20`; unknown avg `0.0459` n `766`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `0.2256` n `230`; crypto_major avg `0.5862` n `8`; equity avg `0.6472` n `92`; fx avg `-0.0398` n `6`; index avg `0.1247` n `25`; metal avg `-0.1297` n `20`; unknown avg `-0.2546` n `758`
- 24h: commodity avg `0.1989` n `12`; crypto_alt avg `1.8943` n `230`; crypto_major avg `3.4433` n `8`; equity avg `1.1312` n `92`; fx avg `-0.0183` n `6`; index avg `0.3596` n `25`; metal avg `0.6742` n `20`; unknown avg `-0.0546` n `742`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1905`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0669`, n `668`, weak_sample_signal
