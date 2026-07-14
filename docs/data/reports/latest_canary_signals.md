# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T12:37:29.146991+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.9076` n `230`; crypto_major avg `1.0384` n `8`; equity avg `0.8731` n `92`; fx avg `-0.011` n `6`; index avg `0.1863` n `25`; metal avg `0.4938` n `20`; unknown avg `0.3464` n `766`
- 1h: commodity avg `0.0572` n `12`; crypto_alt avg `0.8966` n `230`; crypto_major avg `1.0886` n `8`; equity avg `0.6794` n `92`; fx avg `0.0004` n `6`; index avg `0.1733` n `25`; metal avg `0.4005` n `20`; unknown avg `0.3596` n `766`
- 4h: commodity avg `-0.0557` n `12`; crypto_alt avg `0.8895` n `230`; crypto_major avg `1.2691` n `8`; equity avg `0.4261` n `92`; fx avg `0.0222` n `6`; index avg `0.2003` n `25`; metal avg `0.3681` n `20`; unknown avg `0.6255` n `766`
- 24h: commodity avg `1.1254` n `12`; crypto_alt avg `0.4829` n `230`; crypto_major avg `1.3169` n `8`; equity avg `0.3043` n `92`; fx avg `-0.0328` n `6`; index avg `0.1788` n `25`; metal avg `0.3102` n `20`; unknown avg `-0.1027` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0833`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
