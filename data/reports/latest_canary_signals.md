# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T21:40:20.155956+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0355` n `12`; crypto_alt avg `-0.5718` n `230`; crypto_major avg `-0.4142` n `8`; equity avg `0.0044` n `92`; fx avg `0.0065` n `6`; index avg `0.0033` n `25`; metal avg `0.0019` n `20`; unknown avg `-0.0414` n `766`
- 1h: commodity avg `-0.0483` n `12`; crypto_alt avg `-0.7773` n `230`; crypto_major avg `-0.6353` n `8`; equity avg `-0.0132` n `92`; fx avg `0.0243` n `6`; index avg `0.0084` n `25`; metal avg `0.0212` n `20`; unknown avg `-0.1173` n `766`
- 4h: commodity avg `0.2411` n `12`; crypto_alt avg `-0.9276` n `230`; crypto_major avg `-0.5596` n `8`; equity avg `-0.1099` n `92`; fx avg `0.0037` n `6`; index avg `-0.0958` n `25`; metal avg `0.0237` n `20`; unknown avg `-0.3977` n `766`
- 24h: commodity avg `0.6055` n `12`; crypto_alt avg `-2.936` n `230`; crypto_major avg `-3.3683` n `8`; equity avg `-3.3255` n `92`; fx avg `-0.0363` n `6`; index avg `-0.667` n `25`; metal avg `-0.5315` n `20`; unknown avg `-0.4418` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
