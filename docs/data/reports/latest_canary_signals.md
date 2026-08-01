# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T05:22:28.250173+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0009` n `12`; crypto_alt avg `-0.0633` n `230`; crypto_major avg `-0.1013` n `8`; equity avg `-0.0103` n `102`; fx avg `0.0036` n `6`; index avg `-0.0371` n `25`; metal avg `0.003` n `20`; unknown avg `-0.0746` n `781`
- 1h: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0043` n `230`; crypto_major avg `-0.0642` n `8`; equity avg `0.0116` n `102`; fx avg `0.0322` n `6`; index avg `-0.0449` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.0161` n `781`
- 4h: commodity avg `-0.0368` n `12`; crypto_alt avg `0.151` n `230`; crypto_major avg `-0.0198` n `8`; equity avg `0.0278` n `102`; fx avg `0.0241` n `6`; index avg `0.0047` n `25`; metal avg `-0.0004` n `20`; unknown avg `0.4745` n `781`
- 24h: commodity avg `0.9712` n `12`; crypto_alt avg `0.3079` n `230`; crypto_major avg `-1.6242` n `8`; equity avg `-2.8536` n `102`; fx avg `-0.0909` n `6`; index avg `-0.3916` n `25`; metal avg `-0.2649` n `20`; unknown avg `4.773` n `747`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
