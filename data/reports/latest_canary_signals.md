# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T00:08:01.538984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0442` n `12`; crypto_alt avg `0.3275` n `233`; crypto_major avg `0.264` n `8`; equity avg `0.3068` n `134`; fx avg `-0.0413` n `6`; index avg `0.0891` n `26`; metal avg `0.0122` n `20`; unknown avg `0.4389` n `795`
- 1h: commodity avg `0.0151` n `12`; crypto_alt avg `0.3509` n `233`; crypto_major avg `0.2605` n `8`; equity avg `0.0947` n `134`; fx avg `-0.0551` n `6`; index avg `0.0412` n `26`; metal avg `0.011` n `20`; unknown avg `1.3973` n `795`
- 4h: commodity avg `0.0531` n `12`; crypto_alt avg `0.2756` n `233`; crypto_major avg `0.4427` n `8`; equity avg `0.2338` n `134`; fx avg `-0.09` n `6`; index avg `0.0516` n `26`; metal avg `0.0008` n `20`; unknown avg `0.4911` n `725`
- 24h: commodity avg `0.0867` n `12`; crypto_alt avg `-0.0802` n `232`; crypto_major avg `0.3156` n `8`; equity avg `0.532` n `134`; fx avg `-0.0785` n `6`; index avg `-0.0887` n `26`; metal avg `-0.4187` n `20`; unknown avg `6.4439` n `681`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
