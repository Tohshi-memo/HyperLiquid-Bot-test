# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T19:07:26.480088+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `-0.0311` n `229`; crypto_major avg `-0.1608` n `8`; equity avg `0.0007` n `88`; fx avg `-0.0046` n `6`; index avg `0.0027` n `25`; metal avg `-0.012` n `20`; unknown avg `0.8509` n `765`
- 1h: commodity avg `-0.0388` n `12`; crypto_alt avg `0.1312` n `229`; crypto_major avg `0.1349` n `8`; equity avg `0.0633` n `88`; fx avg `-0.0076` n `6`; index avg `0.0192` n `25`; metal avg `-0.0035` n `20`; unknown avg `0.8477` n `765`
- 4h: commodity avg `-0.0273` n `12`; crypto_alt avg `0.0402` n `229`; crypto_major avg `-0.1906` n `8`; equity avg `0.0661` n `88`; fx avg `-0.0009` n `6`; index avg `0.009` n `25`; metal avg `-0.0124` n `20`; unknown avg `0.9194` n `695`
- 24h: commodity avg `0.002` n `12`; crypto_alt avg `-1.2082` n `229`; crypto_major avg `-0.7471` n `8`; equity avg `0.394` n `88`; fx avg `-0.0829` n `6`; index avg `0.114` n `25`; metal avg `0.0505` n `20`; unknown avg `0.9504` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1032`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
