# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T15:12:55.007301+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1674` n `12`; crypto_alt avg `-0.1032` n `230`; crypto_major avg `-0.0482` n `8`; equity avg `0.0245` n `113`; fx avg `0.004` n `6`; index avg `0.022` n `25`; metal avg `-0.0835` n `20`; unknown avg `0.1146` n `787`
- 1h: commodity avg `0.3327` n `12`; crypto_alt avg `0.1866` n `230`; crypto_major avg `0.1914` n `8`; equity avg `0.3354` n `113`; fx avg `-0.001` n `6`; index avg `0.0889` n `25`; metal avg `-0.0407` n `20`; unknown avg `-0.0576` n `787`
- 4h: commodity avg `0.0245` n `12`; crypto_alt avg `0.3677` n `230`; crypto_major avg `0.3842` n `8`; equity avg `1.7107` n `113`; fx avg `-0.0278` n `6`; index avg `0.3078` n `25`; metal avg `-0.1669` n `20`; unknown avg `0.1531` n `787`
- 24h: commodity avg `-0.3647` n `12`; crypto_alt avg `0.0786` n `230`; crypto_major avg `0.5662` n `8`; equity avg `1.9787` n `113`; fx avg `0.0113` n `6`; index avg `0.3543` n `25`; metal avg `-0.5604` n `20`; unknown avg `0.3237` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2273`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.198`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1765`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.175`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
