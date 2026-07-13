# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T01:52:25.026976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0312` n `12`; crypto_alt avg `-0.1711` n `230`; crypto_major avg `-0.1868` n `8`; equity avg `-0.3555` n `92`; fx avg `0.0077` n `6`; index avg `-0.1279` n `25`; metal avg `-0.0125` n `20`; unknown avg `0.0342` n `766`
- 1h: commodity avg `0.0196` n `12`; crypto_alt avg `-0.4489` n `230`; crypto_major avg `-0.522` n `8`; equity avg `-0.7917` n `92`; fx avg `0.0186` n `6`; index avg `-0.1968` n `25`; metal avg `0.0554` n `20`; unknown avg `0.1757` n `766`
- 4h: commodity avg `-0.0346` n `12`; crypto_alt avg `-0.5788` n `230`; crypto_major avg `-0.4888` n `8`; equity avg `-1.6385` n `92`; fx avg `0.0579` n `6`; index avg `-0.4128` n `25`; metal avg `-0.1443` n `20`; unknown avg `-0.026` n `765`
- 24h: commodity avg `0.044` n `12`; crypto_alt avg `-1.0063` n `230`; crypto_major avg `-0.3394` n `8`; equity avg `-1.6471` n `92`; fx avg `0.0112` n `6`; index avg `-0.3966` n `25`; metal avg `-0.226` n `20`; unknown avg `0.2672` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
