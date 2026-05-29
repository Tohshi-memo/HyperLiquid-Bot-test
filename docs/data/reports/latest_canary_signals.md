# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T00:37:19.238144+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0764` n `12`; crypto_alt avg `0.1864` n `228`; crypto_major avg `0.0211` n `8`; equity avg `-0.0655` n `69`; fx avg `0.0152` n `6`; index avg `-0.0725` n `23`; metal avg `-0.1671` n `18`; unknown avg `0.0262` n `417`
- 1h: commodity avg `-0.1825` n `12`; crypto_alt avg `0.4918` n `228`; crypto_major avg `0.175` n `8`; equity avg `-0.0275` n `69`; fx avg `0.0605` n `6`; index avg `-0.0599` n `23`; metal avg `-0.0658` n `18`; unknown avg `0.3917` n `417`
- 4h: commodity avg `-0.3529` n `12`; crypto_alt avg `0.196` n `228`; crypto_major avg `0.1442` n `8`; equity avg `0.5115` n `69`; fx avg `0.0625` n `6`; index avg `-0.0092` n `23`; metal avg `-0.0316` n `18`; unknown avg `-0.1702` n `417`
- 24h: commodity avg `0.276` n `12`; crypto_alt avg `-1.3534` n `228`; crypto_major avg `0.4537` n `8`; equity avg `2.794` n `69`; fx avg `0.0268` n `6`; index avg `0.9475` n `23`; metal avg `0.5185` n `18`; unknown avg `0.3119` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1611`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
