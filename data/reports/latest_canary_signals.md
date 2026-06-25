# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T04:37:29.454631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0382` n `12`; crypto_alt avg `-0.0532` n `228`; crypto_major avg `0.0008` n `8`; equity avg `-0.0031` n `86`; fx avg `-0.0031` n `6`; index avg `-0.01` n `23`; metal avg `0.0087` n `20`; unknown avg `-0.2091` n `765`
- 1h: commodity avg `0.053` n `12`; crypto_alt avg `-0.0242` n `228`; crypto_major avg `0.0035` n `8`; equity avg `0.083` n `86`; fx avg `0.0291` n `6`; index avg `0.0031` n `23`; metal avg `0.2379` n `20`; unknown avg `0.8116` n `765`
- 4h: commodity avg `-0.1361` n `12`; crypto_alt avg `-0.1198` n `228`; crypto_major avg `-0.3001` n `8`; equity avg `-0.2076` n `86`; fx avg `0.0211` n `6`; index avg `0.0474` n `23`; metal avg `0.0336` n `20`; unknown avg `0.1362` n `748`
- 24h: commodity avg `-0.4538` n `12`; crypto_alt avg `-1.7485` n `228`; crypto_major avg `-1.7672` n `8`; equity avg `0.2236` n `86`; fx avg `0.0759` n `6`; index avg `0.6351` n `23`; metal avg `-1.383` n `20`; unknown avg `-0.5276` n `708`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
