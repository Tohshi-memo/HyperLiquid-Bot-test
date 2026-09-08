# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T10:37:29.900226+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `-0.1691` n `232`; crypto_major avg `-0.2133` n `8`; equity avg `-0.1192` n `134`; fx avg `0.0014` n `6`; index avg `-0.0244` n `26`; metal avg `-0.0457` n `20`; unknown avg `0.3343` n `797`
- 1h: commodity avg `-0.1252` n `12`; crypto_alt avg `0.0282` n `232`; crypto_major avg `0.0192` n `8`; equity avg `0.14` n `134`; fx avg `-0.0176` n `6`; index avg `0.0298` n `26`; metal avg `0.036` n `20`; unknown avg `0.9742` n `795`
- 4h: commodity avg `0.0241` n `12`; crypto_alt avg `1.1408` n `232`; crypto_major avg `0.8453` n `8`; equity avg `0.3335` n `134`; fx avg `-0.0311` n `6`; index avg `0.0668` n `26`; metal avg `0.0497` n `20`; unknown avg `0.3957` n `787`
- 24h: commodity avg `0.3541` n `12`; crypto_alt avg `1.0396` n `232`; crypto_major avg `-0.4812` n `8`; equity avg `-0.1113` n `134`; fx avg `-0.1185` n `6`; index avg `-0.0528` n `26`; metal avg `0.1395` n `20`; unknown avg `7462.6742` n `670`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0758`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
