# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T14:52:25.380707+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0012` n `12`; crypto_alt avg `0.3193` n `232`; crypto_major avg `0.2625` n `8`; equity avg `0.061` n `134`; fx avg `0.001` n `6`; index avg `0.0077` n `26`; metal avg `0.0753` n `20`; unknown avg `-0.006` n `796`
- 1h: commodity avg `0.0389` n `12`; crypto_alt avg `-0.1452` n `232`; crypto_major avg `-0.3521` n `8`; equity avg `0.0062` n `134`; fx avg `-0.0277` n `6`; index avg `0.0041` n `26`; metal avg `0.116` n `20`; unknown avg `-0.0334` n `794`
- 4h: commodity avg `0.1925` n `12`; crypto_alt avg `0.4249` n `232`; crypto_major avg `-0.2129` n `8`; equity avg `-0.0378` n `134`; fx avg `-0.0126` n `6`; index avg `0.0016` n `26`; metal avg `0.1402` n `20`; unknown avg `6684.0504` n `748`
- 24h: commodity avg `0.1836` n `12`; crypto_alt avg `1.4031` n `232`; crypto_major avg `-0.4939` n `8`; equity avg `0.5376` n `134`; fx avg `-0.1324` n `6`; index avg `0.077` n `26`; metal avg `0.0253` n `20`; unknown avg `174.8626` n `680`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
