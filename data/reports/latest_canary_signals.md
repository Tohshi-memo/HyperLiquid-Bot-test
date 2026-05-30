# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T13:52:18.364223+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0465` n `12`; crypto_alt avg `0.2004` n `228`; crypto_major avg `0.156` n `8`; equity avg `0.0249` n `69`; fx avg `0.0006` n `6`; index avg `0.012` n `23`; metal avg `-0.0` n `18`; unknown avg `-0.1917` n `421`
- 1h: commodity avg `0.077` n `12`; crypto_alt avg `0.0161` n `228`; crypto_major avg `0.102` n `8`; equity avg `0.0945` n `69`; fx avg `-0.0137` n `6`; index avg `0.0317` n `23`; metal avg `-0.027` n `18`; unknown avg `-0.1312` n `421`
- 4h: commodity avg `0.3059` n `12`; crypto_alt avg `-0.0379` n `228`; crypto_major avg `0.3062` n `8`; equity avg `0.3041` n `69`; fx avg `0.0026` n `6`; index avg `0.079` n `23`; metal avg `-0.0398` n `18`; unknown avg `-0.0693` n `421`
- 24h: commodity avg `-0.091` n `12`; crypto_alt avg `2.448` n `228`; crypto_major avg `2.8972` n `8`; equity avg `1.5604` n `69`; fx avg `0.0755` n `6`; index avg `0.0921` n `23`; metal avg `-0.1703` n `18`; unknown avg `0.2741` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
