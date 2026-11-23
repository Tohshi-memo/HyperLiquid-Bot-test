# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T04:07:39.180449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0547` n `13`; crypto_alt avg `0.0531` n `239`; crypto_major avg `0.0339` n `8`; equity avg `0.1672` n `166`; fx avg `-0.0068` n `6`; index avg `-0.0332` n `27`; metal avg `-0.0161` n `20`; unknown avg `10.4115` n `1250`
- 1h: commodity avg `0.1004` n `13`; crypto_alt avg `0.7706` n `239`; crypto_major avg `0.733` n `8`; equity avg `0.7925` n `166`; fx avg `0.0341` n `6`; index avg `0.0471` n `27`; metal avg `0.101` n `20`; unknown avg `166.105` n `1246`
- 4h: commodity avg `0.0937` n `13`; crypto_alt avg `0.1748` n `239`; crypto_major avg `0.2075` n `8`; equity avg `0.1953` n `166`; fx avg `0.1476` n `6`; index avg `-0.1184` n `27`; metal avg `-0.0495` n `20`; unknown avg `2.437` n `1239`
- 24h: commodity avg `-0.2985` n `13`; crypto_alt avg `1.7586` n `239`; crypto_major avg `2.3889` n `8`; equity avg `2.0477` n `166`; fx avg `0.2201` n `6`; index avg `0.1408` n `27`; metal avg `0.3571` n `20`; unknown avg `246.2363` n `1019`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
