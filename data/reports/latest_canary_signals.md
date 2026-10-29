# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T11:07:30.436345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.2335` n `238`; crypto_major avg `-0.1427` n `8`; equity avg `-0.1097` n `155`; fx avg `-0.0076` n `6`; index avg `-0.0158` n `27`; metal avg `-0.0047` n `20`; unknown avg `0.1818` n `1233`
- 1h: commodity avg `-0.0432` n `13`; crypto_alt avg `0.6212` n `238`; crypto_major avg `1.1491` n `8`; equity avg `0.0496` n `155`; fx avg `0.028` n `6`; index avg `-0.0192` n `27`; metal avg `0.0551` n `20`; unknown avg `2.5814` n `1160`
- 4h: commodity avg `-0.1161` n `13`; crypto_alt avg `1.0416` n `238`; crypto_major avg `1.2393` n `8`; equity avg `0.2307` n `155`; fx avg `0.0627` n `6`; index avg `0.029` n `27`; metal avg `-0.1218` n `20`; unknown avg `2.3275` n `1120`
- 24h: commodity avg `-0.3374` n `13`; crypto_alt avg `-1.8932` n `238`; crypto_major avg `-0.8472` n `8`; equity avg `-1.4426` n `155`; fx avg `0.0788` n `6`; index avg `-0.0016` n `27`; metal avg `-0.3402` n `20`; unknown avg `5.8501` n `982`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
