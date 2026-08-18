# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T23:52:27.449286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0051` n `12`; crypto_alt avg `0.0035` n `230`; crypto_major avg `-0.0192` n `8`; equity avg `-0.0101` n `120`; fx avg `0.0158` n `6`; index avg `-0.0041` n `25`; metal avg `0.035` n `20`; unknown avg `-0.0088` n `789`
- 1h: commodity avg `0.0133` n `12`; crypto_alt avg `0.2164` n `230`; crypto_major avg `0.2195` n `8`; equity avg `-0.1823` n `120`; fx avg `0.0125` n `6`; index avg `0.0091` n `25`; metal avg `-0.0298` n `20`; unknown avg `-0.2448` n `789`
- 4h: commodity avg `0.0885` n `12`; crypto_alt avg `-0.0091` n `230`; crypto_major avg `0.0115` n `8`; equity avg `-0.5123` n `120`; fx avg `0.0086` n `6`; index avg `-0.0572` n `25`; metal avg `-0.0904` n `20`; unknown avg `-0.2788` n `789`
- 24h: commodity avg `0.3255` n `12`; crypto_alt avg `-0.498` n `230`; crypto_major avg `-0.0119` n `8`; equity avg `-4.822` n `120`; fx avg `-0.0246` n `6`; index avg `-0.7074` n `25`; metal avg `-0.8807` n `20`; unknown avg `-0.237` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
