# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T11:52:33.617214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0461` n `13`; crypto_alt avg `0.1269` n `234`; crypto_major avg `0.1962` n `8`; equity avg `-0.0001` n `142`; fx avg `0.012` n `6`; index avg `0.0377` n `26`; metal avg `0.0985` n `20`; unknown avg `1.2311` n `975`
- 1h: commodity avg `0.2088` n `13`; crypto_alt avg `0.126` n `234`; crypto_major avg `0.2279` n `8`; equity avg `-0.2374` n `142`; fx avg `0.0117` n `6`; index avg `-0.0225` n `26`; metal avg `0.0737` n `20`; unknown avg `1.4014` n `973`
- 4h: commodity avg `-0.1606` n `13`; crypto_alt avg `-0.1333` n `234`; crypto_major avg `0.6867` n `8`; equity avg `0.0093` n `142`; fx avg `-0.0215` n `6`; index avg `0.0859` n `26`; metal avg `0.1374` n `20`; unknown avg `9.1628` n `957`
- 24h: commodity avg `-0.2624` n `13`; crypto_alt avg `-0.663` n `234`; crypto_major avg `0.2145` n `8`; equity avg `0.5586` n `142`; fx avg `0.0479` n `6`; index avg `0.2366` n `26`; metal avg `-0.0368` n `20`; unknown avg `774.0995` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
