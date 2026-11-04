# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T11:52:29.297661+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.022` n `13`; crypto_alt avg `-0.1234` n `239`; crypto_major avg `-0.1184` n `8`; equity avg `-0.1669` n `158`; fx avg `0.0201` n `6`; index avg `0.0047` n `27`; metal avg `-0.0077` n `20`; unknown avg `0.4452` n `1264`
- 1h: commodity avg `-0.0175` n `13`; crypto_alt avg `0.2509` n `239`; crypto_major avg `0.1438` n `8`; equity avg `-0.4351` n `158`; fx avg `0.0215` n `6`; index avg `0.0069` n `27`; metal avg `-0.0612` n `20`; unknown avg `1.4896` n `1258`
- 4h: commodity avg `-0.3103` n `13`; crypto_alt avg `0.4217` n `239`; crypto_major avg `0.8216` n `8`; equity avg `0.9491` n `158`; fx avg `0.0597` n `6`; index avg `0.2398` n `27`; metal avg `0.181` n `20`; unknown avg `18.8928` n `1166`
- 24h: commodity avg `-0.8201` n `13`; crypto_alt avg `2.0814` n `239`; crypto_major avg `1.7539` n `8`; equity avg `2.6131` n `158`; fx avg `0.1605` n `6`; index avg `0.3043` n `27`; metal avg `1.1022` n `20`; unknown avg `21.8257` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2551`, n `669`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1706`, n `669`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.169`, n `669`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.162`, n `669`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.157`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1503`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1492`, n `669`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1471`, n `669`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1416`, n `669`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1411`, n `669`, weak_sample_signal
