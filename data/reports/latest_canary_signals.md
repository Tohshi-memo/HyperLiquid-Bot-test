# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T18:37:30.768436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0003` n `13`; crypto_alt avg `0.1981` n `234`; crypto_major avg `0.2548` n `8`; equity avg `0.1978` n `142`; fx avg `0.0172` n `6`; index avg `0.0512` n `26`; metal avg `0.0368` n `20`; unknown avg `0.2038` n `975`
- 1h: commodity avg `0.1484` n `13`; crypto_alt avg `0.2297` n `234`; crypto_major avg `0.1421` n `8`; equity avg `-0.1316` n `142`; fx avg `0.0487` n `6`; index avg `-0.0103` n `26`; metal avg `-0.0275` n `20`; unknown avg `-0.527` n `973`
- 4h: commodity avg `0.0936` n `13`; crypto_alt avg `0.7511` n `234`; crypto_major avg `0.3578` n `8`; equity avg `0.9012` n `142`; fx avg `-0.07` n `6`; index avg `0.1669` n `26`; metal avg `-0.0163` n `20`; unknown avg `1.119` n `931`
- 24h: commodity avg `-0.0994` n `13`; crypto_alt avg `0.4296` n `234`; crypto_major avg `0.6461` n `8`; equity avg `1.0894` n `142`; fx avg `-0.0898` n `6`; index avg `0.1557` n `26`; metal avg `0.0015` n `20`; unknown avg `0.1431` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
