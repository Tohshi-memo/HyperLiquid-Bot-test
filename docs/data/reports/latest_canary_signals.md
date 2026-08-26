# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T01:37:24.040842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `0.097` n `231`; crypto_major avg `0.1707` n `8`; equity avg `-0.0803` n `122`; fx avg `-0.0113` n `6`; index avg `-0.0027` n `25`; metal avg `-0.0218` n `20`; unknown avg `0.1101` n `796`
- 1h: commodity avg `-0.0927` n `12`; crypto_alt avg `0.7579` n `231`; crypto_major avg `0.7878` n `8`; equity avg `-0.1242` n `122`; fx avg `-0.0149` n `6`; index avg `-0.0103` n `25`; metal avg `0.0501` n `20`; unknown avg `0.2947` n `796`
- 4h: commodity avg `-0.0949` n `12`; crypto_alt avg `0.8225` n `231`; crypto_major avg `0.582` n `8`; equity avg `-0.519` n `122`; fx avg `0.0076` n `6`; index avg `-0.1249` n `25`; metal avg `0.0167` n `20`; unknown avg `0.1415` n `795`
- 24h: commodity avg `-0.8292` n `12`; crypto_alt avg `-2.1974` n `231`; crypto_major avg `-2.0006` n `8`; equity avg `1.294` n `122`; fx avg `0.0319` n `6`; index avg `0.1414` n `25`; metal avg `-0.1821` n `20`; unknown avg `-0.3812` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
