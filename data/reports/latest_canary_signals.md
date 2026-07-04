# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T20:52:29.084329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.0626` n `229`; crypto_major avg `0.0007` n `8`; equity avg `0.0199` n `88`; fx avg `0.0138` n `6`; index avg `-0.0008` n `25`; metal avg `0.024` n `20`; unknown avg `-0.0825` n `765`
- 1h: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.2669` n `229`; crypto_major avg `-0.2311` n `8`; equity avg `0.0147` n `88`; fx avg `0.0168` n `6`; index avg `-0.0002` n `25`; metal avg `0.0177` n `20`; unknown avg `-0.1813` n `765`
- 4h: commodity avg `-0.0375` n `12`; crypto_alt avg `-0.3859` n `229`; crypto_major avg `-0.3515` n `8`; equity avg `0.0533` n `88`; fx avg `-0.0302` n `6`; index avg `0.0113` n `25`; metal avg `0.0362` n `20`; unknown avg `-0.928` n `765`
- 24h: commodity avg `0.042` n `12`; crypto_alt avg `0.0981` n `229`; crypto_major avg `0.2119` n `8`; equity avg `0.2859` n `88`; fx avg `-0.0218` n `6`; index avg `-0.0146` n `25`; metal avg `0.0836` n `20`; unknown avg `-0.1492` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0779`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
