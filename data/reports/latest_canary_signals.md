# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T22:44:49.858617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `0.0342` n `230`; crypto_major avg `0.0027` n `8`; equity avg `-0.0222` n `114`; fx avg `-0.0047` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0046` n `20`; unknown avg `1.9663` n `791`
- 1h: commodity avg `0.0412` n `12`; crypto_alt avg `0.1051` n `230`; crypto_major avg `0.0295` n `8`; equity avg `0.0309` n `114`; fx avg `0.0041` n `6`; index avg `-0.0057` n `25`; metal avg `0.0045` n `20`; unknown avg `2.8331` n `791`
- 4h: commodity avg `-0.043` n `12`; crypto_alt avg `0.0848` n `230`; crypto_major avg `0.0292` n `8`; equity avg `0.2772` n `114`; fx avg `0.009` n `6`; index avg `0.0384` n `25`; metal avg `0.0246` n `20`; unknown avg `8.754` n `791`
- 24h: commodity avg `0.2395` n `12`; crypto_alt avg `0.1677` n `230`; crypto_major avg `-1.1193` n `8`; equity avg `-0.5483` n `114`; fx avg `0.0782` n `6`; index avg `-0.094` n `25`; metal avg `0.216` n `20`; unknown avg `-0.0909` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2165`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1841`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1509`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
