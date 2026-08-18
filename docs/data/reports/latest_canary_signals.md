# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T19:56:49.674436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0304` n `12`; crypto_alt avg `-0.1648` n `230`; crypto_major avg `-0.1086` n `8`; equity avg `-0.1394` n `120`; fx avg `-0.002` n `6`; index avg `-0.0129` n `25`; metal avg `-0.0896` n `20`; unknown avg `0.042` n `789`
- 1h: commodity avg `0.012` n `12`; crypto_alt avg `-0.2003` n `230`; crypto_major avg `-0.0598` n `8`; equity avg `-0.0996` n `120`; fx avg `0.0065` n `6`; index avg `0.0004` n `25`; metal avg `-0.0997` n `20`; unknown avg `-0.0188` n `789`
- 4h: commodity avg `0.0248` n `12`; crypto_alt avg `-0.4229` n `230`; crypto_major avg `-0.1822` n `8`; equity avg `-0.5396` n `120`; fx avg `0.0003` n `6`; index avg `-0.0371` n `25`; metal avg `-0.1729` n `20`; unknown avg `0.18` n `789`
- 24h: commodity avg `0.3034` n `12`; crypto_alt avg `-0.6313` n `230`; crypto_major avg `0.314` n `8`; equity avg `-4.453` n `120`; fx avg `-0.0361` n `6`; index avg `-0.6697` n `25`; metal avg `-0.7685` n `20`; unknown avg `-0.2587` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
