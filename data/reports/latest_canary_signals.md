# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T10:37:30.261426+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.0041` n `228`; crypto_major avg `-0.0927` n `8`; equity avg `-0.0112` n `86`; fx avg `-0.006` n `6`; index avg `0.0` n `23`; metal avg `0.1012` n `20`; unknown avg `-0.0156` n `765`
- 1h: commodity avg `0.0155` n `12`; crypto_alt avg `-0.6338` n `228`; crypto_major avg `-0.7461` n `8`; equity avg `-0.1265` n `86`; fx avg `0.0015` n `6`; index avg `-0.0116` n `23`; metal avg `-0.0024` n `20`; unknown avg `-0.0591` n `765`
- 4h: commodity avg `-0.2882` n `12`; crypto_alt avg `-0.1183` n `228`; crypto_major avg `-0.6019` n `8`; equity avg `-0.2702` n `86`; fx avg `0.0539` n `6`; index avg `-0.0591` n `23`; metal avg `0.4554` n `20`; unknown avg `-0.0411` n `757`
- 24h: commodity avg `0.0069` n `12`; crypto_alt avg `-1.8369` n `228`; crypto_major avg `-2.1543` n `8`; equity avg `-4.336` n `86`; fx avg `0.0521` n `6`; index avg `-0.6331` n `23`; metal avg `0.6316` n `20`; unknown avg `0.7029` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2747`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1724`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
