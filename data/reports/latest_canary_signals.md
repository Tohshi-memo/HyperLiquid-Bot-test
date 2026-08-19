# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T12:52:28.051323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.0916` n `230`; crypto_major avg `0.3661` n `8`; equity avg `0.5424` n `120`; fx avg `0.0424` n `6`; index avg `0.0733` n `25`; metal avg `0.0702` n `20`; unknown avg `-0.0589` n `792`
- 1h: commodity avg `-0.0781` n `12`; crypto_alt avg `0.309` n `230`; crypto_major avg `0.5741` n `8`; equity avg `1.4259` n `120`; fx avg `-0.0236` n `6`; index avg `0.2127` n `25`; metal avg `0.3534` n `20`; unknown avg `-0.0484` n `792`
- 4h: commodity avg `0.0501` n `12`; crypto_alt avg `0.3901` n `230`; crypto_major avg `0.6467` n `8`; equity avg `0.4469` n `120`; fx avg `-0.0609` n `6`; index avg `0.1064` n `25`; metal avg `0.4119` n `20`; unknown avg `0.0749` n `789`
- 24h: commodity avg `0.3124` n `12`; crypto_alt avg `0.6155` n `230`; crypto_major avg `1.0128` n `8`; equity avg `-0.6818` n `120`; fx avg `-0.2323` n `6`; index avg `-0.0389` n `25`; metal avg `-0.1176` n `20`; unknown avg `-0.0086` n `757`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
