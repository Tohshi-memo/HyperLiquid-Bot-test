# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T06:52:26.867266+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `0.1803` n `235`; crypto_major avg `0.1565` n `8`; equity avg `-0.0528` n `144`; fx avg `0.032` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0223` n `20`; unknown avg `0.1319` n `1079`
- 1h: commodity avg `0.0678` n `13`; crypto_alt avg `0.3761` n `235`; crypto_major avg `0.4689` n `8`; equity avg `0.0103` n `144`; fx avg `-0.026` n `6`; index avg `-0.0013` n `26`; metal avg `0.089` n `20`; unknown avg `2.5818` n `1061`
- 4h: commodity avg `0.0242` n `13`; crypto_alt avg `-0.3752` n `235`; crypto_major avg `-0.2514` n `8`; equity avg `-0.2235` n `144`; fx avg `-0.0361` n `6`; index avg `-0.0623` n `26`; metal avg `0.0457` n `20`; unknown avg `1.1587` n `970`
- 24h: commodity avg `-0.2836` n `13`; crypto_alt avg `0.6157` n `235`; crypto_major avg `1.1429` n `8`; equity avg `0.2367` n `144`; fx avg `-0.0759` n `6`; index avg `-0.0547` n `26`; metal avg `0.1489` n `20`; unknown avg `0.0898` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1836`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
