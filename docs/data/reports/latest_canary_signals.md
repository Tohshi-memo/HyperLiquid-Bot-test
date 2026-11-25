# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T12:37:34.994189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0318` n `13`; crypto_alt avg `-0.1705` n `239`; crypto_major avg `0.0837` n `8`; equity avg `0.2019` n `168`; fx avg `-0.0086` n `6`; index avg `0.028` n `27`; metal avg `0.129` n `20`; unknown avg `0.3342` n `1265`
- 1h: commodity avg `0.1381` n `13`; crypto_alt avg `0.0184` n `239`; crypto_major avg `0.3599` n `8`; equity avg `0.1126` n `168`; fx avg `0.0323` n `6`; index avg `0.031` n `27`; metal avg `0.2131` n `20`; unknown avg `0.1547` n `1251`
- 4h: commodity avg `0.4805` n `13`; crypto_alt avg `-1.2098` n `239`; crypto_major avg `-0.7019` n `8`; equity avg `-1.4865` n `168`; fx avg `0.0104` n `6`; index avg `-0.2326` n `27`; metal avg `-0.0811` n `20`; unknown avg `84.3594` n `1185`
- 24h: commodity avg `0.4625` n `13`; crypto_alt avg `-2.1278` n `239`; crypto_major avg `-3.0344` n `8`; equity avg `-4.834` n `168`; fx avg `-0.0004` n `6`; index avg `-0.4147` n `27`; metal avg `-0.9971` n `20`; unknown avg `468.8171` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
