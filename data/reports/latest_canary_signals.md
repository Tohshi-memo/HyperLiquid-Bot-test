# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T00:22:28.162823+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `13`; crypto_alt avg `-0.0588` n `235`; crypto_major avg `-0.0352` n `8`; equity avg `-0.0065` n `150`; fx avg `-0.0007` n `6`; index avg `0.0025` n `26`; metal avg `0.0022` n `20`; unknown avg `0.03` n `1117`
- 1h: commodity avg `0.0649` n `13`; crypto_alt avg `0.0445` n `235`; crypto_major avg `-0.0161` n `8`; equity avg `-0.0236` n `150`; fx avg `0.0073` n `6`; index avg `0.0032` n `26`; metal avg `0.0017` n `20`; unknown avg `0.2058` n `1109`
- 4h: commodity avg `0.2228` n `13`; crypto_alt avg `-0.0524` n `235`; crypto_major avg `-0.0636` n `8`; equity avg `0.0028` n `150`; fx avg `0.0029` n `6`; index avg `0.0051` n `26`; metal avg `0.0157` n `20`; unknown avg `0.164` n `1079`
- 24h: commodity avg `0.0687` n `13`; crypto_alt avg `1.3589` n `235`; crypto_major avg `0.5024` n `8`; equity avg `0.1205` n `150`; fx avg `-0.006` n `6`; index avg `0.0079` n `26`; metal avg `-0.0079` n `20`; unknown avg `0.3191` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.113`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
