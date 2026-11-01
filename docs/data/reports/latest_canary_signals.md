# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-01T00:07:28.002493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0637` n `13`; crypto_alt avg `0.137` n `238`; crypto_major avg `0.0546` n `8`; equity avg `-0.0113` n `156`; fx avg `-0.0021` n `6`; index avg `-0.006` n `27`; metal avg `0.0004` n `20`; unknown avg `0.4372` n `1244`
- 1h: commodity avg `0.0751` n `13`; crypto_alt avg `0.1204` n `238`; crypto_major avg `0.0914` n `8`; equity avg `0.0053` n `156`; fx avg `-0.0017` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0016` n `20`; unknown avg `201.9593` n `1242`
- 4h: commodity avg `0.1235` n `13`; crypto_alt avg `-0.037` n `238`; crypto_major avg `-0.1495` n `8`; equity avg `-0.0263` n `156`; fx avg `0.0016` n `6`; index avg `-0.0037` n `27`; metal avg `0.0129` n `20`; unknown avg `3.7195` n `1098`
- 24h: commodity avg `0.0718` n `13`; crypto_alt avg `-0.7172` n `238`; crypto_major avg `-0.4196` n `8`; equity avg `-0.0525` n `156`; fx avg `0.0014` n `6`; index avg `-0.0649` n `27`; metal avg `0.047` n `20`; unknown avg `1.2215` n `1024`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
