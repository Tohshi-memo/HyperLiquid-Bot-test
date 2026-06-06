# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T21:22:27.533004+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0241` n `12`; crypto_alt avg `0.2318` n `228`; crypto_major avg `0.2818` n `8`; equity avg `0.0886` n `74`; fx avg `-0.0071` n `6`; index avg `0.0028` n `23`; metal avg `0.0077` n `18`; unknown avg `0.0674` n `515`
- 1h: commodity avg `0.1291` n `12`; crypto_alt avg `0.5518` n `228`; crypto_major avg `0.6861` n `8`; equity avg `0.1648` n `74`; fx avg `-0.0163` n `6`; index avg `0.1668` n `23`; metal avg `0.0186` n `18`; unknown avg `0.0723` n `515`
- 4h: commodity avg `0.1631` n `12`; crypto_alt avg `0.2747` n `228`; crypto_major avg `0.1382` n `8`; equity avg `0.2744` n `74`; fx avg `0.0132` n `6`; index avg `0.04` n `23`; metal avg `0.0257` n `18`; unknown avg `0.5647` n `515`
- 24h: commodity avg `0.3326` n `12`; crypto_alt avg `-2.441` n `228`; crypto_major avg `-2.0897` n `8`; equity avg `-0.961` n `74`; fx avg `0.0591` n `6`; index avg `0.0161` n `23`; metal avg `-0.5268` n `18`; unknown avg `0.4717` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
