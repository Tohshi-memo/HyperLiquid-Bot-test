# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T11:37:25.312802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `13`; crypto_alt avg `-0.0435` n `235`; crypto_major avg `0.0158` n `8`; equity avg `0.0034` n `150`; fx avg `0.0113` n `6`; index avg `-0.0045` n `26`; metal avg `0.005` n `20`; unknown avg `0.0303` n `1117`
- 1h: commodity avg `-0.0024` n `13`; crypto_alt avg `0.1563` n `235`; crypto_major avg `0.1763` n `8`; equity avg `0.0104` n `150`; fx avg `0.0239` n `6`; index avg `-0.0051` n `26`; metal avg `0.0035` n `20`; unknown avg `0.0097` n `1115`
- 4h: commodity avg `0.0159` n `13`; crypto_alt avg `-0.2566` n `235`; crypto_major avg `0.0796` n `8`; equity avg `0.0381` n `150`; fx avg `0.0285` n `6`; index avg `0.0011` n `26`; metal avg `-0.0051` n `20`; unknown avg `-0.0579` n `1099`
- 24h: commodity avg `0.4266` n `13`; crypto_alt avg `1.0058` n `235`; crypto_major avg `0.0073` n `8`; equity avg `0.0841` n `150`; fx avg `0.0277` n `6`; index avg `-0.0085` n `26`; metal avg `0.0074` n `20`; unknown avg `0.691` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1515`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
