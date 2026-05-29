# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T04:52:19.261839+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.033` n `12`; crypto_alt avg `-0.0352` n `228`; crypto_major avg `-0.0169` n `8`; equity avg `0.0489` n `69`; fx avg `0.0194` n `6`; index avg `-0.0179` n `23`; metal avg `0.0018` n `18`; unknown avg `0.1431` n `417`
- 1h: commodity avg `-0.1617` n `12`; crypto_alt avg `0.2323` n `228`; crypto_major avg `0.11` n `8`; equity avg `0.3169` n `69`; fx avg `0.0058` n `6`; index avg `0.1108` n `23`; metal avg `0.2529` n `18`; unknown avg `-0.1857` n `417`
- 4h: commodity avg `-0.104` n `12`; crypto_alt avg `-0.8303` n `228`; crypto_major avg `-0.6088` n `8`; equity avg `0.2464` n `69`; fx avg `0.0037` n `6`; index avg `0.0812` n `23`; metal avg `0.1506` n `18`; unknown avg `-0.8209` n `417`
- 24h: commodity avg `-0.2647` n `12`; crypto_alt avg `0.7292` n `228`; crypto_major avg `1.6001` n `8`; equity avg `4.7285` n `69`; fx avg `0.1609` n `6`; index avg `1.7485` n `23`; metal avg `2.7397` n `18`; unknown avg `0.5807` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
