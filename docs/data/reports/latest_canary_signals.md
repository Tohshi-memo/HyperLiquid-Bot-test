# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T19:52:39.241908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0341` n `12`; crypto_alt avg `-0.1081` n `230`; crypto_major avg `-0.0656` n `8`; equity avg `-0.0536` n `120`; fx avg `-0.001` n `6`; index avg `0.0019` n `25`; metal avg `-0.081` n `20`; unknown avg `-0.0055` n `789`
- 1h: commodity avg `0.0157` n `12`; crypto_alt avg `-0.1435` n `230`; crypto_major avg `-0.0168` n `8`; equity avg `-0.0138` n `120`; fx avg `0.0075` n `6`; index avg `0.0151` n `25`; metal avg `-0.0911` n `20`; unknown avg `-0.0592` n `789`
- 4h: commodity avg `0.0283` n `12`; crypto_alt avg `-0.3668` n `230`; crypto_major avg `-0.1393` n `8`; equity avg `-0.4535` n `120`; fx avg `0.0014` n `6`; index avg `-0.0223` n `25`; metal avg `-0.1643` n `20`; unknown avg `0.1482` n `789`
- 24h: commodity avg `0.307` n `12`; crypto_alt avg `-0.5747` n `230`; crypto_major avg `0.3572` n `8`; equity avg `-4.3726` n `120`; fx avg `-0.035` n `6`; index avg `-0.6555` n `25`; metal avg `-0.76` n `20`; unknown avg `-0.2552` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
