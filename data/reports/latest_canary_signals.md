# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T02:37:30.624262+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0184` n `12`; crypto_alt avg `-0.5094` n `232`; crypto_major avg `-0.3889` n `8`; equity avg `0.0163` n `134`; fx avg `0.0081` n `6`; index avg `0.0131` n `26`; metal avg `-0.053` n `20`; unknown avg `0.0555` n `797`
- 1h: commodity avg `0.0246` n `12`; crypto_alt avg `-0.3589` n `232`; crypto_major avg `-0.3323` n `8`; equity avg `0.1917` n `134`; fx avg `-0.0437` n `6`; index avg `0.0514` n `26`; metal avg `-0.1126` n `20`; unknown avg `1.2209` n `789`
- 4h: commodity avg `-0.0842` n `12`; crypto_alt avg `0.9757` n `232`; crypto_major avg `0.3696` n `8`; equity avg `0.6049` n `134`; fx avg `-0.1932` n `6`; index avg `0.1381` n `26`; metal avg `0.1029` n `20`; unknown avg `1.159` n `783`
- 24h: commodity avg `0.1191` n `12`; crypto_alt avg `0.5736` n `232`; crypto_major avg `-1.2536` n `8`; equity avg `0.6937` n `134`; fx avg `-0.3229` n `6`; index avg `0.1698` n `26`; metal avg `0.1585` n `20`; unknown avg `7691.974` n `650`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0851`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
