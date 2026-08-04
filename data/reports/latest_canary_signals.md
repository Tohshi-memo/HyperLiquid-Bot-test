# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T23:52:28.767123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `12`; crypto_alt avg `-0.0637` n `230`; crypto_major avg `0.0069` n `8`; equity avg `0.1309` n `108`; fx avg `-0.0048` n `6`; index avg `0.0118` n `25`; metal avg `0.0287` n `20`; unknown avg `-0.0155` n `781`
- 1h: commodity avg `-0.0331` n `12`; crypto_alt avg `-0.1771` n `230`; crypto_major avg `-0.1336` n `8`; equity avg `0.2762` n `108`; fx avg `0.0011` n `6`; index avg `0.022` n `25`; metal avg `-0.0496` n `20`; unknown avg `-0.0106` n `781`
- 4h: commodity avg `-0.1318` n `12`; crypto_alt avg `-0.195` n `230`; crypto_major avg `-0.3274` n `8`; equity avg `-0.1118` n `108`; fx avg `0.0028` n `6`; index avg `-0.0417` n `25`; metal avg `-0.0248` n `20`; unknown avg `0.1725` n `781`
- 24h: commodity avg `-1.3012` n `12`; crypto_alt avg `0.035` n `230`; crypto_major avg `0.5935` n `8`; equity avg `3.0243` n `107`; fx avg `0.0731` n `6`; index avg `0.6569` n `25`; metal avg `0.8417` n `20`; unknown avg `0.4123` n `764`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
