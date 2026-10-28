# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T23:49:32.374627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0017` n `13`; crypto_alt avg `-0.0268` n `238`; crypto_major avg `-0.0787` n `8`; equity avg `-0.0788` n `155`; fx avg `-0.0099` n `6`; index avg `-0.0106` n `27`; metal avg `-0.0112` n `20`; unknown avg `0.8403` n `1228`
- 1h: commodity avg `-0.0538` n `13`; crypto_alt avg `-0.1451` n `238`; crypto_major avg `-0.0747` n `8`; equity avg `-0.1244` n `155`; fx avg `-0.014` n `6`; index avg `-0.0114` n `27`; metal avg `0.0176` n `20`; unknown avg `0.2533` n `1184`
- 4h: commodity avg `-0.2313` n `13`; crypto_alt avg `-0.3957` n `238`; crypto_major avg `-0.2195` n `8`; equity avg `-1.2731` n `155`; fx avg `-0.0311` n `6`; index avg `-0.1996` n `27`; metal avg `-0.0659` n `20`; unknown avg `4.1016` n `1056`
- 24h: commodity avg `0.1069` n `13`; crypto_alt avg `0.3435` n `238`; crypto_major avg `0.4027` n `8`; equity avg `0.3765` n `154`; fx avg `0.2171` n `6`; index avg `0.0805` n `27`; metal avg `-0.1735` n `20`; unknown avg `26.1608` n `1002`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
