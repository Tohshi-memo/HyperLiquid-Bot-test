# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T17:07:40.722121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.2` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.5331` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0428` n `12`; crypto_alt avg `-0.4835` n `228`; crypto_major avg `-0.4552` n `8`; equity avg `-0.0124` n `77`; fx avg `0.0079` n `6`; index avg `-0.0428` n `23`; metal avg `-0.0796` n `18`; unknown avg `0.1792` n `687`
- 1h: commodity avg `0.267` n `12`; crypto_alt avg `-0.7949` n `228`; crypto_major avg `-0.0963` n `8`; equity avg `-0.1131` n `77`; fx avg `0.0041` n `6`; index avg `-0.1249` n `23`; metal avg `-0.4005` n `18`; unknown avg `0.5241` n `687`
- 4h: commodity avg `0.4615` n `12`; crypto_alt avg `-0.0502` n `228`; crypto_major avg `0.9986` n `8`; equity avg `1.2984` n `76`; fx avg `0.0036` n `6`; index avg `0.3745` n `23`; metal avg `-0.5345` n `18`; unknown avg `0.9674` n `687`
- 24h: commodity avg `-0.6709` n `12`; crypto_alt avg `5.59` n `228`; crypto_major avg `7.2295` n `8`; equity avg `2.9867` n `76`; fx avg `0.0532` n `6`; index avg `1.2799` n `23`; metal avg `2.236` n `18`; unknown avg `2.9024` n `527`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1497`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1464`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1343`, n `669`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1123`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0912`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0903`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0834`, n `669`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.067`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0654`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `669`, weak_sample_signal
