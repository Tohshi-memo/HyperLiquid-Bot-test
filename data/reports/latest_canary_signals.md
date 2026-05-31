# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T12:37:23.394205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0527` n `12`; crypto_alt avg `0.0706` n `228`; crypto_major avg `0.0863` n `8`; equity avg `0.0247` n `69`; fx avg `0.0` n `6`; index avg `0.0023` n `23`; metal avg `0.0009` n `18`; unknown avg `-0.2397` n `421`
- 1h: commodity avg `0.0008` n `12`; crypto_alt avg `0.1472` n `228`; crypto_major avg `0.1811` n `8`; equity avg `0.0316` n `69`; fx avg `0.01` n `6`; index avg `-0.0023` n `23`; metal avg `0.0243` n `18`; unknown avg `-0.0437` n `421`
- 4h: commodity avg `0.1276` n `12`; crypto_alt avg `0.2012` n `228`; crypto_major avg `-0.0687` n `8`; equity avg `0.0023` n `69`; fx avg `-0.0203` n `6`; index avg `-0.0893` n `23`; metal avg `0.0004` n `18`; unknown avg `-0.3374` n `421`
- 24h: commodity avg `0.1643` n `12`; crypto_alt avg `0.3662` n `228`; crypto_major avg `1.2439` n `8`; equity avg `0.9312` n `69`; fx avg `-0.0079` n `6`; index avg `-0.1499` n `23`; metal avg `-0.0668` n `18`; unknown avg `0.3612` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
