# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T05:37:26.395048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0175` n `12`; crypto_alt avg `0.0119` n `230`; crypto_major avg `0.0218` n `8`; equity avg `0.0163` n `92`; fx avg `0.0` n `6`; index avg `-0.0005` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.1211` n `765`
- 1h: commodity avg `0.0173` n `12`; crypto_alt avg `-0.0862` n `230`; crypto_major avg `-0.0453` n `8`; equity avg `0.0058` n `92`; fx avg `0.0034` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.0203` n `765`
- 4h: commodity avg `-0.0454` n `12`; crypto_alt avg `0.1623` n `230`; crypto_major avg `-0.1229` n `8`; equity avg `0.0237` n `92`; fx avg `0.002` n `6`; index avg `0.0085` n `25`; metal avg `-0.0028` n `20`; unknown avg `-0.3565` n `765`
- 24h: commodity avg `0.4827` n `12`; crypto_alt avg `-0.5821` n `230`; crypto_major avg `-0.6182` n `8`; equity avg `0.0471` n `92`; fx avg `-0.0119` n `6`; index avg `-0.0974` n `25`; metal avg `-0.0958` n `20`; unknown avg `-0.1078` n `729`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
