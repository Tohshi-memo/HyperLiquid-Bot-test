# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T22:37:27.060630+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0141` n `12`; crypto_alt avg `0.0187` n `229`; crypto_major avg `0.0145` n `8`; equity avg `-0.0043` n `88`; fx avg `0.0088` n `6`; index avg `0.0089` n `25`; metal avg `-0.0008` n `20`; unknown avg `-0.1603` n `765`
- 1h: commodity avg `0.0429` n `12`; crypto_alt avg `-0.3424` n `229`; crypto_major avg `-0.1571` n `8`; equity avg `-0.013` n `88`; fx avg `0.0122` n `6`; index avg `0.0191` n `25`; metal avg `-0.0143` n `20`; unknown avg `0.0787` n `765`
- 4h: commodity avg `0.004` n `12`; crypto_alt avg `-0.5686` n `229`; crypto_major avg `-0.3927` n `8`; equity avg `0.0985` n `88`; fx avg `-0.0176` n `6`; index avg `0.037` n `25`; metal avg `0.0387` n `20`; unknown avg `-0.6436` n `765`
- 24h: commodity avg `0.017` n `12`; crypto_alt avg `0.1278` n `229`; crypto_major avg `0.618` n `8`; equity avg `0.3027` n `88`; fx avg `-0.023` n `6`; index avg `0.0095` n `25`; metal avg `0.0927` n `20`; unknown avg `-0.1094` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0752`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
