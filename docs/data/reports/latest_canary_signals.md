# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T03:52:24.495556+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `0.0954` n `230`; crypto_major avg `0.0662` n `8`; equity avg `-0.1039` n `120`; fx avg `-0.0013` n `6`; index avg `-0.0156` n `25`; metal avg `-0.0089` n `20`; unknown avg `-0.0757` n `789`
- 1h: commodity avg `-0.011` n `12`; crypto_alt avg `0.3911` n `230`; crypto_major avg `0.1751` n `8`; equity avg `-0.1362` n `120`; fx avg `-0.007` n `6`; index avg `0.0052` n `25`; metal avg `0.0295` n `20`; unknown avg `-0.3297` n `789`
- 4h: commodity avg `0.0212` n `12`; crypto_alt avg `0.1496` n `230`; crypto_major avg `-0.258` n `8`; equity avg `0.3926` n `120`; fx avg `-0.1647` n `6`; index avg `-0.0416` n `25`; metal avg `0.1382` n `20`; unknown avg `0.2321` n `789`
- 24h: commodity avg `0.2793` n `12`; crypto_alt avg `0.84` n `230`; crypto_major avg `0.354` n `8`; equity avg `-3.1041` n `120`; fx avg `-0.1468` n `6`; index avg `-0.4923` n `25`; metal avg `-0.4942` n `20`; unknown avg `-0.1789` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
