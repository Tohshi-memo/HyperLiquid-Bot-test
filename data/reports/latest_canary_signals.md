# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T07:22:17.048225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0591` n `12`; crypto_alt avg `-0.3809` n `228`; crypto_major avg `-0.3788` n `8`; equity avg `-0.0976` n `66`; fx avg `0.0102` n `5`; index avg `-0.1082` n `23`; metal avg `-0.2003` n `18`; unknown avg `-0.1604` n `383`
- 1h: commodity avg `-0.2443` n `12`; crypto_alt avg `-0.2158` n `228`; crypto_major avg `-0.086` n `8`; equity avg `0.1801` n `66`; fx avg `0.0183` n `5`; index avg `0.0206` n `23`; metal avg `0.1859` n `18`; unknown avg `-0.3212` n `383`
- 4h: commodity avg `-0.101` n `12`; crypto_alt avg `-1.0112` n `228`; crypto_major avg `-0.5738` n `8`; equity avg `0.1848` n `66`; fx avg `-0.0235` n `5`; index avg `0.0526` n `23`; metal avg `0.4556` n `18`; unknown avg `-0.2546` n `363`
- 24h: commodity avg `0.6993` n `12`; crypto_alt avg `-3.1692` n `228`; crypto_major avg `-1.5869` n `8`; equity avg `-0.1308` n `65`; fx avg `0.0726` n `5`; index avg `0.0331` n `23`; metal avg `-0.1972` n `18`; unknown avg `-0.4017` n `363`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1029`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
