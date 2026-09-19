# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T13:37:33.740084+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `12`; crypto_alt avg `0.0376` n `234`; crypto_major avg `-0.0489` n `8`; equity avg `0.0224` n `140`; fx avg `0.0065` n `6`; index avg `0.0021` n `26`; metal avg `0.0078` n `20`; unknown avg `0.0125` n `940`
- 1h: commodity avg `0.0132` n `12`; crypto_alt avg `-0.1245` n `234`; crypto_major avg `0.0731` n `8`; equity avg `0.0223` n `140`; fx avg `0.0021` n `6`; index avg `-0.0016` n `26`; metal avg `-0.001` n `20`; unknown avg `-0.2256` n `938`
- 4h: commodity avg `0.0214` n `12`; crypto_alt avg `0.7487` n `234`; crypto_major avg `0.6465` n `8`; equity avg `0.0645` n `140`; fx avg `-0.033` n `6`; index avg `0.0004` n `26`; metal avg `0.0285` n `20`; unknown avg `0.3884` n `932`
- 24h: commodity avg `-0.1114` n `12`; crypto_alt avg `3.5183` n `234`; crypto_major avg `3.5376` n `8`; equity avg `0.5246` n `140`; fx avg `-0.0196` n `6`; index avg `0.0545` n `26`; metal avg `0.059` n `20`; unknown avg `2.3628` n `806`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1627`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
