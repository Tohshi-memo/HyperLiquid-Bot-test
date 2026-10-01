# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T11:22:29.073338+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `0.0721` n `234`; crypto_major avg `0.004` n `8`; equity avg `-0.1384` n `142`; fx avg `-0.0088` n `6`; index avg `-0.0398` n `26`; metal avg `-0.0486` n `20`; unknown avg `0.0978` n `975`
- 1h: commodity avg `-0.0135` n `13`; crypto_alt avg `0.2703` n `234`; crypto_major avg `0.4138` n `8`; equity avg `0.0297` n `142`; fx avg `0.0071` n `6`; index avg `-0.0016` n `26`; metal avg `0.0334` n `20`; unknown avg `-0.2878` n `973`
- 4h: commodity avg `-0.1163` n `13`; crypto_alt avg `-0.8446` n `234`; crypto_major avg `0.0792` n `8`; equity avg `-0.1893` n `142`; fx avg `-0.0594` n `6`; index avg `-0.0168` n `26`; metal avg `-0.0498` n `20`; unknown avg `7.2402` n `957`
- 24h: commodity avg `-0.1824` n `13`; crypto_alt avg `-0.6572` n `234`; crypto_major avg `0.0917` n `8`; equity avg `0.6243` n `142`; fx avg `0.0402` n `6`; index avg `0.1944` n `26`; metal avg `-0.1695` n `20`; unknown avg `776.6477` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1664`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1123`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
