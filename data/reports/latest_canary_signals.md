# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T13:22:28.047675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0011` n `12`; crypto_alt avg `0.0238` n `228`; crypto_major avg `-0.0357` n `8`; equity avg `0.1041` n `74`; fx avg `0.0066` n `6`; index avg `-0.0184` n `23`; metal avg `0.0076` n `18`; unknown avg `0.0156` n `417`
- 1h: commodity avg `0.0613` n `12`; crypto_alt avg `0.7697` n `228`; crypto_major avg `0.43` n `8`; equity avg `0.3396` n `74`; fx avg `0.004` n `6`; index avg `0.2619` n `23`; metal avg `0.0653` n `18`; unknown avg `0.3066` n `417`
- 4h: commodity avg `0.0345` n `12`; crypto_alt avg `-0.2188` n `228`; crypto_major avg `-0.3954` n `8`; equity avg `-0.9065` n `74`; fx avg `0.0189` n `6`; index avg `0.1689` n `23`; metal avg `0.0097` n `18`; unknown avg `1.1878` n `413`
- 24h: commodity avg `-0.7241` n `12`; crypto_alt avg `-3.3513` n `228`; crypto_major avg `-3.5122` n `8`; equity avg `-5.4082` n `74`; fx avg `-0.2444` n `6`; index avg `-3.2993` n `23`; metal avg `-3.4341` n `18`; unknown avg `-0.5975` n `402`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
