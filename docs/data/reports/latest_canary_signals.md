# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T13:07:30.714338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0134` n `13`; crypto_alt avg `0.2425` n `235`; crypto_major avg `0.0846` n `8`; equity avg `0.0025` n `143`; fx avg `-0.0002` n `6`; index avg `0.0033` n `26`; metal avg `0.0064` n `20`; unknown avg `0.2057` n `982`
- 1h: commodity avg `-0.0052` n `13`; crypto_alt avg `-0.0872` n `235`; crypto_major avg `0.0751` n `8`; equity avg `-0.0009` n `143`; fx avg `-0.0027` n `6`; index avg `0.0025` n `26`; metal avg `0.0042` n `20`; unknown avg `0.2906` n `982`
- 4h: commodity avg `-0.0203` n `13`; crypto_alt avg `0.6642` n `235`; crypto_major avg `0.32` n `8`; equity avg `0.0147` n `143`; fx avg `-0.0225` n `6`; index avg `-0.0093` n `26`; metal avg `-0.0062` n `20`; unknown avg `-0.033` n `972`
- 24h: commodity avg `0.628` n `13`; crypto_alt avg `-2.5252` n `235`; crypto_major avg `-2.4657` n `8`; equity avg `-0.3963` n `143`; fx avg `0.0654` n `6`; index avg `-0.0645` n `26`; metal avg `-0.4417` n `20`; unknown avg `-0.1001` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1981`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1879`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
