# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T01:07:26.113887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0044` n `12`; crypto_alt avg `0.0755` n `233`; crypto_major avg `0.0743` n `8`; equity avg `0.0142` n `136`; fx avg `-0.0006` n `6`; index avg `0.0012` n `26`; metal avg `0.0015` n `20`; unknown avg `0.1151` n `836`
- 1h: commodity avg `0.0545` n `12`; crypto_alt avg `0.2233` n `233`; crypto_major avg `0.0168` n `8`; equity avg `0.0015` n `136`; fx avg `0.0018` n `6`; index avg `-0.0048` n `26`; metal avg `0.0001` n `20`; unknown avg `52.4222` n `830`
- 4h: commodity avg `0.0235` n `12`; crypto_alt avg `0.2904` n `233`; crypto_major avg `0.0072` n `8`; equity avg `-0.021` n `136`; fx avg `0.0023` n `6`; index avg `-0.0112` n `26`; metal avg `0.0012` n `20`; unknown avg `13.7444` n `796`
- 24h: commodity avg `-0.0177` n `12`; crypto_alt avg `1.1212` n `233`; crypto_major avg `0.2501` n `8`; equity avg `-0.3766` n `136`; fx avg `-0.0111` n `6`; index avg `-0.039` n `26`; metal avg `0.0043` n `20`; unknown avg `0.8348` n `724`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
