# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T02:52:27.162249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.13` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `-1.8184` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.3792` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `-0.0211` n `239`; crypto_major avg `-0.0271` n `8`; equity avg `-0.1258` n `158`; fx avg `0.028` n `6`; index avg `-0.0245` n `27`; metal avg `-0.0881` n `20`; unknown avg `0.6713` n `1262`
- 1h: commodity avg `-0.1934` n `13`; crypto_alt avg `-0.2706` n `239`; crypto_major avg `-0.3069` n `8`; equity avg `-0.6612` n `158`; fx avg `0.0341` n `6`; index avg `-0.1571` n `27`; metal avg `-0.2153` n `20`; unknown avg `-0.1386` n `1258`
- 4h: commodity avg `-0.4786` n `13`; crypto_alt avg `-1.8671` n `239`; crypto_major avg `-2.0026` n `8`; equity avg `-3.2168` n `158`; fx avg `-0.0053` n `6`; index avg `-0.6234` n `27`; metal avg `-0.1842` n `20`; unknown avg `148.0828` n `1204`
- 24h: commodity avg `-0.1895` n `13`; crypto_alt avg `0.0097` n `239`; crypto_major avg `-0.4813` n `8`; equity avg `-1.1359` n `158`; fx avg `0.1394` n `6`; index avg `-0.4116` n `27`; metal avg `-0.5825` n `20`; unknown avg `-0.3029` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
