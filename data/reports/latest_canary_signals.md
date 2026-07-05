# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T22:37:29.075783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0894` n `229`; crypto_major avg `-0.0701` n `8`; equity avg `0.055` n `88`; fx avg `0.0061` n `6`; index avg `0.0167` n `25`; metal avg `0.0957` n `20`; unknown avg `0.3557` n `765`
- 1h: commodity avg `-0.1072` n `12`; crypto_alt avg `0.3634` n `229`; crypto_major avg `0.7149` n `8`; equity avg `0.156` n `88`; fx avg `0.0811` n `6`; index avg `0.0025` n `25`; metal avg `0.1418` n `20`; unknown avg `1.3351` n `765`
- 4h: commodity avg `-0.1314` n `12`; crypto_alt avg `0.838` n `229`; crypto_major avg `1.292` n `8`; equity avg `0.2271` n `88`; fx avg `0.0876` n `6`; index avg `-0.0004` n `25`; metal avg `0.1476` n `20`; unknown avg `2.1981` n `765`
- 24h: commodity avg `-0.1126` n `12`; crypto_alt avg `-0.0361` n `229`; crypto_major avg `0.7209` n `8`; equity avg `0.486` n `88`; fx avg `0.03` n `6`; index avg `0.068` n `25`; metal avg `0.164` n `20`; unknown avg `1.3689` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
