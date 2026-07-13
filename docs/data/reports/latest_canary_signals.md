# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T18:07:38.178799+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1283` n `12`; crypto_alt avg `0.0075` n `230`; crypto_major avg `-0.0454` n `8`; equity avg `0.2773` n `92`; fx avg `-0.0045` n `6`; index avg `0.0217` n `25`; metal avg `0.0142` n `20`; unknown avg `0.008` n `766`
- 1h: commodity avg `0.4197` n `12`; crypto_alt avg `-0.5545` n `230`; crypto_major avg `-0.4125` n `8`; equity avg `-0.2098` n `92`; fx avg `-0.0255` n `6`; index avg `-0.0541` n `25`; metal avg `-0.0468` n `20`; unknown avg `-0.1432` n `766`
- 4h: commodity avg `0.983` n `12`; crypto_alt avg `-0.9082` n `230`; crypto_major avg `-0.6686` n `8`; equity avg `-0.3315` n `92`; fx avg `-0.0363` n `6`; index avg `-0.1265` n `25`; metal avg `-0.253` n `20`; unknown avg `-0.1869` n `766`
- 24h: commodity avg `0.6024` n `12`; crypto_alt avg `-2.2802` n `230`; crypto_major avg `-3.1331` n `8`; equity avg `-3.0305` n `92`; fx avg `-0.08` n `6`; index avg `-0.5997` n `25`; metal avg `-0.5879` n `20`; unknown avg `-0.2463` n `749`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1934`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1804`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
