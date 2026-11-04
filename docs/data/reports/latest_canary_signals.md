# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T19:52:36.477719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2205` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0335` n `13`; crypto_alt avg `-0.4934` n `239`; crypto_major avg `-0.4784` n `8`; equity avg `-0.2016` n `158`; fx avg `0.0102` n `6`; index avg `-0.019` n `27`; metal avg `-0.0076` n `20`; unknown avg `0.1726` n `1264`
- 1h: commodity avg `0.039` n `13`; crypto_alt avg `-0.7055` n `239`; crypto_major avg `-0.6515` n `8`; equity avg `-0.1876` n `158`; fx avg `0.0079` n `6`; index avg `-0.023` n `27`; metal avg `-0.0184` n `20`; unknown avg `0.3694` n `1258`
- 4h: commodity avg `-1.0524` n `13`; crypto_alt avg `-1.8927` n `239`; crypto_major avg `-1.2014` n `8`; equity avg `-0.1623` n `158`; fx avg `-0.0148` n `6`; index avg `0.0191` n `27`; metal avg `0.1436` n `20`; unknown avg `-0.3854` n `1254`
- 24h: commodity avg `-1.7441` n `13`; crypto_alt avg `1.1321` n `239`; crypto_major avg `1.6013` n `8`; equity avg `-0.9269` n `158`; fx avg `0.0459` n `6`; index avg `0.1381` n `27`; metal avg `1.2373` n `20`; unknown avg `0.4818` n `1115`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2627`, n `668`, moderate_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1392`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1379`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
