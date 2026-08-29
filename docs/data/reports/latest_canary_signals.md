# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-29T19:37:27.076488+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0026` n `12`; crypto_alt avg `-0.0502` n `231`; crypto_major avg `-0.0144` n `8`; equity avg `0.0761` n `128`; fx avg `-0.0074` n `6`; index avg `0.0066` n `26`; metal avg `0.0003` n `20`; unknown avg `0.2742` n `792`
- 1h: commodity avg `-0.0105` n `12`; crypto_alt avg `0.0695` n `231`; crypto_major avg `0.0997` n `8`; equity avg `0.1263` n `128`; fx avg `-0.0157` n `6`; index avg `0.025` n `26`; metal avg `0.0069` n `20`; unknown avg `0.2206` n `792`
- 4h: commodity avg `0.063` n `12`; crypto_alt avg `0.1115` n `231`; crypto_major avg `0.3002` n `8`; equity avg `0.1643` n `128`; fx avg `-0.0184` n `6`; index avg `0.0202` n `26`; metal avg `0.0299` n `20`; unknown avg `-0.0677` n `788`
- 24h: commodity avg `-0.0201` n `12`; crypto_alt avg `0.8758` n `231`; crypto_major avg `1.1587` n `8`; equity avg `0.3699` n `128`; fx avg `-0.0536` n `6`; index avg `0.0538` n `26`; metal avg `0.1037` n `20`; unknown avg `0.2063` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2257`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
