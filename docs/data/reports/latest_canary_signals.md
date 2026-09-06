# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T10:07:30.979554+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0066` n `12`; crypto_alt avg `-0.0038` n `232`; crypto_major avg `0.0291` n `8`; equity avg `0.0476` n `134`; fx avg `0.0098` n `6`; index avg `0.0186` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.1731` n `792`
- 1h: commodity avg `0.0061` n `12`; crypto_alt avg `0.2209` n `232`; crypto_major avg `0.2492` n `8`; equity avg `0.0944` n `134`; fx avg `0.0147` n `6`; index avg `0.0253` n `26`; metal avg `0.0064` n `20`; unknown avg `0.5644` n `792`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `-0.0018` n `232`; crypto_major avg `-0.1307` n `8`; equity avg `0.0935` n `134`; fx avg `0.0122` n `6`; index avg `0.0117` n `26`; metal avg `-0.0084` n `20`; unknown avg `-0.2337` n `782`
- 24h: commodity avg `0.1702` n `12`; crypto_alt avg `1.8549` n `232`; crypto_major avg `2.0759` n `8`; equity avg `0.4443` n `134`; fx avg `-0.0246` n `6`; index avg `0.1056` n `26`; metal avg `0.022` n `20`; unknown avg `493.2317` n `676`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1082`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
