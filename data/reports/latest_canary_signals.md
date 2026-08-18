# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T18:16:06.288442+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0031` n `12`; crypto_alt avg `-0.0255` n `230`; crypto_major avg `0.0544` n `8`; equity avg `0.1031` n `120`; fx avg `-0.0015` n `6`; index avg `0.0111` n `25`; metal avg `0.0176` n `20`; unknown avg `-0.0369` n `789`
- 1h: commodity avg `0.0149` n `12`; crypto_alt avg `-0.1497` n `230`; crypto_major avg `0.0263` n `8`; equity avg `-0.2905` n `120`; fx avg `0.013` n `6`; index avg `-0.0392` n `25`; metal avg `-0.0725` n `20`; unknown avg `-0.0226` n `789`
- 4h: commodity avg `0.1595` n `12`; crypto_alt avg `0.018` n `230`; crypto_major avg `0.1397` n `8`; equity avg `-1.0414` n `120`; fx avg `0.0012` n `6`; index avg `-0.1578` n `25`; metal avg `-0.2955` n `20`; unknown avg `2.031` n `789`
- 24h: commodity avg `0.2577` n `12`; crypto_alt avg `-0.5646` n `230`; crypto_major avg `0.1116` n `8`; equity avg `-4.5329` n `120`; fx avg `-0.0441` n `6`; index avg `-0.7126` n `25`; metal avg `-0.6814` n `20`; unknown avg `-0.279` n `754`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
