# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-03T12:52:23.986125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `0.0087` n `235`; crypto_major avg `0.0553` n `8`; equity avg `-0.0078` n `143`; fx avg `0.0` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0025` n `20`; unknown avg `0.8136` n `984`
- 1h: commodity avg `-0.0338` n `13`; crypto_alt avg `-0.3691` n `235`; crypto_major avg `0.0521` n `8`; equity avg `-0.0` n `143`; fx avg `-0.0029` n `6`; index avg `0.001` n `26`; metal avg `-0.0132` n `20`; unknown avg `0.4876` n `974`
- 4h: commodity avg `-0.0336` n `13`; crypto_alt avg `0.4201` n `235`; crypto_major avg `0.235` n `8`; equity avg `0.0122` n `143`; fx avg `-0.0222` n `6`; index avg `-0.0127` n `26`; metal avg `-0.0126` n `20`; unknown avg `0.3974` n `972`
- 24h: commodity avg `0.5201` n `13`; crypto_alt avg `-2.6566` n `235`; crypto_major avg `-2.4797` n `8`; equity avg `-0.2658` n `143`; fx avg `0.042` n `6`; index avg `-0.0312` n `26`; metal avg `-0.42` n `20`; unknown avg `0.0485` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1982`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.188`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1566`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
