# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T20:52:17.148066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0583` n `12`; crypto_alt avg `0.1559` n `228`; crypto_major avg `0.0643` n `8`; equity avg `0.0385` n `69`; fx avg `0.0007` n `6`; index avg `-0.0091` n `23`; metal avg `-0.0169` n `18`; unknown avg `0.0634` n `417`
- 1h: commodity avg `0.0925` n `12`; crypto_alt avg `0.3811` n `228`; crypto_major avg `0.1099` n `8`; equity avg `0.0622` n `69`; fx avg `0.0063` n `6`; index avg `-0.1773` n `23`; metal avg `0.0115` n `18`; unknown avg `0.3823` n `417`
- 4h: commodity avg `0.444` n `12`; crypto_alt avg `0.8953` n `228`; crypto_major avg `0.6957` n `8`; equity avg `0.7054` n `69`; fx avg `0.0055` n `6`; index avg `-0.2536` n `23`; metal avg `-0.1759` n `18`; unknown avg `0.5397` n `417`
- 24h: commodity avg `1.0001` n `12`; crypto_alt avg `-3.3128` n `228`; crypto_major avg `-1.1058` n `8`; equity avg `1.6006` n `69`; fx avg `-0.0195` n `6`; index avg `0.6555` n `23`; metal avg `0.5227` n `18`; unknown avg `-0.6801` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1211`, n `668`, weak_sample_signal
