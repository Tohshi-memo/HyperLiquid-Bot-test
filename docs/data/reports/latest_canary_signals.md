# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T13:52:28.504433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `0.34` n `232`; crypto_major avg `0.3755` n `8`; equity avg `-0.2049` n `131`; fx avg `-0.0015` n `6`; index avg `0.0005` n `26`; metal avg `0.0174` n `20`; unknown avg `0.5486` n `792`
- 1h: commodity avg `0.025` n `12`; crypto_alt avg `0.3247` n `232`; crypto_major avg `0.0267` n `8`; equity avg `-0.4451` n `131`; fx avg `-0.0064` n `6`; index avg `0.0023` n `26`; metal avg `-0.0671` n `20`; unknown avg `0.5421` n `790`
- 4h: commodity avg `-0.0829` n `12`; crypto_alt avg `0.5385` n `232`; crypto_major avg `0.1656` n `8`; equity avg `-0.9495` n `130`; fx avg `-0.0168` n `6`; index avg `-0.0488` n `26`; metal avg `0.0119` n `20`; unknown avg `-0.1878` n `790`
- 24h: commodity avg `0.224` n `12`; crypto_alt avg `1.6476` n `232`; crypto_major avg `0.7274` n `8`; equity avg `-1.4474` n `130`; fx avg `0.0546` n `6`; index avg `-0.2513` n `26`; metal avg `-0.542` n `20`; unknown avg `0.1844` n `750`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0501`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0392`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0313`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0312`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.03`, n `668`, weak_sample_signal
