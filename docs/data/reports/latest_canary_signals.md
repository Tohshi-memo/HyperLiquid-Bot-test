# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T14:37:36.453012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0633` n `12`; crypto_alt avg `0.1802` n `230`; crypto_major avg `0.1522` n `8`; equity avg `0.5456` n `92`; fx avg `0.0019` n `6`; index avg `0.0859` n `25`; metal avg `-0.0388` n `20`; unknown avg `0.0223` n `766`
- 1h: commodity avg `0.1639` n `12`; crypto_alt avg `0.1977` n `230`; crypto_major avg `0.0878` n `8`; equity avg `0.1706` n `92`; fx avg `0.0058` n `6`; index avg `0.0513` n `25`; metal avg `-0.2481` n `20`; unknown avg `0.1473` n `766`
- 4h: commodity avg `0.1127` n `12`; crypto_alt avg `-0.1397` n `230`; crypto_major avg `-0.3971` n `8`; equity avg `-0.0011` n `92`; fx avg `0.0006` n `6`; index avg `0.0839` n `25`; metal avg `-0.1877` n `20`; unknown avg `0.0795` n `766`
- 24h: commodity avg `0.0112` n `12`; crypto_alt avg `-1.1446` n `230`; crypto_major avg `-2.0544` n `8`; equity avg `-2.136` n `92`; fx avg `-0.0741` n `6`; index avg `-0.4034` n `25`; metal avg `-0.4495` n `20`; unknown avg `-0.1072` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1897`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
