# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T01:52:52.807870+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0477` n `12`; crypto_alt avg `-0.0738` n `231`; crypto_major avg `-0.1835` n `8`; equity avg `-0.0786` n `122`; fx avg `-0.0306` n `6`; index avg `-0.0019` n `25`; metal avg `0.0911` n `20`; unknown avg `-0.0989` n `796`
- 1h: commodity avg `0.0048` n `12`; crypto_alt avg `0.2203` n `231`; crypto_major avg `0.2181` n `8`; equity avg `-0.1053` n `122`; fx avg `-0.0347` n `6`; index avg `0.0088` n `25`; metal avg `0.1494` n `20`; unknown avg `0.1012` n `796`
- 4h: commodity avg `-0.0521` n `12`; crypto_alt avg `0.833` n `231`; crypto_major avg `0.4111` n `8`; equity avg `-0.666` n `122`; fx avg `-0.0264` n `6`; index avg `-0.1316` n `25`; metal avg `0.0912` n `20`; unknown avg `0.0266` n `795`
- 24h: commodity avg `-0.8175` n `12`; crypto_alt avg `-2.0828` n `231`; crypto_major avg `-1.8604` n `8`; equity avg `1.1592` n `122`; fx avg `0.0013` n `6`; index avg `0.1214` n `25`; metal avg `-0.0369` n `20`; unknown avg `-0.3435` n `778`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
