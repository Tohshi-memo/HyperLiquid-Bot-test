# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T00:37:28.377686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `12`; crypto_alt avg `0.1114` n `231`; crypto_major avg `0.1284` n `8`; equity avg `0.2303` n `122`; fx avg `0.0179` n `6`; index avg `0.0474` n `25`; metal avg `0.0943` n `20`; unknown avg `0.0501` n `794`
- 1h: commodity avg `-0.0124` n `12`; crypto_alt avg `0.2575` n `231`; crypto_major avg `0.4709` n `8`; equity avg `-0.0307` n `122`; fx avg `0.013` n `6`; index avg `-0.0442` n `25`; metal avg `0.0554` n `20`; unknown avg `-0.0978` n `794`
- 4h: commodity avg `0.0457` n `12`; crypto_alt avg `0.2184` n `231`; crypto_major avg `0.917` n `8`; equity avg `-0.0873` n `122`; fx avg `0.0093` n `6`; index avg `-0.0512` n `25`; metal avg `0.2353` n `20`; unknown avg `-0.1922` n `794`
- 24h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.4668` n `231`; crypto_major avg `0.4602` n `8`; equity avg `-2.4293` n `122`; fx avg `-0.0089` n `6`; index avg `-0.339` n `25`; metal avg `0.4163` n `20`; unknown avg `0.8824` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0465`, n `668`, weak_sample_signal
