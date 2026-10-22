# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T03:07:30.654619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.66` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.5708` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0227` n `13`; crypto_alt avg `0.0272` n `237`; crypto_major avg `0.0211` n `8`; equity avg `-0.0036` n `151`; fx avg `0.0061` n `6`; index avg `-0.0146` n `26`; metal avg `-0.0033` n `20`; unknown avg `1.013` n `1197`
- 1h: commodity avg `0.0127` n `13`; crypto_alt avg `-0.4607` n `237`; crypto_major avg `-0.4362` n `8`; equity avg `-0.2874` n `151`; fx avg `0.0112` n `6`; index avg `-0.0391` n `26`; metal avg `0.001` n `20`; unknown avg `0.0384` n `1195`
- 4h: commodity avg `0.1459` n `13`; crypto_alt avg `-1.7462` n `237`; crypto_major avg `-1.6958` n `8`; equity avg `-1.1303` n `151`; fx avg `-0.0334` n `6`; index avg `-0.125` n `26`; metal avg `-0.3685` n `20`; unknown avg `11.4317` n `1189`
- 24h: commodity avg `-0.6041` n `13`; crypto_alt avg `-0.3261` n `237`; crypto_major avg `-0.5778` n `8`; equity avg `-1.8611` n `151`; fx avg `-0.052` n `6`; index avg `-0.2777` n `26`; metal avg `-0.4241` n `20`; unknown avg `121.3797` n `942`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1455`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
