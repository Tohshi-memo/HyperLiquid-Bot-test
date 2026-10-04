# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-04T01:37:29.078570+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0075` n `13`; crypto_alt avg `-0.0632` n `235`; crypto_major avg `0.0007` n `8`; equity avg `0.0141` n `143`; fx avg `-0.0006` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0005` n `20`; unknown avg `0.0181` n `1079`
- 1h: commodity avg `-0.0067` n `13`; crypto_alt avg `-0.2288` n `235`; crypto_major avg `-0.1113` n `8`; equity avg `-0.021` n `143`; fx avg `-0.0022` n `6`; index avg `-0.0088` n `26`; metal avg `0.003` n `20`; unknown avg `-0.0472` n `1077`
- 4h: commodity avg `-0.0454` n `13`; crypto_alt avg `0.0758` n `235`; crypto_major avg `0.0419` n `8`; equity avg `0.0273` n `143`; fx avg `-0.0031` n `6`; index avg `-0.0089` n `26`; metal avg `-0.0003` n `20`; unknown avg `-0.1264` n `1055`
- 24h: commodity avg `0.1453` n `13`; crypto_alt avg `1.2934` n `235`; crypto_major avg `0.3196` n `8`; equity avg `0.158` n `143`; fx avg `-0.0279` n `6`; index avg `0.0156` n `26`; metal avg `0.0081` n `20`; unknown avg `-0.0533` n `898`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1985`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.156`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1552`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
