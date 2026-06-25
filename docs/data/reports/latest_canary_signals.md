# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T01:52:26.662422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `12`; crypto_alt avg `0.0575` n `228`; crypto_major avg `0.079` n `8`; equity avg `0.0717` n `86`; fx avg `0.018` n `6`; index avg `0.017` n `23`; metal avg `0.1172` n `20`; unknown avg `0.4582` n `764`
- 1h: commodity avg `-0.1725` n `12`; crypto_alt avg `0.0873` n `228`; crypto_major avg `0.0514` n `8`; equity avg `0.1746` n `86`; fx avg `0.0277` n `6`; index avg `0.0982` n `23`; metal avg `-0.0855` n `20`; unknown avg `0.3457` n `764`
- 4h: commodity avg `-0.1054` n `12`; crypto_alt avg `0.1386` n `228`; crypto_major avg `0.2498` n `8`; equity avg `-0.1293` n `86`; fx avg `0.1184` n `6`; index avg `-0.0193` n `23`; metal avg `-0.218` n `20`; unknown avg `-0.5649` n `748`
- 24h: commodity avg `-0.5578` n `12`; crypto_alt avg `-2.5602` n `228`; crypto_major avg `-2.369` n `8`; equity avg `4.025` n `86`; fx avg `0.108` n `6`; index avg `0.4353` n `23`; metal avg `-1.6536` n `20`; unknown avg `-1.1827` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
