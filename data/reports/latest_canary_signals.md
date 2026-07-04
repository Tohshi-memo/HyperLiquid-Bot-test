# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T11:54:48.434369+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0093` n `12`; crypto_alt avg `-0.0101` n `229`; crypto_major avg `-0.0581` n `8`; equity avg `-0.0223` n `88`; fx avg `-0.0094` n `6`; index avg `0.0003` n `25`; metal avg `-0.0082` n `20`; unknown avg `-0.0178` n `765`
- 1h: commodity avg `0.0189` n `12`; crypto_alt avg `0.364` n `229`; crypto_major avg `-0.0007` n `8`; equity avg `-0.0669` n `88`; fx avg `0.0192` n `6`; index avg `-0.0048` n `25`; metal avg `0.0037` n `20`; unknown avg `-0.0064` n `765`
- 4h: commodity avg `0.1205` n `12`; crypto_alt avg `0.2861` n `229`; crypto_major avg `-0.2385` n `8`; equity avg `-0.0183` n `88`; fx avg `-0.0074` n `6`; index avg `0.0274` n `25`; metal avg `0.0201` n `20`; unknown avg `0.2013` n `765`
- 24h: commodity avg `0.1529` n `12`; crypto_alt avg `0.8924` n `229`; crypto_major avg `1.076` n `8`; equity avg `0.1267` n `88`; fx avg `-0.0806` n `6`; index avg `-0.0287` n `25`; metal avg `-0.0716` n `20`; unknown avg `2.894` n `743`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0567`, n `668`, weak_sample_signal
