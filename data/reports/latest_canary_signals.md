# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T02:22:23.805037+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0948` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0528` n `13`; crypto_alt avg `-0.2655` n `239`; crypto_major avg `-0.4504` n `8`; equity avg `0.0139` n `166`; fx avg `-0.0158` n `6`; index avg `0.0281` n `27`; metal avg `0.0437` n `20`; unknown avg `0.6134` n `1262`
- 1h: commodity avg `-0.0555` n `13`; crypto_alt avg `-0.7084` n `239`; crypto_major avg `-1.1858` n `8`; equity avg `-1.1636` n `166`; fx avg `-0.0292` n `6`; index avg `-0.091` n `27`; metal avg `-0.1671` n `20`; unknown avg `159.7076` n `1262`
- 4h: commodity avg `-0.0844` n `13`; crypto_alt avg `0.2893` n `239`; crypto_major avg `-0.6482` n `8`; equity avg `-0.4103` n `166`; fx avg `0.0575` n `6`; index avg `0.0713` n `27`; metal avg `0.0158` n `20`; unknown avg `2.4549` n `1250`
- 24h: commodity avg `-1.1878` n `13`; crypto_alt avg `1.4939` n `239`; crypto_major avg `1.1217` n `8`; equity avg `5.8058` n `166`; fx avg `-0.2247` n `6`; index avg `0.6733` n `27`; metal avg `0.5526` n `20`; unknown avg `2.5092` n `1047`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
