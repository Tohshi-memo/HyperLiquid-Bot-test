# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T10:37:32.804041+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0273` n `12`; crypto_alt avg `0.0426` n `232`; crypto_major avg `-0.0007` n `8`; equity avg `-0.0119` n `134`; fx avg `0.0066` n `6`; index avg `-0.005` n `26`; metal avg `-0.0324` n `20`; unknown avg `0.5154` n `796`
- 1h: commodity avg `0.0383` n `12`; crypto_alt avg `-0.0029` n `232`; crypto_major avg `0.0146` n `8`; equity avg `0.0067` n `134`; fx avg `0.0425` n `6`; index avg `-0.001` n `26`; metal avg `-0.0856` n `20`; unknown avg `0.6277` n `794`
- 4h: commodity avg `-0.1264` n `12`; crypto_alt avg `0.0885` n `232`; crypto_major avg `-0.1351` n `8`; equity avg `-0.0073` n `134`; fx avg `-0.0559` n `6`; index avg `-0.01` n `26`; metal avg `0.0105` n `20`; unknown avg `2.2094` n `784`
- 24h: commodity avg `-0.0315` n `12`; crypto_alt avg `0.0941` n `232`; crypto_major avg `-0.7315` n `8`; equity avg `0.3045` n `134`; fx avg `-0.1254` n `6`; index avg `0.0293` n `26`; metal avg `-0.1454` n `20`; unknown avg `76.3102` n `648`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1939`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
