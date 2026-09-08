# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T06:37:30.848227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.2192` n `232`; crypto_major avg `-0.1554` n `8`; equity avg `0.0104` n `134`; fx avg `0.0199` n `6`; index avg `-0.0297` n `26`; metal avg `-0.0353` n `20`; unknown avg `0.7563` n `795`
- 1h: commodity avg `0.0613` n `12`; crypto_alt avg `-0.672` n `232`; crypto_major avg `-0.5318` n `8`; equity avg `-0.6607` n `134`; fx avg `0.0634` n `6`; index avg `-0.1685` n `26`; metal avg `-0.1716` n `20`; unknown avg `0.4022` n `761`
- 4h: commodity avg `0.2068` n `12`; crypto_alt avg `-0.8501` n `232`; crypto_major avg `-0.8305` n `8`; equity avg `-1.0332` n `134`; fx avg `0.1526` n `6`; index avg `-0.2648` n `26`; metal avg `-0.1594` n `20`; unknown avg `1.3514` n `747`
- 24h: commodity avg `0.201` n `12`; crypto_alt avg `-0.0705` n `232`; crypto_major avg `-1.4552` n `8`; equity avg `-0.4488` n `134`; fx avg `-0.1426` n `6`; index avg `-0.129` n `26`; metal avg `0.0999` n `20`; unknown avg `7509.6268` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
