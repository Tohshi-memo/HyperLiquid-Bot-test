# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T19:37:21.480842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2412` n `12`; crypto_alt avg `-0.1112` n `228`; crypto_major avg `-0.0524` n `8`; equity avg `0.2127` n `69`; fx avg `-0.0004` n `6`; index avg `0.0716` n `23`; metal avg `0.0436` n `18`; unknown avg `0.0568` n `417`
- 1h: commodity avg `-0.3872` n `12`; crypto_alt avg `-0.1694` n `228`; crypto_major avg `-0.0847` n `8`; equity avg `0.1151` n `69`; fx avg `-0.0136` n `6`; index avg `0.0461` n `23`; metal avg `0.0193` n `18`; unknown avg `0.2455` n `417`
- 4h: commodity avg `-0.1522` n `12`; crypto_alt avg `1.6185` n `228`; crypto_major avg `1.6066` n `8`; equity avg `0.7098` n `69`; fx avg `-0.0146` n `6`; index avg `0.1359` n `23`; metal avg `0.5044` n `18`; unknown avg `0.5889` n `417`
- 24h: commodity avg `0.7943` n `12`; crypto_alt avg `-3.7995` n `228`; crypto_major avg `-1.2664` n `8`; equity avg `1.6876` n `69`; fx avg `-0.0353` n `6`; index avg `0.9742` n `23`; metal avg `0.5897` n `18`; unknown avg `-0.7834` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1914`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1416`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
