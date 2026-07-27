# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T20:37:33.865115+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `12`; crypto_alt avg `0.1209` n `230`; crypto_major avg `0.1398` n `8`; equity avg `0.1239` n `102`; fx avg `-0.0044` n `6`; index avg `0.0265` n `25`; metal avg `-0.0043` n `20`; unknown avg `0.0228` n `774`
- 1h: commodity avg `-0.0711` n `12`; crypto_alt avg `0.1657` n `230`; crypto_major avg `-0.0097` n `8`; equity avg `0.1556` n `102`; fx avg `-0.011` n `6`; index avg `0.0138` n `25`; metal avg `-0.054` n `20`; unknown avg `-0.1547` n `774`
- 4h: commodity avg `-0.1536` n `12`; crypto_alt avg `0.1185` n `230`; crypto_major avg `-0.0345` n `8`; equity avg `0.4471` n `102`; fx avg `-0.0271` n `6`; index avg `0.088` n `25`; metal avg `-0.1429` n `20`; unknown avg `95.4604` n `774`
- 24h: commodity avg `-1.0544` n `12`; crypto_alt avg `-0.7593` n `230`; crypto_major avg `-0.1036` n `8`; equity avg `-0.9025` n `102`; fx avg `-0.0384` n `6`; index avg `-0.3048` n `25`; metal avg `0.2122` n `20`; unknown avg `97.711` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1921`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
