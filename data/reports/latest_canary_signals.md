# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T03:07:28.061634+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `12`; crypto_alt avg `-0.0471` n `230`; crypto_major avg `-0.0699` n `8`; equity avg `-0.0622` n `102`; fx avg `0.024` n `6`; index avg `-0.0095` n `25`; metal avg `-0.005` n `20`; unknown avg `0.5104` n `784`
- 1h: commodity avg `-0.0154` n `12`; crypto_alt avg `-0.0412` n `230`; crypto_major avg `-0.0663` n `8`; equity avg `-0.0523` n `102`; fx avg `0.0034` n `6`; index avg `-0.033` n `25`; metal avg `-0.0058` n `20`; unknown avg `-0.0731` n `784`
- 4h: commodity avg `-0.1313` n `12`; crypto_alt avg `-0.5548` n `230`; crypto_major avg `-0.6161` n `8`; equity avg `0.2377` n `102`; fx avg `-0.2548` n `6`; index avg `-0.0828` n `25`; metal avg `-0.0528` n `20`; unknown avg `-0.2192` n `784`
- 24h: commodity avg `-0.0599` n `12`; crypto_alt avg `-0.6144` n `230`; crypto_major avg `-0.3223` n `8`; equity avg `0.8724` n `102`; fx avg `-0.2608` n `6`; index avg `0.0591` n `25`; metal avg `-0.0089` n `20`; unknown avg `1.2924` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
