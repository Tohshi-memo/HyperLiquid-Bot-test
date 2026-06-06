# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T23:22:26.157831+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `-0.1237` n `8`; equity avg `0.0455` n `74`; fx avg `-0.0019` n `6`; index avg `0.0096` n `23`; metal avg `-0.0329` n `18`; unknown avg `-0.0264` n `515`
- 1h: commodity avg `-0.0519` n `12`; crypto_alt avg `0.0691` n `228`; crypto_major avg `0.1241` n `8`; equity avg `0.1579` n `74`; fx avg `-0.0166` n `6`; index avg `0.002` n `23`; metal avg `-0.0424` n `18`; unknown avg `-0.1172` n `515`
- 4h: commodity avg `0.2191` n `12`; crypto_alt avg `0.2075` n `228`; crypto_major avg `0.0802` n `8`; equity avg `0.2474` n `74`; fx avg `-0.0585` n `6`; index avg `0.1083` n `23`; metal avg `-0.0417` n `18`; unknown avg `4.1056` n `515`
- 24h: commodity avg `0.1297` n `12`; crypto_alt avg `-1.3917` n `228`; crypto_major avg `-1.5875` n `8`; equity avg `-0.6049` n `74`; fx avg `0.014` n `6`; index avg `0.0127` n `23`; metal avg `-0.5142` n `18`; unknown avg `0.9043` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
