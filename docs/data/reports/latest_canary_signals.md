# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T21:07:25.186332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0218` n `12`; crypto_alt avg `-0.1497` n `229`; crypto_major avg `-0.0624` n `8`; equity avg `-0.0189` n `88`; fx avg `0.0399` n `6`; index avg `0.0002` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0272` n `765`
- 1h: commodity avg `-0.0075` n `12`; crypto_alt avg `-0.2423` n `229`; crypto_major avg `-0.1304` n `8`; equity avg `-0.0239` n `88`; fx avg `0.0296` n `6`; index avg `-0.0062` n `25`; metal avg `0.0097` n `20`; unknown avg `-0.1307` n `765`
- 4h: commodity avg `-0.0555` n `12`; crypto_alt avg `0.114` n `229`; crypto_major avg `0.1371` n `8`; equity avg `0.1034` n `88`; fx avg `0.019` n `6`; index avg `0.0007` n `25`; metal avg `0.0181` n `20`; unknown avg `0.7222` n `765`
- 24h: commodity avg `-0.0153` n `12`; crypto_alt avg `-1.1778` n `229`; crypto_major avg `-0.4533` n `8`; equity avg `0.3176` n `88`; fx avg `-0.0306` n `6`; index avg `0.0949` n `25`; metal avg `0.0318` n `20`; unknown avg `1.2109` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
