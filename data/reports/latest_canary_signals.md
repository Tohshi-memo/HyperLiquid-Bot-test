# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T22:52:27.298452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.04` n `12`; crypto_alt avg `0.0481` n `232`; crypto_major avg `0.0275` n `8`; equity avg `0.0269` n `134`; fx avg `0.0016` n `6`; index avg `-0.0064` n `26`; metal avg `0.023` n `20`; unknown avg `0.0594` n `793`
- 1h: commodity avg `-0.0129` n `12`; crypto_alt avg `-0.2936` n `232`; crypto_major avg `-0.1311` n `8`; equity avg `-0.0504` n `134`; fx avg `0.005` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0128` n `20`; unknown avg `0.3115` n `791`
- 4h: commodity avg `-0.0454` n `12`; crypto_alt avg `0.4116` n `232`; crypto_major avg `0.2843` n `8`; equity avg `0.0232` n `134`; fx avg `0.0361` n `6`; index avg `0.0057` n `26`; metal avg `-0.0247` n `20`; unknown avg `151.2835` n `761`
- 24h: commodity avg `-0.0359` n `12`; crypto_alt avg `1.1652` n `232`; crypto_major avg `0.5582` n `8`; equity avg `0.2734` n `134`; fx avg `0.0281` n `6`; index avg `0.0148` n `26`; metal avg `-0.065` n `20`; unknown avg `151.4692` n `678`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
