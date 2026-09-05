# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T08:37:28.091096+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `-0.0417` n `232`; crypto_major avg `0.0428` n `8`; equity avg `0.0083` n `134`; fx avg `0.0031` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0088` n `20`; unknown avg `0.0883` n `784`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `-0.1455` n `232`; crypto_major avg `0.098` n `8`; equity avg `-0.0051` n `134`; fx avg `0.0146` n `6`; index avg `-0.0247` n `26`; metal avg `-0.0138` n `20`; unknown avg `0.1574` n `782`
- 4h: commodity avg `-0.034` n `12`; crypto_alt avg `0.9586` n `232`; crypto_major avg `0.8736` n `8`; equity avg `0.1018` n `134`; fx avg `-0.0061` n `6`; index avg `0.0229` n `26`; metal avg `0.0151` n `20`; unknown avg `15.9774` n `746`
- 24h: commodity avg `0.1563` n `12`; crypto_alt avg `0.9299` n `232`; crypto_major avg `-1.0526` n `8`; equity avg `0.8878` n `134`; fx avg `-0.1012` n `6`; index avg `0.0672` n `26`; metal avg `-0.2487` n `20`; unknown avg `16.4656` n `648`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
