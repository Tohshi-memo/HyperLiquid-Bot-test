# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T21:22:28.705951+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0128` n `13`; crypto_alt avg `0.3682` n `236`; crypto_major avg `0.253` n `8`; equity avg `-0.0367` n `151`; fx avg `-0.0029` n `6`; index avg `0.003` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.2359` n `1193`
- 1h: commodity avg `0.0843` n `13`; crypto_alt avg `0.5627` n `236`; crypto_major avg `0.4922` n `8`; equity avg `0.0623` n `151`; fx avg `0.0045` n `6`; index avg `0.0119` n `26`; metal avg `0.0092` n `20`; unknown avg `3.5772` n `1185`
- 4h: commodity avg `0.1842` n `13`; crypto_alt avg `1.192` n `236`; crypto_major avg `1.1536` n `8`; equity avg `-0.3377` n `151`; fx avg `0.0153` n `6`; index avg `-0.0496` n `26`; metal avg `0.026` n `20`; unknown avg `11.2884` n `1109`
- 24h: commodity avg `0.4354` n `13`; crypto_alt avg `-1.5222` n `236`; crypto_major avg `-1.3415` n `8`; equity avg `-3.6952` n `151`; fx avg `0.0444` n `6`; index avg `-0.6162` n `26`; metal avg `-0.1063` n `20`; unknown avg `0.3752` n `896`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1621`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.112`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0881`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0766`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0719`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
