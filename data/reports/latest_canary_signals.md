# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T16:22:30.563580+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1463` n `13`; crypto_alt avg `-0.2725` n `234`; crypto_major avg `-0.1294` n `8`; equity avg `-0.0586` n `142`; fx avg `0.001` n `6`; index avg `0.0037` n `26`; metal avg `-0.0354` n `20`; unknown avg `0.2097` n `975`
- 1h: commodity avg `-0.3478` n `13`; crypto_alt avg `-0.1658` n `234`; crypto_major avg `-0.3675` n `8`; equity avg `0.0893` n `142`; fx avg `-0.0189` n `6`; index avg `0.0176` n `26`; metal avg `0.0017` n `20`; unknown avg `0.5368` n `967`
- 4h: commodity avg `-0.0566` n `13`; crypto_alt avg `-0.702` n `234`; crypto_major avg `-0.7392` n `8`; equity avg `-0.4434` n `142`; fx avg `-0.1484` n `6`; index avg `-0.1902` n `26`; metal avg `-0.2461` n `20`; unknown avg `1.4055` n `909`
- 24h: commodity avg `-0.4081` n `13`; crypto_alt avg `-1.9697` n `234`; crypto_major avg `-0.929` n `8`; equity avg `-0.1267` n `142`; fx avg `-0.0824` n `6`; index avg `-0.1171` n `26`; metal avg `-0.1192` n `20`; unknown avg `2.6999` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1741`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1559`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.078`, n `668`, weak_sample_signal
