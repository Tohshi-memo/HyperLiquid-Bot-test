# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T20:07:41.502949+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2113` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0501` n `13`; crypto_alt avg `0.1424` n `239`; crypto_major avg `0.2289` n `8`; equity avg `0.0332` n `158`; fx avg `0.0138` n `6`; index avg `-0.0047` n `27`; metal avg `0.0679` n `20`; unknown avg `165.4764` n `1236`
- 1h: commodity avg `0.1368` n `13`; crypto_alt avg `-0.6234` n `239`; crypto_major avg `-0.3963` n `8`; equity avg `-0.3885` n `158`; fx avg `0.0255` n `6`; index avg `-0.0601` n `27`; metal avg `0.0367` n `20`; unknown avg `166.3374` n `1236`
- 4h: commodity avg `-0.6944` n `13`; crypto_alt avg `-1.4841` n `239`; crypto_major avg `-1.1522` n `8`; equity avg `0.3409` n `158`; fx avg `0.0024` n `6`; index avg `0.0591` n `27`; metal avg `0.1998` n `20`; unknown avg `1.809` n `1238`
- 24h: commodity avg `-1.7675` n `13`; crypto_alt avg `1.2983` n `239`; crypto_major avg `1.7723` n `8`; equity avg `-0.9035` n `158`; fx avg `0.0624` n `6`; index avg `0.1316` n `27`; metal avg `1.3488` n `20`; unknown avg `0.5206` n `1117`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2616`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1385`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
