# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T16:37:29.811273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0386` n `13`; crypto_alt avg `0.2497` n `235`; crypto_major avg `0.3046` n `8`; equity avg `0.0805` n `144`; fx avg `-0.0001` n `6`; index avg `0.0191` n `26`; metal avg `-0.003` n `20`; unknown avg `0.1036` n `1079`
- 1h: commodity avg `-0.1574` n `13`; crypto_alt avg `-0.2038` n `235`; crypto_major avg `-0.0838` n `8`; equity avg `0.0126` n `144`; fx avg `-0.0152` n `6`; index avg `0.025` n `26`; metal avg `-0.0982` n `20`; unknown avg `0.9659` n `1071`
- 4h: commodity avg `-0.1079` n `13`; crypto_alt avg `-1.1465` n `235`; crypto_major avg `-0.6509` n `8`; equity avg `0.1565` n `144`; fx avg `-0.0556` n `6`; index avg `0.1169` n `26`; metal avg `-0.2018` n `20`; unknown avg `0.7999` n `989`
- 24h: commodity avg `-0.2233` n `13`; crypto_alt avg `-0.1409` n `235`; crypto_major avg `-0.0326` n `8`; equity avg `0.2279` n `144`; fx avg `-0.0976` n `6`; index avg `0.0937` n `26`; metal avg `0.1128` n `20`; unknown avg `-0.2338` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2017`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
