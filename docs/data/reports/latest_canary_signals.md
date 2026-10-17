# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T14:52:33.869446+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `13`; crypto_alt avg `0.0535` n `236`; crypto_major avg `0.0338` n `8`; equity avg `-0.0065` n `151`; fx avg `-0.0025` n `6`; index avg `-0.0155` n `26`; metal avg `-0.003` n `20`; unknown avg `0.3073` n `1185`
- 1h: commodity avg `0.0244` n `13`; crypto_alt avg `0.2587` n `236`; crypto_major avg `0.2476` n `8`; equity avg `0.0084` n `151`; fx avg `-0.0075` n `6`; index avg `-0.0109` n `26`; metal avg `-0.0077` n `20`; unknown avg `2.5743` n `1181`
- 4h: commodity avg `0.0476` n `13`; crypto_alt avg `-0.8598` n `236`; crypto_major avg `-0.3586` n `8`; equity avg `-0.17` n `151`; fx avg `-0.0086` n `6`; index avg `-0.0402` n `26`; metal avg `-0.0181` n `20`; unknown avg `3.5505` n `1175`
- 24h: commodity avg `0.7419` n `13`; crypto_alt avg `-2.9444` n `236`; crypto_major avg `-1.5301` n `8`; equity avg `-2.2983` n `151`; fx avg `-0.033` n `6`; index avg `-0.4621` n `26`; metal avg `-0.2755` n `20`; unknown avg `3.2419` n `1032`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1726`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1436`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1169`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1115`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0707`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
