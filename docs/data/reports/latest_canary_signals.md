# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T10:52:20.265868+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1039` n `12`; crypto_alt avg `0.1656` n `228`; crypto_major avg `-0.0543` n `8`; equity avg `-0.0082` n `69`; fx avg `0.0007` n `6`; index avg `0.0012` n `23`; metal avg `0.0014` n `18`; unknown avg `0.0098` n `421`
- 1h: commodity avg `0.1102` n `12`; crypto_alt avg `-0.2608` n `228`; crypto_major avg `-0.2606` n `8`; equity avg `-0.096` n `69`; fx avg `-0.0019` n `6`; index avg `0.0248` n `23`; metal avg `-0.0012` n `18`; unknown avg `-0.2307` n `421`
- 4h: commodity avg `0.2392` n `12`; crypto_alt avg `-0.5953` n `228`; crypto_major avg `-0.6276` n `8`; equity avg `0.0876` n `69`; fx avg `-0.023` n `6`; index avg `-0.0863` n `23`; metal avg `-0.0347` n `18`; unknown avg `-0.1603` n `421`
- 24h: commodity avg `0.2826` n `12`; crypto_alt avg `-0.0973` n `228`; crypto_major avg `1.0467` n `8`; equity avg `1.0031` n `69`; fx avg `0.0168` n `6`; index avg `-0.0707` n `23`; metal avg `-0.0925` n `18`; unknown avg `0.534` n `401`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
