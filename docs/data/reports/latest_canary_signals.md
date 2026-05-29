# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T02:37:22.169386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `-0.1107` n `228`; crypto_major avg `-0.0229` n `8`; equity avg `-0.0092` n `69`; fx avg `-0.0064` n `6`; index avg `-0.0128` n `23`; metal avg `-0.1051` n `18`; unknown avg `-0.1009` n `417`
- 1h: commodity avg `-0.1634` n `12`; crypto_alt avg `-0.0709` n `228`; crypto_major avg `-0.1943` n `8`; equity avg `-0.0247` n `69`; fx avg `-0.0216` n `6`; index avg `0.0314` n `23`; metal avg `-0.2458` n `18`; unknown avg `-0.2196` n `417`
- 4h: commodity avg `-0.3151` n `12`; crypto_alt avg `0.3757` n `228`; crypto_major avg `-0.2553` n `8`; equity avg `0.024` n `69`; fx avg `0.0652` n `6`; index avg `-0.0572` n `23`; metal avg `0.0923` n `18`; unknown avg `-0.2907` n `417`
- 24h: commodity avg `0.4458` n `12`; crypto_alt avg `-1.3342` n `228`; crypto_major avg `0.2086` n `8`; equity avg `2.779` n `69`; fx avg `0.0568` n `6`; index avg `0.9067` n `23`; metal avg `1.5718` n `18`; unknown avg `0.1297` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1666`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1277`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
