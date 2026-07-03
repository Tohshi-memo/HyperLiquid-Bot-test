# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T13:07:31.262131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0965` n `12`; crypto_alt avg `0.1464` n `229`; crypto_major avg `0.2189` n `8`; equity avg `-0.0927` n `88`; fx avg `-0.0112` n `6`; index avg `-0.0043` n `25`; metal avg `-0.0733` n `20`; unknown avg `0.2423` n `765`
- 1h: commodity avg `0.1047` n `12`; crypto_alt avg `-0.0195` n `229`; crypto_major avg `-0.0779` n `8`; equity avg `-0.1667` n `88`; fx avg `-0.0055` n `6`; index avg `-0.0111` n `25`; metal avg `-0.1045` n `20`; unknown avg `0.213` n `765`
- 4h: commodity avg `-0.0026` n `12`; crypto_alt avg `0.9326` n `229`; crypto_major avg `0.7155` n `8`; equity avg `0.0855` n `88`; fx avg `0.0218` n `6`; index avg `0.0549` n `25`; metal avg `-0.1697` n `20`; unknown avg `1.4661` n `755`
- 24h: commodity avg `0.5073` n `12`; crypto_alt avg `1.8915` n `229`; crypto_major avg `1.927` n `8`; equity avg `-0.7424` n `88`; fx avg `-0.1172` n `6`; index avg `0.0674` n `25`; metal avg `0.5601` n `20`; unknown avg `6.8193` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
