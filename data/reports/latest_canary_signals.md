# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T09:22:31.974079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0216` n `12`; crypto_alt avg `0.037` n `228`; crypto_major avg `0.0939` n `8`; equity avg `0.0075` n `86`; fx avg `-0.0089` n `6`; index avg `-0.0199` n `23`; metal avg `0.0867` n `20`; unknown avg `-0.0136` n `765`
- 1h: commodity avg `-0.0967` n `12`; crypto_alt avg `-0.2553` n `228`; crypto_major avg `-0.4477` n `8`; equity avg `-0.3366` n `86`; fx avg `-0.0019` n `6`; index avg `-0.0748` n `23`; metal avg `0.1335` n `20`; unknown avg `0.0041` n `765`
- 4h: commodity avg `-0.1603` n `12`; crypto_alt avg `1.0767` n `228`; crypto_major avg `1.0264` n `8`; equity avg `0.2275` n `86`; fx avg `-0.0463` n `6`; index avg `0.0459` n `23`; metal avg `0.7086` n `20`; unknown avg `0.238` n `733`
- 24h: commodity avg `-0.0246` n `12`; crypto_alt avg `-1.425` n `228`; crypto_major avg `-1.6989` n `8`; equity avg `-3.9985` n `86`; fx avg `0.0051` n `6`; index avg `-0.5884` n `23`; metal avg `0.5056` n `20`; unknown avg `0.9741` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.2578`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1749`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
