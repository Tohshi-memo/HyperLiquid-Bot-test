# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-08T17:13:53.343053+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0624` n `12`; crypto_alt avg `0.1898` n `229`; crypto_major avg `0.0401` n `8`; equity avg `-0.034` n `91`; fx avg `0.0154` n `6`; index avg `0.0298` n `25`; metal avg `0.0388` n `20`; unknown avg `0.0322` n `764`
- 1h: commodity avg `-0.3176` n `12`; crypto_alt avg `0.511` n `229`; crypto_major avg `0.4073` n `8`; equity avg `0.6208` n `91`; fx avg `0.0111` n `6`; index avg `0.2112` n `25`; metal avg `0.2726` n `20`; unknown avg `0.1525` n `764`
- 4h: commodity avg `-0.0989` n `12`; crypto_alt avg `0.689` n `229`; crypto_major avg `0.2783` n `8`; equity avg `0.9889` n `91`; fx avg `0.0814` n `6`; index avg `0.2373` n `25`; metal avg `-0.1077` n `20`; unknown avg `-0.1082` n `764`
- 24h: commodity avg `0.7798` n `12`; crypto_alt avg `-3.5262` n `229`; crypto_major avg `-3.8861` n `8`; equity avg `-0.4823` n `91`; fx avg `0.0171` n `6`; index avg `-0.1963` n `25`; metal avg `-1.2964` n `20`; unknown avg `-0.4416` n `737`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1043`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
