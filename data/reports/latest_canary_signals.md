# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T07:52:25.091772+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `-0.0109` n `235`; crypto_major avg `-0.0168` n `8`; equity avg `-0.0011` n `150`; fx avg `0.0006` n `6`; index avg `0.0048` n `26`; metal avg `0.0022` n `20`; unknown avg `4.5154` n `1117`
- 1h: commodity avg `-0.0052` n `13`; crypto_alt avg `-0.2087` n `235`; crypto_major avg `-0.2458` n `8`; equity avg `-0.0108` n `150`; fx avg `-0.0045` n `6`; index avg `0.0056` n `26`; metal avg `0.0032` n `20`; unknown avg `4.1611` n `1115`
- 4h: commodity avg `0.0141` n `13`; crypto_alt avg `0.9711` n `235`; crypto_major avg `0.117` n `8`; equity avg `0.0374` n `150`; fx avg `0.0023` n `6`; index avg `0.0124` n `26`; metal avg `0.0143` n `20`; unknown avg `1.7223` n `1093`
- 24h: commodity avg `0.1553` n `13`; crypto_alt avg `1.2519` n `235`; crypto_major avg `-0.1811` n `8`; equity avg `0.0699` n `150`; fx avg `-0.0113` n `6`; index avg `0.0045` n `26`; metal avg `0.0115` n `20`; unknown avg `0.6578` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
