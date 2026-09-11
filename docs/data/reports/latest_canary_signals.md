# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T16:52:29.359916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0185` n `12`; crypto_alt avg `0.3498` n `233`; crypto_major avg `0.3369` n `8`; equity avg `0.0185` n `136`; fx avg `0.0032` n `6`; index avg `0.0087` n `26`; metal avg `0.0113` n `20`; unknown avg `0.0981` n `796`
- 1h: commodity avg `0.042` n `12`; crypto_alt avg `-0.2409` n `233`; crypto_major avg `-0.3771` n `8`; equity avg `-0.2149` n `136`; fx avg `0.003` n `6`; index avg `-0.0368` n `26`; metal avg `-0.0478` n `20`; unknown avg `0.0963` n `788`
- 4h: commodity avg `0.0865` n `12`; crypto_alt avg `0.9549` n `233`; crypto_major avg `0.6723` n `8`; equity avg `-0.3034` n `136`; fx avg `0.0226` n `6`; index avg `-0.0063` n `26`; metal avg `-0.1516` n `20`; unknown avg `1.113` n `772`
- 24h: commodity avg `-0.3056` n `12`; crypto_alt avg `1.9803` n `233`; crypto_major avg `2.5141` n `8`; equity avg `0.3595` n `136`; fx avg `-0.1533` n `6`; index avg `0.2766` n `26`; metal avg `0.0929` n `20`; unknown avg `2.7206` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0761`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
