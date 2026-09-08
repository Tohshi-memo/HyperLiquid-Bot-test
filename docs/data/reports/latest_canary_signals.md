# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T06:22:31.273292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0174` n `12`; crypto_alt avg `-0.291` n `232`; crypto_major avg `-0.1831` n `8`; equity avg `-0.2917` n `134`; fx avg `0.0428` n `6`; index avg `-0.0416` n `26`; metal avg `-0.0571` n `20`; unknown avg `0.3205` n `797`
- 1h: commodity avg `0.1089` n `12`; crypto_alt avg `-0.4613` n `232`; crypto_major avg `-0.3953` n `8`; equity avg `-0.952` n `134`; fx avg `0.0746` n `6`; index avg `-0.2051` n `26`; metal avg `-0.1952` n `20`; unknown avg `0.7771` n `763`
- 4h: commodity avg `0.237` n `12`; crypto_alt avg `-1.1333` n `232`; crypto_major avg `-1.0629` n `8`; equity avg `-1.0274` n `134`; fx avg `0.1409` n `6`; index avg `-0.2229` n `26`; metal avg `-0.1771` n `20`; unknown avg `0.2869` n `749`
- 24h: commodity avg `0.2071` n `12`; crypto_alt avg `0.0879` n `232`; crypto_major avg `-1.4524` n `8`; equity avg `-0.4725` n `134`; fx avg `-0.1412` n `6`; index avg `-0.0761` n `26`; metal avg `0.1558` n `20`; unknown avg `7508.947` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1017`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0868`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
