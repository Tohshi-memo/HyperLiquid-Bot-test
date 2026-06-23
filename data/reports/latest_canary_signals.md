# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T17:07:35.020925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0498` n `12`; crypto_alt avg `-0.2558` n `228`; crypto_major avg `-0.2346` n `8`; equity avg `-0.1968` n `86`; fx avg `-0.0067` n `6`; index avg `-0.0373` n `23`; metal avg `-0.0344` n `20`; unknown avg `-0.4225` n `764`
- 1h: commodity avg `-0.0973` n `12`; crypto_alt avg `-0.5529` n `228`; crypto_major avg `-0.5562` n `8`; equity avg `-0.3424` n `86`; fx avg `0.0071` n `6`; index avg `-0.0423` n `23`; metal avg `-0.0696` n `20`; unknown avg `-0.4177` n `764`
- 4h: commodity avg `-0.2473` n `12`; crypto_alt avg `-0.0657` n `228`; crypto_major avg `-0.2252` n `8`; equity avg `1.0482` n `86`; fx avg `-0.0711` n `6`; index avg `0.0921` n `23`; metal avg `0.0903` n `20`; unknown avg `-0.547` n `764`
- 24h: commodity avg `-0.5002` n `12`; crypto_alt avg `-4.0198` n `228`; crypto_major avg `-4.2637` n `8`; equity avg `-2.8834` n `86`; fx avg `-0.1811` n `6`; index avg `-0.905` n `23`; metal avg `-0.9915` n `20`; unknown avg `-0.1041` n `604`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
