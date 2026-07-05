# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T05:07:25.365300+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `12`; crypto_alt avg `-0.1262` n `229`; crypto_major avg `-0.1847` n `8`; equity avg `-0.0143` n `88`; fx avg `-0.0015` n `6`; index avg `0.0549` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.1778` n `765`
- 1h: commodity avg `0.0042` n `12`; crypto_alt avg `0.0101` n `229`; crypto_major avg `-0.0378` n `8`; equity avg `0.0501` n `88`; fx avg `-0.0015` n `6`; index avg `0.0529` n `25`; metal avg `0.0015` n `20`; unknown avg `1.5791` n `765`
- 4h: commodity avg `0.031` n `12`; crypto_alt avg `-0.8813` n `229`; crypto_major avg `-0.7861` n `8`; equity avg `0.1134` n `88`; fx avg `0.0001` n `6`; index avg `0.0156` n `25`; metal avg `-0.0205` n `20`; unknown avg `-0.4937` n `763`
- 24h: commodity avg `0.0796` n `12`; crypto_alt avg `-0.9572` n `229`; crypto_major avg `-1.1478` n `8`; equity avg `0.2002` n `88`; fx avg `-0.0099` n `6`; index avg `0.0597` n `25`; metal avg `0.072` n `20`; unknown avg `-0.913` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0964`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
