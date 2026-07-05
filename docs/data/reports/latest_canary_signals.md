# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T05:52:25.292637+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `-0.0785` n `229`; crypto_major avg `0.0021` n `8`; equity avg `0.0034` n `88`; fx avg `0.0005` n `6`; index avg `-0.0079` n `25`; metal avg `-0.0012` n `20`; unknown avg `-0.1425` n `765`
- 1h: commodity avg `0.0006` n `12`; crypto_alt avg `-0.2586` n `229`; crypto_major avg `-0.2132` n `8`; equity avg `0.0169` n `88`; fx avg `0.0003` n `6`; index avg `0.0376` n `25`; metal avg `-0.0076` n `20`; unknown avg `0.6571` n `765`
- 4h: commodity avg `0.0193` n `12`; crypto_alt avg `-0.5407` n `229`; crypto_major avg `-0.3987` n `8`; equity avg `0.1225` n `88`; fx avg `-0.0038` n `6`; index avg `0.037` n `25`; metal avg `-0.0261` n `20`; unknown avg `-0.4324` n `765`
- 24h: commodity avg `0.0708` n `12`; crypto_alt avg `-1.0616` n `229`; crypto_major avg `-1.1818` n `8`; equity avg `0.1612` n `88`; fx avg `-0.0108` n `6`; index avg `0.0636` n `25`; metal avg `0.0696` n `20`; unknown avg `-1.0022` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
