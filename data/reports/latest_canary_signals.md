# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T06:34:09.316304+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0749` n `12`; crypto_alt avg `-0.0176` n `228`; crypto_major avg `-0.0442` n `8`; equity avg `0.0007` n `69`; fx avg `0.0116` n `6`; index avg `0.0041` n `23`; metal avg `0.0095` n `18`; unknown avg `1.1868` n `421`
- 1h: commodity avg `-0.0103` n `12`; crypto_alt avg `-0.3066` n `228`; crypto_major avg `-0.2075` n `8`; equity avg `0.0829` n `69`; fx avg `0.011` n `6`; index avg `-0.0687` n `23`; metal avg `-0.0213` n `18`; unknown avg `-0.102` n `401`
- 4h: commodity avg `0.0804` n `12`; crypto_alt avg `0.2564` n `228`; crypto_major avg `0.2587` n `8`; equity avg `0.2227` n `69`; fx avg `0.0255` n `6`; index avg `0.0113` n `23`; metal avg `0.0095` n `18`; unknown avg `0.0722` n `401`
- 24h: commodity avg `0.0676` n `12`; crypto_alt avg `0.2515` n `228`; crypto_major avg `2.112` n `8`; equity avg `0.9802` n `69`; fx avg `0.0522` n `6`; index avg `-0.0224` n `23`; metal avg `-0.0344` n `18`; unknown avg `1.3222` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
