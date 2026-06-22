# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T23:52:25.270693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0015` n `12`; crypto_alt avg `-0.0869` n `228`; crypto_major avg `-0.0381` n `8`; equity avg `-0.0345` n `86`; fx avg `0.0026` n `6`; index avg `-0.0457` n `23`; metal avg `-0.0692` n `20`; unknown avg `1.5675` n `716`
- 1h: commodity avg `-0.0422` n `12`; crypto_alt avg `0.0996` n `228`; crypto_major avg `0.1016` n `8`; equity avg `-0.0949` n `86`; fx avg `0.0465` n `6`; index avg `-0.0682` n `23`; metal avg `-0.0204` n `20`; unknown avg `1.1549` n `716`
- 4h: commodity avg `-0.0587` n `12`; crypto_alt avg `-0.7915` n `228`; crypto_major avg `-0.5363` n `8`; equity avg `-0.2773` n `86`; fx avg `0.0175` n `6`; index avg `-0.0681` n `23`; metal avg `-0.0138` n `20`; unknown avg `-0.2256` n `708`
- 24h: commodity avg `-0.8872` n `12`; crypto_alt avg `-0.1322` n `228`; crypto_major avg `0.3378` n `8`; equity avg `-0.0739` n `85`; fx avg `0.1071` n `6`; index avg `0.1942` n `23`; metal avg `0.47` n `18`; unknown avg `0.6793` n `631`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1142`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
