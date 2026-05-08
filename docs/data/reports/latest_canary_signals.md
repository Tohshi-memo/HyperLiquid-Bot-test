# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T01:28:11.112604+00:00`
- Correlation status: `ready`
- Asset price records: `601`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.15` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1496` n `12`; crypto_alt avg `-0.1425` n `228`; crypto_major avg `-0.0702` n `8`; equity avg `0.1226` n `65`; fx avg `-0.011` n `5`; index avg `0.031` n `23`; metal avg `0.0355` n `18`; unknown avg `0.1873` n `365`
- 1h: commodity avg `-0.4245` n `12`; crypto_alt avg `-0.3744` n `228`; crypto_major avg `-0.3877` n `8`; equity avg `0.3429` n `65`; fx avg `0.0046` n `5`; index avg `0.1646` n `23`; metal avg `0.6279` n `18`; unknown avg `0.2743` n `365`
- 4h: commodity avg `-0.9575` n `12`; crypto_alt avg `0.3288` n `228`; crypto_major avg `-0.2305` n `8`; equity avg `0.4919` n `65`; fx avg `0.0825` n `5`; index avg `0.3657` n `23`; metal avg `0.9336` n `18`; unknown avg `-0.1335` n `365`
- 24h: commodity avg `0.4269` n `12`; crypto_alt avg `2.233` n `228`; crypto_major avg `-1.3555` n `8`; equity avg `-0.5035` n `65`; fx avg `0.1861` n `5`; index avg `-0.4882` n `23`; metal avg `0.0949` n `18`; unknown avg `-0.1679` n `354`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1351`, n `597`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `597`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1116`, n `597`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1063`, n `593`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `597`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1045`, n `593`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.092`, n `593`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0904`, n `593`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0801`, n `593`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0717`, n `597`, weak_sample_signal
