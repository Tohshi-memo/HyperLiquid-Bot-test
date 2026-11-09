# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T01:37:31.647490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.3894` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.0285` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7092` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0219` n `13`; crypto_alt avg `0.0271` n `239`; crypto_major avg `-0.0393` n `8`; equity avg `0.3933` n `158`; fx avg `0.0118` n `6`; index avg `0.0438` n `27`; metal avg `0.0113` n `20`; unknown avg `0.337` n `1258`
- 1h: commodity avg `-0.0351` n `13`; crypto_alt avg `0.3022` n `239`; crypto_major avg `-0.1282` n `8`; equity avg `0.4593` n `158`; fx avg `0.0307` n `6`; index avg `0.1324` n `27`; metal avg `0.175` n `20`; unknown avg `1.3679` n `1250`
- 4h: commodity avg `-0.138` n `13`; crypto_alt avg `-0.797` n `239`; crypto_major avg `-1.9612` n `8`; equity avg `-0.252` n `158`; fx avg `-0.0279` n `6`; index avg `0.0673` n `27`; metal avg `0.4282` n `20`; unknown avg `1.9845` n `1204`
- 24h: commodity avg `-0.0854` n `13`; crypto_alt avg `-2.1361` n `239`; crypto_major avg `-2.5633` n `8`; equity avg `-0.3209` n `158`; fx avg `-0.0025` n `6`; index avg `-0.0113` n `27`; metal avg `0.3979` n `20`; unknown avg `1.6329` n `996`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1763`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
