# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T03:07:40.609625+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0116` n `13`; crypto_alt avg `0.2322` n `234`; crypto_major avg `0.0671` n `8`; equity avg `0.1043` n `142`; fx avg `-0.0081` n `6`; index avg `0.0255` n `26`; metal avg `0.0545` n `20`; unknown avg `0.0881` n `972`
- 1h: commodity avg `0.1663` n `13`; crypto_alt avg `0.6058` n `234`; crypto_major avg `-0.0097` n `8`; equity avg `0.2834` n `142`; fx avg `-0.0154` n `6`; index avg `0.0779` n `26`; metal avg `0.089` n `20`; unknown avg `0.1075` n `972`
- 4h: commodity avg `-0.1156` n `13`; crypto_alt avg `0.2863` n `234`; crypto_major avg `-0.3039` n `8`; equity avg `0.4578` n `142`; fx avg `0.0893` n `6`; index avg `0.1511` n `26`; metal avg `0.0806` n `20`; unknown avg `1.4894` n `942`
- 24h: commodity avg `-0.0201` n `13`; crypto_alt avg `1.0007` n `234`; crypto_major avg `0.5851` n `8`; equity avg `0.362` n `142`; fx avg `0.2063` n `6`; index avg `0.1768` n `26`; metal avg `-0.1258` n `20`; unknown avg `775.4028` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.15`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
