# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T17:07:29.613590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0004` n `12`; crypto_alt avg `-0.0849` n `229`; crypto_major avg `-0.1966` n `8`; equity avg `-0.0434` n `88`; fx avg `0.0009` n `6`; index avg `-0.0235` n `25`; metal avg `-0.0157` n `20`; unknown avg `-0.0094` n `765`
- 1h: commodity avg `-0.0114` n `12`; crypto_alt avg `-0.1761` n `229`; crypto_major avg `-0.1429` n `8`; equity avg `-0.0924` n `88`; fx avg `-0.0085` n `6`; index avg `-0.0426` n `25`; metal avg `-0.0194` n `20`; unknown avg `0.0894` n `765`
- 4h: commodity avg `-0.0188` n `12`; crypto_alt avg `0.7998` n `229`; crypto_major avg `0.7086` n `8`; equity avg `0.0` n `88`; fx avg `0.0188` n `6`; index avg `-0.0366` n `25`; metal avg `0.0019` n `20`; unknown avg `0.2303` n `765`
- 24h: commodity avg `-0.0216` n `12`; crypto_alt avg `1.1285` n `229`; crypto_major avg `1.5158` n `8`; equity avg `0.1583` n `88`; fx avg `-0.0088` n `6`; index avg `-0.0751` n `25`; metal avg `0.02` n `20`; unknown avg `1.6436` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0671`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
