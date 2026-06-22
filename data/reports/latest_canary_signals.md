# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T17:07:39.108746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0398` n `12`; crypto_alt avg `0.0295` n `228`; crypto_major avg `0.0625` n `8`; equity avg `-0.1555` n `85`; fx avg `-0.0031` n `6`; index avg `-0.0182` n `23`; metal avg `-0.0041` n `20`; unknown avg `-0.2222` n `717`
- 1h: commodity avg `0.0464` n `12`; crypto_alt avg `0.148` n `228`; crypto_major avg `0.1876` n `8`; equity avg `-0.1409` n `85`; fx avg `-0.0163` n `6`; index avg `0.0215` n `23`; metal avg `0.1087` n `20`; unknown avg `-0.3115` n `717`
- 4h: commodity avg `-0.2709` n `12`; crypto_alt avg `-0.9217` n `228`; crypto_major avg `-1.0247` n `8`; equity avg `-1.0554` n `85`; fx avg `-0.0595` n `6`; index avg `-0.048` n `23`; metal avg `-0.176` n `20`; unknown avg `-0.0229` n `716`
- 24h: commodity avg `-0.8321` n `12`; crypto_alt avg `-0.4829` n `228`; crypto_major avg `-0.2693` n `8`; equity avg `-0.7962` n `85`; fx avg `0.045` n `6`; index avg `0.1081` n `23`; metal avg `0.2223` n `18`; unknown avg `0.6846` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
