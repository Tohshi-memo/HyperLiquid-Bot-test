# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T15:37:18.998784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0629` n `12`; crypto_alt avg `0.1643` n `228`; crypto_major avg `0.0021` n `8`; equity avg `0.0697` n `69`; fx avg `-0.0026` n `6`; index avg `0.063` n `23`; metal avg `-0.0056` n `18`; unknown avg `-0.0237` n `421`
- 1h: commodity avg `0.061` n `12`; crypto_alt avg `0.294` n `228`; crypto_major avg `0.1476` n `8`; equity avg `0.0975` n `69`; fx avg `-0.0001` n `6`; index avg `0.0609` n `23`; metal avg `-0.0401` n `18`; unknown avg `0.1712` n `421`
- 4h: commodity avg `0.1309` n `12`; crypto_alt avg `-0.6155` n `228`; crypto_major avg `-0.0876` n `8`; equity avg `0.0527` n `69`; fx avg `0.0018` n `6`; index avg `0.1183` n `23`; metal avg `-0.0259` n `18`; unknown avg `-0.2645` n `421`
- 24h: commodity avg `0.1493` n `12`; crypto_alt avg `-0.3679` n `228`; crypto_major avg `0.5937` n `8`; equity avg `0.8216` n `69`; fx avg `-0.0264` n `6`; index avg `-0.0766` n `23`; metal avg `-0.0981` n `18`; unknown avg `0.356` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1686`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
