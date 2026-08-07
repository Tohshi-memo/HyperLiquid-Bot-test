# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-07T06:51:08.666532+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.039` n `12`; crypto_alt avg `-0.0953` n `230`; crypto_major avg `-0.1322` n `8`; equity avg `-0.1368` n `112`; fx avg `-0.0118` n `6`; index avg `-0.0153` n `25`; metal avg `0.0064` n `20`; unknown avg `0.0074` n `782`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `-0.0298` n `230`; crypto_major avg `0.137` n `8`; equity avg `0.1156` n `112`; fx avg `-0.0327` n `6`; index avg `0.0177` n `25`; metal avg `0.1817` n `20`; unknown avg `0.006` n `766`
- 4h: commodity avg `0.0898` n `12`; crypto_alt avg `-0.0802` n `230`; crypto_major avg `-0.2605` n `8`; equity avg `0.2117` n `112`; fx avg `-0.0424` n `6`; index avg `0.0463` n `25`; metal avg `0.3377` n `20`; unknown avg `-0.0528` n `766`
- 24h: commodity avg `0.5647` n `12`; crypto_alt avg `0.1391` n `230`; crypto_major avg `-1.0701` n `8`; equity avg `1.2984` n `109`; fx avg `-0.1047` n `6`; index avg `-0.0352` n `25`; metal avg `0.3787` n `20`; unknown avg `110.8016` n `765`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
