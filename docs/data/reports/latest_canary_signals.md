# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T16:07:37.899918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6744` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.1483` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0348` n `12`; crypto_alt avg `0.0094` n `230`; crypto_major avg `-0.0983` n `8`; equity avg `0.3197` n `102`; fx avg `-0.0037` n `6`; index avg `0.0467` n `25`; metal avg `0.0488` n `20`; unknown avg `-0.1323` n `774`
- 1h: commodity avg `0.0443` n `12`; crypto_alt avg `-0.0508` n `230`; crypto_major avg `-0.1018` n `8`; equity avg `-0.1183` n `102`; fx avg `-0.0104` n `6`; index avg `-0.088` n `25`; metal avg `0.0598` n `20`; unknown avg `-0.2858` n `774`
- 4h: commodity avg `-0.0362` n `12`; crypto_alt avg `-1.8429` n `230`; crypto_major avg `-1.7137` n `8`; equity avg `-2.7521` n `102`; fx avg `-0.0661` n `6`; index avg `-0.5654` n `25`; metal avg `-0.0393` n `20`; unknown avg `-0.1093` n `774`
- 24h: commodity avg `-0.5406` n `12`; crypto_alt avg `-1.4953` n `230`; crypto_major avg `-0.8467` n `8`; equity avg `-1.8605` n `102`; fx avg `0.0229` n `6`; index avg `-0.472` n `25`; metal avg `0.2791` n `20`; unknown avg `-0.3771` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1986`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1125`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
