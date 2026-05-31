# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T01:52:20.348923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `-0.0909` n `228`; crypto_major avg `-0.1338` n `8`; equity avg `0.0031` n `69`; fx avg `0.0183` n `6`; index avg `-0.0121` n `23`; metal avg `0.0019` n `18`; unknown avg `0.8077` n `421`
- 1h: commodity avg `0.1588` n `12`; crypto_alt avg `0.232` n `228`; crypto_major avg `0.3481` n `8`; equity avg `0.0695` n `69`; fx avg `0.019` n `6`; index avg `0.0134` n `23`; metal avg `0.02` n `18`; unknown avg `1.0457` n `421`
- 4h: commodity avg `0.1243` n `12`; crypto_alt avg `-0.2454` n `228`; crypto_major avg `0.3905` n `8`; equity avg `0.1849` n `69`; fx avg `-0.0039` n `6`; index avg `0.0212` n `23`; metal avg `-0.0262` n `18`; unknown avg `0.5235` n `421`
- 24h: commodity avg `-0.1462` n `12`; crypto_alt avg `0.3639` n `228`; crypto_major avg `2.2668` n `8`; equity avg `0.9698` n `69`; fx avg `0.0268` n `6`; index avg `0.0934` n `23`; metal avg `0.0161` n `18`; unknown avg `1.3552` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
