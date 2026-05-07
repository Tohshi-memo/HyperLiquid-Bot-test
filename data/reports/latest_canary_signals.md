# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T21:37:15.472600+00:00`
- Correlation status: `ready`
- Asset price records: `586`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.2006` n `12`; crypto_alt avg `0.3043` n `228`; crypto_major avg `0.1414` n `8`; equity avg `-0.2469` n `65`; fx avg `-0.0088` n `5`; index avg `-0.0997` n `23`; metal avg `-0.0133` n `18`; unknown avg `-0.1906` n `365`
- 1h: commodity avg `0.4539` n `12`; crypto_alt avg `-0.0349` n `228`; crypto_major avg `0.0667` n `8`; equity avg `-0.4444` n `65`; fx avg `-0.0321` n `5`; index avg `-0.1709` n `23`; metal avg `-0.5023` n `18`; unknown avg `-0.3067` n `365`
- 4h: commodity avg `0.6376` n `12`; crypto_alt avg `0.7031` n `228`; crypto_major avg `0.1199` n `8`; equity avg `-0.402` n `65`; fx avg `-0.0384` n `5`; index avg `-0.1716` n `23`; metal avg `-0.6603` n `18`; unknown avg `-0.6227` n `365`
- 24h: commodity avg `1.0157` n `12`; crypto_alt avg `0.7874` n `228`; crypto_major avg `-1.9903` n `8`; equity avg `-1.2896` n `65`; fx avg `0.1626` n `5`; index avg `-0.9194` n `23`; metal avg `-0.4211` n `18`; unknown avg `-0.5583` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `582`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1123`, n `582`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1119`, n `582`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1028`, n `582`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.095`, n `578`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `578`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0854`, n `578`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0845`, n `578`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0844`, n `578`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0804`, n `578`, weak_sample_signal
