# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T04:52:15.130335+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0566` n `12`; crypto_alt avg `0.0511` n `228`; crypto_major avg `-0.0758` n `8`; equity avg `0.0346` n `69`; fx avg `0.0006` n `6`; index avg `-0.0061` n `23`; metal avg `-0.0237` n `18`; unknown avg `-0.0909` n `421`
- 1h: commodity avg `0.1217` n `12`; crypto_alt avg `0.2122` n `228`; crypto_major avg `0.0529` n `8`; equity avg `0.0255` n `69`; fx avg `0.0027` n `6`; index avg `-0.0183` n `23`; metal avg `-0.0125` n `18`; unknown avg `-0.3554` n `421`
- 4h: commodity avg `0.1103` n `12`; crypto_alt avg `0.6259` n `228`; crypto_major avg `0.6416` n `8`; equity avg `0.1666` n `69`; fx avg `0.0385` n `6`; index avg `-0.0123` n `23`; metal avg `-0.0474` n `18`; unknown avg `-0.1972` n `419`
- 24h: commodity avg `0.0818` n `12`; crypto_alt avg `1.2498` n `228`; crypto_major avg `2.9476` n `8`; equity avg `1.033` n `69`; fx avg `0.0531` n `6`; index avg `0.0504` n `23`; metal avg `-0.0313` n `18`; unknown avg `0.7861` n `399`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
