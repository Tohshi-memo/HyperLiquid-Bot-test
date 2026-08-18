# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T21:34:55.205409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.0056` n `230`; crypto_major avg `-0.0227` n `8`; equity avg `0.0065` n `120`; fx avg `-0.0008` n `6`; index avg `0.0039` n `25`; metal avg `0.0125` n `20`; unknown avg `-0.0414` n `789`
- 1h: commodity avg `-0.0187` n `12`; crypto_alt avg `-0.1429` n `230`; crypto_major avg `-0.1376` n `8`; equity avg `-0.1345` n `120`; fx avg `0.0027` n `6`; index avg `-0.01` n `25`; metal avg `0.0077` n `20`; unknown avg `0.3031` n `789`
- 4h: commodity avg `0.075` n `12`; crypto_alt avg `-0.4574` n `230`; crypto_major avg `-0.0167` n `8`; equity avg `-0.352` n `120`; fx avg `0.0144` n `6`; index avg `-0.0461` n `25`; metal avg `-0.1351` n `20`; unknown avg `0.0061` n `789`
- 24h: commodity avg `0.2885` n `12`; crypto_alt avg `-0.895` n `230`; crypto_major avg `0.1046` n `8`; equity avg `-4.4541` n `120`; fx avg `-0.0307` n `6`; index avg `-0.6915` n `25`; metal avg `-0.752` n `20`; unknown avg `-0.2605` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
