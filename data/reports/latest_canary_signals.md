# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T22:14:32.370038+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `12`; crypto_alt avg `-0.2576` n `228`; crypto_major avg `-0.4528` n `8`; equity avg `-0.1083` n `74`; fx avg `-0.0026` n `6`; index avg `-0.0526` n `23`; metal avg `0.0076` n `18`; unknown avg `-0.1118` n `515`
- 1h: commodity avg `0.0041` n `12`; crypto_alt avg `0.0358` n `228`; crypto_major avg `-0.2498` n `8`; equity avg `-0.0713` n `74`; fx avg `-0.0171` n `6`; index avg `-0.0528` n `23`; metal avg `0.0119` n `18`; unknown avg `0.1993` n `515`
- 4h: commodity avg `0.072` n `12`; crypto_alt avg `0.5394` n `228`; crypto_major avg `0.0727` n `8`; equity avg `0.2576` n `74`; fx avg `-0.1245` n `6`; index avg `0.0619` n `23`; metal avg `0.0139` n `18`; unknown avg `-0.1021` n `515`
- 24h: commodity avg `0.8747` n `12`; crypto_alt avg `-2.0826` n `228`; crypto_major avg `-1.9751` n `8`; equity avg `-1.2191` n `74`; fx avg `0.0223` n `6`; index avg `-0.1037` n `23`; metal avg `-0.583` n `18`; unknown avg `-0.6292` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
