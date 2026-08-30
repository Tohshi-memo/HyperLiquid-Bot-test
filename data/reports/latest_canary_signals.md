# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T07:07:28.954622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0828` n `231`; crypto_major avg `0.0117` n `8`; equity avg `0.022` n `128`; fx avg `0.0` n `6`; index avg `0.005` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.0081` n `793`
- 1h: commodity avg `0.0225` n `12`; crypto_alt avg `0.0659` n `231`; crypto_major avg `0.1472` n `8`; equity avg `0.0274` n `128`; fx avg `-0.0004` n `6`; index avg `0.0` n `26`; metal avg `0.0069` n `20`; unknown avg `0.0605` n `789`
- 4h: commodity avg `0.0094` n `12`; crypto_alt avg `0.3137` n `231`; crypto_major avg `0.1508` n `8`; equity avg `0.0654` n `128`; fx avg `0.009` n `6`; index avg `-0.0023` n `26`; metal avg `0.0142` n `20`; unknown avg `0.0137` n `759`
- 24h: commodity avg `0.0051` n `12`; crypto_alt avg `0.848` n `231`; crypto_major avg `1.0385` n `8`; equity avg `0.3129` n `128`; fx avg `0.0025` n `6`; index avg `0.0632` n `26`; metal avg `0.1091` n `20`; unknown avg `0.7618` n `714`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.174`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1161`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1084`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
