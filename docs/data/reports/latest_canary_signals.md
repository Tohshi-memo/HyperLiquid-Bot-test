# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T12:07:25.371217+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0482` n `12`; crypto_alt avg `-0.2072` n `231`; crypto_major avg `-0.2` n `8`; equity avg `-0.034` n `122`; fx avg `-0.0048` n `6`; index avg `-0.0056` n `25`; metal avg `0.0419` n `20`; unknown avg `0.002` n `797`
- 1h: commodity avg `0.0406` n `12`; crypto_alt avg `-0.5024` n `231`; crypto_major avg `-0.8421` n `8`; equity avg `-0.2336` n `122`; fx avg `0.0075` n `6`; index avg `-0.0287` n `25`; metal avg `0.0078` n `20`; unknown avg `-0.0585` n `797`
- 4h: commodity avg `0.1045` n `12`; crypto_alt avg `-0.2961` n `231`; crypto_major avg `-0.3913` n `8`; equity avg `-0.0628` n `122`; fx avg `-0.0079` n `6`; index avg `-0.0023` n `25`; metal avg `-0.0226` n `20`; unknown avg `-0.0424` n `797`
- 24h: commodity avg `-0.0719` n `12`; crypto_alt avg `-1.0605` n `231`; crypto_major avg `-0.9182` n `8`; equity avg `0.1625` n `122`; fx avg `-0.0026` n `6`; index avg `-0.0515` n `25`; metal avg `0.1656` n `20`; unknown avg `0.6712` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1029`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
