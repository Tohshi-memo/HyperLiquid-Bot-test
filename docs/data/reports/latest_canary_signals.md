# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T08:22:27.382627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0047` n `12`; crypto_alt avg `0.0742` n `232`; crypto_major avg `0.1172` n `8`; equity avg `0.0113` n `134`; fx avg `0.003` n `6`; index avg `0.0029` n `26`; metal avg `0.0008` n `20`; unknown avg `0.0558` n `790`
- 1h: commodity avg `-0.0127` n `12`; crypto_alt avg `-0.0469` n `232`; crypto_major avg `0.2325` n `8`; equity avg `-0.0086` n `134`; fx avg `0.0117` n `6`; index avg `-0.0098` n `26`; metal avg `-0.0016` n `20`; unknown avg `0.4737` n `788`
- 4h: commodity avg `-0.0294` n `12`; crypto_alt avg `0.9426` n `232`; crypto_major avg `0.8162` n `8`; equity avg `0.1313` n `134`; fx avg `-0.0092` n `6`; index avg `0.0401` n `26`; metal avg `0.0256` n `20`; unknown avg `15.7634` n `746`
- 24h: commodity avg `0.1543` n `12`; crypto_alt avg `0.9549` n `232`; crypto_major avg `-0.9485` n `8`; equity avg `0.9227` n `134`; fx avg `-0.1276` n `6`; index avg `0.0664` n `26`; metal avg `-0.2484` n `20`; unknown avg `16.4327` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
