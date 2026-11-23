# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T21:07:32.468320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4253` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0314` n `13`; crypto_alt avg `0.2828` n `239`; crypto_major avg `0.392` n `8`; equity avg `0.435` n `166`; fx avg `0.0048` n `6`; index avg `0.0528` n `27`; metal avg `0.0412` n `20`; unknown avg `1.1933` n `1230`
- 1h: commodity avg `0.0837` n `13`; crypto_alt avg `-0.2068` n `239`; crypto_major avg `0.0361` n `8`; equity avg `0.6654` n `166`; fx avg `0.0022` n `6`; index avg `0.0782` n `27`; metal avg `0.0124` n `20`; unknown avg `416.077` n `1236`
- 4h: commodity avg `-0.1682` n `13`; crypto_alt avg `-1.6654` n `239`; crypto_major avg `-1.4305` n `8`; equity avg `-0.2858` n `166`; fx avg `-0.003` n `6`; index avg `-0.0052` n `27`; metal avg `-0.2065` n `20`; unknown avg `400.6673` n `1230`
- 24h: commodity avg `-1.498` n `13`; crypto_alt avg `1.1156` n `239`; crypto_major avg `1.4195` n `8`; equity avg `6.0223` n `166`; fx avg `-0.077` n `6`; index avg `0.5949` n `27`; metal avg `0.6139` n `20`; unknown avg `537.9407` n `1056`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
