# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T13:37:27.744406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0365` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1175` n `13`; crypto_alt avg `0.0212` n `239`; crypto_major avg `-0.1045` n `8`; equity avg `-0.0951` n `158`; fx avg `-0.0013` n `6`; index avg `-0.0052` n `27`; metal avg `0.0599` n `20`; unknown avg `-0.1723` n `1256`
- 1h: commodity avg `0.0309` n `13`; crypto_alt avg `0.1818` n `239`; crypto_major avg `-0.1863` n `8`; equity avg `-0.2283` n `158`; fx avg `-0.0015` n `6`; index avg `0.0029` n `27`; metal avg `0.1218` n `20`; unknown avg `-0.066` n `1253`
- 4h: commodity avg `0.331` n `13`; crypto_alt avg `-1.1781` n `239`; crypto_major avg `-1.0974` n `8`; equity avg `-1.1199` n `158`; fx avg `0.0307` n `6`; index avg `-0.0609` n `27`; metal avg `0.097` n `20`; unknown avg `183.0906` n `1217`
- 24h: commodity avg `-0.8605` n `13`; crypto_alt avg `0.2395` n `239`; crypto_major avg `1.0952` n `8`; equity avg `-2.8306` n `158`; fx avg `-0.0282` n `6`; index avg `-0.2582` n `27`; metal avg `0.7788` n `20`; unknown avg `208.8665` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2377`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2001`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1911`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1431`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
