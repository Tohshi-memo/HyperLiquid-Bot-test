# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T06:22:13.177770+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0155` n `12`; crypto_alt avg `-0.1474` n `228`; crypto_major avg `-0.0431` n `8`; equity avg `-0.0133` n `65`; fx avg `0.0` n `5`; index avg `0.0068` n `23`; metal avg `-0.0306` n `18`; unknown avg `0.1927` n `376`
- 1h: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.0879` n `228`; crypto_major avg `-0.0142` n `8`; equity avg `-0.0235` n `65`; fx avg `0.0013` n `5`; index avg `0.0131` n `23`; metal avg `0.0555` n `18`; unknown avg `-0.1051` n `366`
- 4h: commodity avg `-0.1296` n `12`; crypto_alt avg `0.2278` n `228`; crypto_major avg `0.1543` n `8`; equity avg `0.3166` n `65`; fx avg `0.0036` n `5`; index avg `0.0293` n `23`; metal avg `0.2566` n `18`; unknown avg `0.1707` n `366`
- 24h: commodity avg `0.1873` n `12`; crypto_alt avg `-1.5689` n `228`; crypto_major avg `-0.6489` n `8`; equity avg `0.9666` n `65`; fx avg `-0.0244` n `5`; index avg `0.3342` n `23`; metal avg `0.434` n `18`; unknown avg `-0.2971` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
