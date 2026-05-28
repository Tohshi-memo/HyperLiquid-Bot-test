# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T22:07:18.307760+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0598` n `12`; crypto_alt avg `-0.2129` n `228`; crypto_major avg `-0.1616` n `8`; equity avg `0.0938` n `69`; fx avg `0.0032` n `6`; index avg `0.079` n `23`; metal avg `0.0843` n `18`; unknown avg `0.0232` n `417`
- 1h: commodity avg `-0.207` n `12`; crypto_alt avg `0.0424` n `228`; crypto_major avg `0.2686` n `8`; equity avg `0.2276` n `69`; fx avg `-0.013` n `6`; index avg `0.0334` n `23`; metal avg `0.0932` n `18`; unknown avg `0.0759` n `417`
- 4h: commodity avg `0.1281` n `12`; crypto_alt avg `-0.2372` n `228`; crypto_major avg `0.1485` n `8`; equity avg `0.5016` n `69`; fx avg `0.0052` n `6`; index avg `-0.1713` n `23`; metal avg `-0.1519` n `18`; unknown avg `0.2895` n `417`
- 24h: commodity avg `0.9123` n `12`; crypto_alt avg `-1.963` n `228`; crypto_major avg `-0.1363` n `8`; equity avg `2.0624` n `69`; fx avg `-0.0089` n `6`; index avg `0.7139` n `23`; metal avg `0.4792` n `18`; unknown avg `-0.0508` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1816`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1547`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
