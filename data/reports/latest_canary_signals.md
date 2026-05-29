# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T13:37:21.609486+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1361` n `12`; crypto_alt avg `0.1777` n `228`; crypto_major avg `0.0718` n `8`; equity avg `-0.0777` n `69`; fx avg `-0.0073` n `6`; index avg `-0.1556` n `23`; metal avg `-0.208` n `18`; unknown avg `-0.0031` n `417`
- 1h: commodity avg `-0.1466` n `12`; crypto_alt avg `-0.1011` n `228`; crypto_major avg `-0.0231` n `8`; equity avg `-0.0876` n `69`; fx avg `0.0231` n `6`; index avg `-0.0762` n `23`; metal avg `0.1773` n `18`; unknown avg `1.1008` n `417`
- 4h: commodity avg `0.184` n `12`; crypto_alt avg `-1.5085` n `228`; crypto_major avg `-1.0075` n `8`; equity avg `-0.4603` n `69`; fx avg `0.0488` n `6`; index avg `-0.0322` n `23`; metal avg `-0.0021` n `18`; unknown avg `-0.0547` n `417`
- 24h: commodity avg `-0.2226` n `12`; crypto_alt avg `0.9581` n `228`; crypto_major avg `1.7786` n `8`; equity avg `3.0261` n `69`; fx avg `0.0915` n `6`; index avg `1.1922` n `23`; metal avg `1.9814` n `18`; unknown avg `1.2206` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
