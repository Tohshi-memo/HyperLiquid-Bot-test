# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T03:52:17.597579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1557` n `12`; crypto_alt avg `-0.21` n `228`; crypto_major avg `-0.102` n `8`; equity avg `-0.0351` n `69`; fx avg `0.0029` n `6`; index avg `0.0246` n `23`; metal avg `0.0058` n `18`; unknown avg `-0.2012` n `417`
- 1h: commodity avg `0.1236` n `12`; crypto_alt avg `-0.19` n `228`; crypto_major avg `0.1261` n `8`; equity avg `0.2127` n `69`; fx avg `0.0102` n `6`; index avg `0.024` n `23`; metal avg `-0.2269` n `18`; unknown avg `0.106` n `417`
- 4h: commodity avg `-0.0651` n `12`; crypto_alt avg `-0.3827` n `228`; crypto_major avg `-0.3537` n `8`; equity avg `-0.0522` n `69`; fx avg `0.0553` n `6`; index avg `-0.0764` n `23`; metal avg `-0.0875` n `18`; unknown avg `-0.505` n `417`
- 24h: commodity avg `-0.1408` n `12`; crypto_alt avg `-0.2353` n `228`; crypto_major avg `1.441` n `8`; equity avg `4.1954` n `69`; fx avg `0.1083` n `6`; index avg `1.4132` n `23`; metal avg `2.1862` n `18`; unknown avg `0.4556` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1236`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
