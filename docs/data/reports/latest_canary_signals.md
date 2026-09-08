# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T12:07:28.350679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.1274` n `232`; crypto_major avg `-0.1803` n `8`; equity avg `0.0809` n `134`; fx avg `0.0082` n `6`; index avg `0.0016` n `26`; metal avg `0.0276` n `20`; unknown avg `0.1805` n `795`
- 1h: commodity avg `0.0768` n `12`; crypto_alt avg `-0.5024` n `232`; crypto_major avg `-0.4319` n `8`; equity avg `0.0298` n `134`; fx avg `0.0185` n `6`; index avg `-0.0026` n `26`; metal avg `0.0704` n `20`; unknown avg `0.3044` n `795`
- 4h: commodity avg `0.0072` n `12`; crypto_alt avg `-0.0844` n `232`; crypto_major avg `-0.3249` n `8`; equity avg `0.5297` n `134`; fx avg `0.0333` n `6`; index avg `0.0686` n `26`; metal avg `0.0558` n `20`; unknown avg `-0.3053` n `787`
- 24h: commodity avg `0.3298` n `12`; crypto_alt avg `-0.4764` n `232`; crypto_major avg `-1.5328` n `8`; equity avg `-0.0596` n `134`; fx avg `-0.1175` n `6`; index avg `-0.0421` n `26`; metal avg `0.1893` n `20`; unknown avg `7374.8114` n `678`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
