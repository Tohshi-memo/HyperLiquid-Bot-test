# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T19:37:29.057513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2817` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `0.3922` n `228`; crypto_major avg `0.3816` n `8`; equity avg `0.4189` n `86`; fx avg `0.0038` n `6`; index avg `0.0846` n `23`; metal avg `0.0492` n `20`; unknown avg `0.0701` n `764`
- 1h: commodity avg `-0.0235` n `12`; crypto_alt avg `-0.0082` n `228`; crypto_major avg `-0.0019` n `8`; equity avg `-0.2014` n `86`; fx avg `-0.0037` n `6`; index avg `-0.0093` n `23`; metal avg `-0.0671` n `20`; unknown avg `-0.1073` n `764`
- 4h: commodity avg `-0.0551` n `12`; crypto_alt avg `-1.9713` n `228`; crypto_major avg `-1.4708` n `8`; equity avg `-1.328` n `86`; fx avg `0.0268` n `6`; index avg `-0.1891` n `23`; metal avg `-0.6252` n `20`; unknown avg `-1.0039` n `764`
- 24h: commodity avg `-0.5637` n `12`; crypto_alt avg `-3.8272` n `228`; crypto_major avg `-3.5417` n `8`; equity avg `1.9653` n `86`; fx avg `0.0752` n `6`; index avg `0.0384` n `23`; metal avg `-2.0308` n `20`; unknown avg `-0.7651` n `724`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
