# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T17:37:30.646912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.29` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0248` n `12`; crypto_alt avg `-0.005` n `233`; crypto_major avg `-0.0497` n `8`; equity avg `0.048` n `136`; fx avg `0.0009` n `6`; index avg `0.0111` n `26`; metal avg `-0.0044` n `20`; unknown avg `-0.1518` n `774`
- 1h: commodity avg `-0.1216` n `12`; crypto_alt avg `-0.0481` n `233`; crypto_major avg `0.0576` n `8`; equity avg `0.2277` n `136`; fx avg `-0.0036` n `6`; index avg `0.0453` n `26`; metal avg `0.0483` n `20`; unknown avg `0.0521` n `758`
- 4h: commodity avg `0.067` n `12`; crypto_alt avg `1.2034` n `233`; crypto_major avg `1.0748` n `8`; equity avg `0.4638` n `136`; fx avg `0.0547` n `6`; index avg `0.0469` n `26`; metal avg `-0.1934` n `20`; unknown avg `1.0732` n `736`
- 24h: commodity avg `-0.5334` n `12`; crypto_alt avg `0.82` n `233`; crypto_major avg `1.5245` n `8`; equity avg `0.584` n `136`; fx avg `-0.1559` n `6`; index avg `0.3355` n `26`; metal avg `0.1292` n `20`; unknown avg `1.9647` n `666`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0582`, n `668`, weak_sample_signal
