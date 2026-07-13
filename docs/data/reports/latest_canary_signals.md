# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T13:52:29.219465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0024` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `-0.2386` n `230`; crypto_major avg `-0.3891` n `8`; equity avg `-0.5075` n `92`; fx avg `0.0151` n `6`; index avg `-0.0545` n `25`; metal avg `-0.0297` n `20`; unknown avg `0.021` n `766`
- 1h: commodity avg `-0.1116` n `12`; crypto_alt avg `-0.2676` n `230`; crypto_major avg `-0.4772` n `8`; equity avg `-0.6341` n `92`; fx avg `-0.0029` n `6`; index avg `-0.0486` n `25`; metal avg `-0.0544` n `20`; unknown avg `-0.0537` n `766`
- 4h: commodity avg `0.136` n `12`; crypto_alt avg `-0.4943` n `230`; crypto_major avg `-1.0773` n `8`; equity avg `-0.8165` n `92`; fx avg `-0.0005` n `6`; index avg `-0.0749` n `25`; metal avg `-0.0742` n `20`; unknown avg `0.163` n `766`
- 24h: commodity avg `-0.1817` n `12`; crypto_alt avg `-1.6215` n `230`; crypto_major avg `-2.4791` n `8`; equity avg `-2.7869` n `92`; fx avg `-0.0598` n `6`; index avg `-0.5138` n `25`; metal avg `-0.2466` n `20`; unknown avg `-0.2508` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1894`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
