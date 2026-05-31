# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T11:52:21.593748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `-0.0697` n `228`; crypto_major avg `0.0397` n `8`; equity avg `-0.0179` n `69`; fx avg `0.0` n `6`; index avg `-0.037` n `23`; metal avg `0.0004` n `18`; unknown avg `0.8086` n `421`
- 1h: commodity avg `0.0587` n `12`; crypto_alt avg `0.1425` n `228`; crypto_major avg `0.1154` n `8`; equity avg `0.0353` n `69`; fx avg `-0.0216` n `6`; index avg `-0.0952` n `23`; metal avg `-0.0064` n `18`; unknown avg `0.9636` n `421`
- 4h: commodity avg `0.1243` n `12`; crypto_alt avg `0.25` n `228`; crypto_major avg `-0.0878` n `8`; equity avg `-0.1075` n `69`; fx avg `-0.0241` n `6`; index avg `-0.164` n `23`; metal avg `-0.0305` n `18`; unknown avg `-0.024` n `421`
- 24h: commodity avg `0.316` n `12`; crypto_alt avg `0.1807` n `228`; crypto_major avg `1.1158` n `8`; equity avg `1.0278` n `69`; fx avg `-0.0025` n `6`; index avg `-0.1716` n `23`; metal avg `-0.0787` n `18`; unknown avg `1.4857` n `401`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0911`, n `668`, weak_sample_signal
