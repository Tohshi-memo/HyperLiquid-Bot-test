# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T01:37:46.867928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0307` n `13`; crypto_alt avg `-0.0012` n `239`; crypto_major avg `-0.0396` n `8`; equity avg `0.0949` n `168`; fx avg `0.0174` n `6`; index avg `0.0063` n `27`; metal avg `0.2219` n `20`; unknown avg `23.9144` n `1265`
- 1h: commodity avg `-0.0509` n `13`; crypto_alt avg `-0.0788` n `239`; crypto_major avg `-0.3166` n `8`; equity avg `0.3942` n `168`; fx avg `-0.0404` n `6`; index avg `0.0377` n `27`; metal avg `0.1063` n `20`; unknown avg `181.5768` n `1257`
- 4h: commodity avg `-0.0087` n `13`; crypto_alt avg `-0.2152` n `239`; crypto_major avg `-0.6158` n `8`; equity avg `-0.3111` n `168`; fx avg `0.02` n `6`; index avg `-0.0485` n `27`; metal avg `0.0301` n `20`; unknown avg `30.462` n `1167`
- 24h: commodity avg `0.6423` n `13`; crypto_alt avg `-3.7528` n `239`; crypto_major avg `-3.6534` n `8`; equity avg `-4.8974` n `167`; fx avg `0.1596` n `6`; index avg `-0.4728` n `27`; metal avg `-1.308` n `20`; unknown avg `480.9228` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0982`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
