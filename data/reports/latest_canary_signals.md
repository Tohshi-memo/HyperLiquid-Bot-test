# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-23T01:37:24.276515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0497` n `12`; crypto_alt avg `-0.0917` n `230`; crypto_major avg `-0.1928` n `8`; equity avg `-0.0003` n `98`; fx avg `-0.0031` n `6`; index avg `0.009` n `25`; metal avg `-0.105` n `20`; unknown avg `0.1005` n `773`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `-0.3302` n `230`; crypto_major avg `-0.4921` n `8`; equity avg `0.0792` n `98`; fx avg `-0.0294` n `6`; index avg `0.0308` n `25`; metal avg `0.0134` n `20`; unknown avg `0.4263` n `773`
- 4h: commodity avg `0.1908` n `12`; crypto_alt avg `-0.3333` n `230`; crypto_major avg `-0.2529` n `8`; equity avg `0.2257` n `98`; fx avg `-0.0598` n `6`; index avg `0.1088` n `25`; metal avg `-0.0069` n `20`; unknown avg `-0.0031` n `773`
- 24h: commodity avg `0.5685` n `12`; crypto_alt avg `-0.6234` n `230`; crypto_major avg `-0.9368` n `8`; equity avg `-0.5334` n `98`; fx avg `-0.1018` n `6`; index avg `-0.065` n `25`; metal avg `-0.1275` n `20`; unknown avg `1.7481` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0721`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0704`, n `666`, weak_sample_signal
