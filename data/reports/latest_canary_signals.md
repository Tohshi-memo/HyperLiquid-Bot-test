# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T02:22:21.636462+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0606` n `12`; crypto_alt avg `-0.2256` n `228`; crypto_major avg `-0.3334` n `8`; equity avg `-0.0128` n `69`; fx avg `0.0019` n `6`; index avg `0.018` n `23`; metal avg `0.0233` n `18`; unknown avg `-0.1971` n `417`
- 1h: commodity avg `-0.0906` n `12`; crypto_alt avg `0.0163` n `228`; crypto_major avg `-0.3005` n `8`; equity avg `-0.0374` n `69`; fx avg `-0.0167` n `6`; index avg `-0.0179` n `23`; metal avg `-0.3534` n `18`; unknown avg `-0.331` n `417`
- 4h: commodity avg `-0.2921` n `12`; crypto_alt avg `0.2061` n `228`; crypto_major avg `-0.3944` n `8`; equity avg `-0.063` n `69`; fx avg `0.0735` n `6`; index avg `-0.1178` n `23`; metal avg `0.2118` n `18`; unknown avg `-0.4078` n `417`
- 24h: commodity avg `0.4674` n `12`; crypto_alt avg `-1.2639` n `228`; crypto_major avg `0.253` n `8`; equity avg `2.7643` n `69`; fx avg `0.0604` n `6`; index avg `0.9071` n `23`; metal avg `1.8491` n `18`; unknown avg `0.3285` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1551`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1444`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
