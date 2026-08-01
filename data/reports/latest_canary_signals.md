# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T10:37:25.612813+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.1021` n `230`; crypto_major avg `-0.087` n `8`; equity avg `-0.0013` n `102`; fx avg `0.0102` n `6`; index avg `0.0099` n `25`; metal avg `0.0211` n `20`; unknown avg `-0.0251` n `781`
- 1h: commodity avg `0.0223` n `12`; crypto_alt avg `-0.2604` n `230`; crypto_major avg `-0.2185` n `8`; equity avg `-0.0377` n `102`; fx avg `0.0025` n `6`; index avg `0.0272` n `25`; metal avg `0.0146` n `20`; unknown avg `0.0037` n `781`
- 4h: commodity avg `0.0424` n `12`; crypto_alt avg `-0.4241` n `230`; crypto_major avg `-0.3128` n `8`; equity avg `-0.1007` n `102`; fx avg `0.001` n `6`; index avg `0.0265` n `25`; metal avg `0.0271` n `20`; unknown avg `-0.0828` n `781`
- 24h: commodity avg `0.4856` n `12`; crypto_alt avg `0.0633` n `230`; crypto_major avg `-1.2975` n `8`; equity avg `-2.707` n `102`; fx avg `-0.0608` n `6`; index avg `-0.3019` n `25`; metal avg `-0.0617` n `20`; unknown avg `4.742` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0644`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
