# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T14:37:37.679984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0157` n `12`; crypto_alt avg `-0.1071` n `230`; crypto_major avg `-0.2616` n `8`; equity avg `-0.131` n `113`; fx avg `-0.0171` n `6`; index avg `0.0103` n `25`; metal avg `0.0579` n `20`; unknown avg `-0.0322` n `785`
- 1h: commodity avg `0.0353` n `12`; crypto_alt avg `-0.1201` n `230`; crypto_major avg `-0.2437` n `8`; equity avg `0.2282` n `113`; fx avg `-0.0129` n `6`; index avg `0.0229` n `25`; metal avg `-0.0196` n `20`; unknown avg `-0.0636` n `785`
- 4h: commodity avg `-0.2128` n `12`; crypto_alt avg `-0.2758` n `230`; crypto_major avg `-0.2453` n `8`; equity avg `0.5919` n `113`; fx avg `-0.0279` n `6`; index avg `0.0502` n `25`; metal avg `-0.1086` n `20`; unknown avg `-0.0926` n `785`
- 24h: commodity avg `0.2362` n `12`; crypto_alt avg `-1.4487` n `230`; crypto_major avg `-0.6106` n `8`; equity avg `-0.1449` n `113`; fx avg `-0.0755` n `6`; index avg `0.0916` n `25`; metal avg `0.2074` n `20`; unknown avg `-0.1699` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1991`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1776`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
