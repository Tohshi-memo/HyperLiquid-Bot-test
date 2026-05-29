# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T00:17:55.348382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.012` n `12`; crypto_alt avg `0.1501` n `228`; crypto_major avg `0.2276` n `8`; equity avg `0.0879` n `69`; fx avg `0.0018` n `6`; index avg `0.0657` n `23`; metal avg `0.1227` n `18`; unknown avg `-0.0396` n `417`
- 1h: commodity avg `-0.1439` n `12`; crypto_alt avg `0.4312` n `228`; crypto_major avg `0.2328` n `8`; equity avg `0.0617` n `69`; fx avg `0.0507` n `6`; index avg `0.0245` n `23`; metal avg `0.1376` n `18`; unknown avg `0.3575` n `417`
- 4h: commodity avg `-0.29` n `12`; crypto_alt avg `0.1176` n `228`; crypto_major avg `0.1778` n `8`; equity avg `0.58` n `69`; fx avg `0.0481` n `6`; index avg `0.0557` n `23`; metal avg `0.151` n `18`; unknown avg `-0.2436` n `417`
- 24h: commodity avg `0.4152` n `12`; crypto_alt avg `-1.737` n `228`; crypto_major avg `0.3849` n `8`; equity avg `2.8662` n `69`; fx avg `0.0179` n `6`; index avg `1.0201` n `23`; metal avg `0.6579` n `18`; unknown avg `0.1583` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
