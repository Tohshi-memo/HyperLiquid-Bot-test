# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T22:44:21.111859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0313` n `12`; crypto_alt avg `-0.2214` n `229`; crypto_major avg `-0.2227` n `8`; equity avg `0.0323` n `88`; fx avg `0.0061` n `6`; index avg `0.0128` n `25`; metal avg `0.0881` n `20`; unknown avg `0.3392` n `765`
- 1h: commodity avg `-0.1322` n `12`; crypto_alt avg `0.2303` n `229`; crypto_major avg `0.5607` n `8`; equity avg `0.133` n `88`; fx avg `0.0811` n `6`; index avg `-0.0014` n `25`; metal avg `0.1342` n `20`; unknown avg `1.0084` n `765`
- 4h: commodity avg `-0.1565` n `12`; crypto_alt avg `0.7046` n `229`; crypto_major avg `1.137` n `8`; equity avg `0.2042` n `88`; fx avg `0.0876` n `6`; index avg `-0.0043` n `25`; metal avg `0.14` n `20`; unknown avg `1.8533` n `765`
- 24h: commodity avg `-0.1377` n `12`; crypto_alt avg `-0.1681` n `229`; crypto_major avg `0.5673` n `8`; equity avg `0.4627` n `88`; fx avg `0.03` n `6`; index avg `0.0641` n `25`; metal avg `0.1564` n `20`; unknown avg `1.3827` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0547`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
