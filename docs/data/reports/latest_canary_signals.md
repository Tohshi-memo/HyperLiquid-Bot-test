# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T20:22:30.005444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0452` n `13`; crypto_alt avg `0.0718` n `234`; crypto_major avg `0.0121` n `8`; equity avg `0.0538` n `142`; fx avg `-0.0108` n `6`; index avg `0.0065` n `26`; metal avg `-0.0011` n `20`; unknown avg `0.2364` n `943`
- 1h: commodity avg `-0.0267` n `13`; crypto_alt avg `0.414` n `234`; crypto_major avg `0.1823` n `8`; equity avg `0.0523` n `142`; fx avg `0.0033` n `6`; index avg `0.0176` n `26`; metal avg `-0.0074` n `20`; unknown avg `0.2482` n `933`
- 4h: commodity avg `0.2813` n `13`; crypto_alt avg `0.8826` n `234`; crypto_major avg `0.6451` n `8`; equity avg `0.9509` n `142`; fx avg `-0.0114` n `6`; index avg `0.201` n `26`; metal avg `0.1346` n `20`; unknown avg `0.8817` n `933`
- 24h: commodity avg `-0.0051` n `13`; crypto_alt avg `-0.0676` n `234`; crypto_major avg `0.1328` n `8`; equity avg `0.986` n `142`; fx avg `-0.1114` n `6`; index avg `0.2063` n `26`; metal avg `-0.0002` n `20`; unknown avg `0.6101` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1723`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
