# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T14:37:27.896143+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.0687` n `229`; crypto_major avg `0.0394` n `8`; equity avg `0.0133` n `88`; fx avg `0.0059` n `6`; index avg `-0.005` n `25`; metal avg `0.0037` n `20`; unknown avg `0.023` n `765`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.1633` n `229`; crypto_major avg `0.3189` n `8`; equity avg `0.0368` n `88`; fx avg `0.0091` n `6`; index avg `0.0059` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.0388` n `765`
- 4h: commodity avg `-0.0315` n `12`; crypto_alt avg `0.7588` n `229`; crypto_major avg `0.5736` n `8`; equity avg `-0.0844` n `88`; fx avg `0.0149` n `6`; index avg `0.0007` n `25`; metal avg `0.0047` n `20`; unknown avg `-0.0641` n `759`
- 24h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.9545` n `229`; crypto_major avg `1.6684` n `8`; equity avg `0.3246` n `88`; fx avg `-0.0452` n `6`; index avg `-0.0143` n `25`; metal avg `0.0343` n `20`; unknown avg `2.1504` n `741`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
