# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T18:37:36.701888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0727` n `13`; crypto_alt avg `0.0412` n `235`; crypto_major avg `-0.0248` n `8`; equity avg `-0.0697` n `144`; fx avg `0.0076` n `6`; index avg `0.0045` n `26`; metal avg `0.018` n `20`; unknown avg `3.2295` n `1079`
- 1h: commodity avg `-0.05` n `13`; crypto_alt avg `0.4169` n `235`; crypto_major avg `0.1701` n `8`; equity avg `0.0057` n `144`; fx avg `0.0054` n `6`; index avg `0.0209` n `26`; metal avg `0.0992` n `20`; unknown avg `3.052` n `1077`
- 4h: commodity avg `-0.1604` n `13`; crypto_alt avg `0.2561` n `235`; crypto_major avg `-0.0063` n `8`; equity avg `0.2917` n `144`; fx avg `0.0438` n `6`; index avg `0.0824` n `26`; metal avg `0.0628` n `20`; unknown avg `3.3643` n `1039`
- 24h: commodity avg `-0.4207` n `13`; crypto_alt avg `0.1068` n `235`; crypto_major avg `0.173` n `8`; equity avg `0.3021` n `144`; fx avg `-0.0796` n `6`; index avg `0.1322` n `26`; metal avg `0.1835` n `20`; unknown avg `2.8529` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.2009`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
