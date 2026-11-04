# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T11:37:31.019791+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0865` n `13`; crypto_alt avg `0.0324` n `239`; crypto_major avg `0.1655` n `8`; equity avg `-0.1589` n `158`; fx avg `0.0015` n `6`; index avg `0.0143` n `27`; metal avg `-0.0152` n `20`; unknown avg `-0.0107` n `1264`
- 1h: commodity avg `0.0045` n `13`; crypto_alt avg `0.375` n `239`; crypto_major avg `0.2625` n `8`; equity avg `-0.2682` n `158`; fx avg `0.0014` n `6`; index avg `0.0022` n `27`; metal avg `-0.0535` n `20`; unknown avg `1.0696` n `1258`
- 4h: commodity avg `-0.345` n `13`; crypto_alt avg `0.6019` n `239`; crypto_major avg `0.9119` n `8`; equity avg `1.2289` n `158`; fx avg `0.037` n `6`; index avg `0.2423` n `27`; metal avg `0.2161` n `20`; unknown avg `18.8143` n `1166`
- 24h: commodity avg `-0.7715` n `13`; crypto_alt avg `2.4906` n `239`; crypto_major avg `1.9793` n `8`; equity avg `2.7059` n `158`; fx avg `0.1417` n `6`; index avg `0.2846` n `27`; metal avg `1.1233` n `20`; unknown avg `18.0115` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2566`, n `670`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1694`, n `670`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1683`, n `670`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1626`, n `670`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1564`, n `670`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1508`, n `670`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1475`, n `670`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1471`, n `670`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1442`, n `670`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1426`, n `670`, weak_sample_signal
