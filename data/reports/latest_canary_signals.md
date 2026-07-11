# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T11:33:59.188588+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0168` n `12`; crypto_alt avg `0.1129` n `230`; crypto_major avg `0.0403` n `8`; equity avg `0.0061` n `92`; fx avg `-0.0102` n `6`; index avg `-0.0023` n `25`; metal avg `0.0` n `20`; unknown avg `-0.0205` n `765`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `0.0521` n `230`; crypto_major avg `0.1153` n `8`; equity avg `0.0158` n `92`; fx avg `-0.0021` n `6`; index avg `-0.0036` n `25`; metal avg `-0.0045` n `20`; unknown avg `-0.1432` n `765`
- 4h: commodity avg `0.0148` n `12`; crypto_alt avg `0.2584` n `230`; crypto_major avg `0.21` n `8`; equity avg `0.0465` n `92`; fx avg `-0.0052` n `6`; index avg `0.0046` n `25`; metal avg `0.0083` n `20`; unknown avg `-0.2078` n `761`
- 24h: commodity avg `-0.3212` n `12`; crypto_alt avg `0.1589` n `229`; crypto_major avg `-0.433` n `8`; equity avg `-0.3332` n `92`; fx avg `-0.1072` n `6`; index avg `0.1154` n `25`; metal avg `0.2051` n `20`; unknown avg `2.7773` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0894`, n `668`, weak_sample_signal
