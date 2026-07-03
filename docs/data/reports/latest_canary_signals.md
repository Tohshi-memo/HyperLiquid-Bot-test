# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T02:37:30.221764+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.2634` n `229`; crypto_major avg `-0.3989` n `8`; equity avg `-0.1051` n `88`; fx avg `0.0244` n `6`; index avg `-0.0111` n `25`; metal avg `0.0501` n `20`; unknown avg `2.927` n `765`
- 1h: commodity avg `0.0995` n `12`; crypto_alt avg `-0.2086` n `229`; crypto_major avg `-0.4349` n `8`; equity avg `0.1167` n `88`; fx avg `0.0371` n `6`; index avg `0.0092` n `25`; metal avg `0.0363` n `20`; unknown avg `3.2428` n `765`
- 4h: commodity avg `0.1325` n `12`; crypto_alt avg `0.7103` n `229`; crypto_major avg `0.4249` n `8`; equity avg `0.8955` n `88`; fx avg `0.0721` n `6`; index avg `0.2135` n `25`; metal avg `0.6931` n `20`; unknown avg `3.9678` n `765`
- 24h: commodity avg `0.3368` n `12`; crypto_alt avg `2.039` n `228`; crypto_major avg `2.7867` n `8`; equity avg `-1.4652` n `88`; fx avg `-0.0723` n `6`; index avg `-0.2926` n `25`; metal avg `1.3253` n `20`; unknown avg `5.5345` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
