# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T01:37:26.267200+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0104` n `12`; crypto_alt avg `0.1662` n `229`; crypto_major avg `0.1517` n `8`; equity avg `0.197` n `91`; fx avg `0.0375` n `6`; index avg `0.0539` n `25`; metal avg `-0.041` n `20`; unknown avg `-0.0334` n `765`
- 1h: commodity avg `0.0423` n `12`; crypto_alt avg `0.5825` n `229`; crypto_major avg `0.5617` n `8`; equity avg `0.5815` n `91`; fx avg `-0.0144` n `6`; index avg `0.1331` n `25`; metal avg `0.0727` n `20`; unknown avg `1.5317` n `765`
- 4h: commodity avg `0.0242` n `12`; crypto_alt avg `0.2604` n `229`; crypto_major avg `0.2319` n `8`; equity avg `0.2143` n `91`; fx avg `0.0315` n `6`; index avg `-0.0065` n `25`; metal avg `0.0365` n `20`; unknown avg `-0.3835` n `765`
- 24h: commodity avg `-1.0129` n `12`; crypto_alt avg `0.8699` n `229`; crypto_major avg `0.6457` n `8`; equity avg `1.1368` n `91`; fx avg `0.0537` n `6`; index avg `0.3157` n `25`; metal avg `0.702` n `20`; unknown avg `-0.2388` n `748`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
