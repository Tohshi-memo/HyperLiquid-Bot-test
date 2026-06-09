# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T19:22:28.457476+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.2008` n `228`; crypto_major avg `-0.1844` n `8`; equity avg `-0.693` n `74`; fx avg `0.0161` n `6`; index avg `-0.3567` n `23`; metal avg `-0.3718` n `18`; unknown avg `-0.0701` n `547`
- 1h: commodity avg `0.0411` n `12`; crypto_alt avg `-0.1868` n `228`; crypto_major avg `-0.2799` n `8`; equity avg `-0.2704` n `74`; fx avg `-0.0026` n `6`; index avg `0.0981` n `23`; metal avg `-0.3113` n `18`; unknown avg `-0.0867` n `547`
- 4h: commodity avg `0.0844` n `12`; crypto_alt avg `0.366` n `228`; crypto_major avg `0.036` n `8`; equity avg `-0.8248` n `74`; fx avg `-0.0351` n `6`; index avg `-0.8087` n `23`; metal avg `-0.7191` n `18`; unknown avg `-0.2547` n `547`
- 24h: commodity avg `-0.8685` n `12`; crypto_alt avg `-2.6028` n `228`; crypto_major avg `-3.3005` n `8`; equity avg `-2.3929` n `74`; fx avg `0.1158` n `6`; index avg `-1.3735` n `23`; metal avg `-1.5104` n `18`; unknown avg `-1.4716` n `503`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0422`, n `668`, weak_sample_signal
