# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T00:22:27.112481+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0185` n `12`; crypto_alt avg `-0.1932` n `229`; crypto_major avg `-0.1426` n `8`; equity avg `0.0683` n `88`; fx avg `-0.0475` n `6`; index avg `0.0475` n `25`; metal avg `0.0657` n `20`; unknown avg `-0.1149` n `765`
- 1h: commodity avg `-0.0093` n `12`; crypto_alt avg `-0.575` n `229`; crypto_major avg `-0.5846` n `8`; equity avg `-0.2508` n `88`; fx avg `0.0365` n `6`; index avg `0.0923` n `25`; metal avg `-0.1524` n `20`; unknown avg `-0.0257` n `765`
- 4h: commodity avg `-0.1506` n `12`; crypto_alt avg `0.2485` n `229`; crypto_major avg `0.6132` n `8`; equity avg `-0.049` n `88`; fx avg `0.1242` n `6`; index avg `0.123` n `25`; metal avg `0.0092` n `20`; unknown avg `0.7867` n `765`
- 24h: commodity avg `-0.1607` n `12`; crypto_alt avg `-0.0013` n `229`; crypto_major avg `0.8777` n `8`; equity avg `0.2927` n `88`; fx avg `0.061` n `6`; index avg `0.1992` n `25`; metal avg `0.0397` n `20`; unknown avg `1.397` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
