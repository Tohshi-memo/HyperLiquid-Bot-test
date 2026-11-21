# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T00:37:28.539131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `13`; crypto_alt avg `0.1019` n `239`; crypto_major avg `0.1995` n `8`; equity avg `0.2102` n `166`; fx avg `0.0064` n `6`; index avg `0.0123` n `27`; metal avg `0.0228` n `20`; unknown avg `0.9136` n `1262`
- 1h: commodity avg `-0.0326` n `13`; crypto_alt avg `-0.4371` n `239`; crypto_major avg `-0.0972` n `8`; equity avg `-0.2213` n `166`; fx avg `0.0069` n `6`; index avg `-0.0206` n `27`; metal avg `-0.0024` n `20`; unknown avg `160.5217` n `1250`
- 4h: commodity avg `-0.0335` n `13`; crypto_alt avg `1.3314` n `239`; crypto_major avg `1.4643` n `8`; equity avg `1.4684` n `166`; fx avg `-0.0291` n `6`; index avg `0.1903` n `27`; metal avg `0.2136` n `20`; unknown avg `167.7911` n `1200`
- 24h: commodity avg `0.2771` n `13`; crypto_alt avg `-4.9759` n `239`; crypto_major avg `-5.5404` n `8`; equity avg `-5.2437` n `166`; fx avg `-0.0684` n `6`; index avg `-0.5389` n `27`; metal avg `-0.5345` n `20`; unknown avg `12.3793` n `1119`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
