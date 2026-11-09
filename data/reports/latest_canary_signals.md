# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T08:07:29.408734+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7074` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.6609` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0415` n `13`; crypto_alt avg `-0.0266` n `239`; crypto_major avg `-0.1181` n `8`; equity avg `0.2838` n `158`; fx avg `0.0043` n `6`; index avg `0.0247` n `27`; metal avg `0.0663` n `20`; unknown avg `1.6077` n `1199`
- 1h: commodity avg `-0.1` n `13`; crypto_alt avg `-0.5446` n `239`; crypto_major avg `-0.4415` n `8`; equity avg `-0.4766` n `158`; fx avg `0.03` n `6`; index avg `-0.0712` n `27`; metal avg `-0.081` n `20`; unknown avg `1.2802` n `1175`
- 4h: commodity avg `-0.396` n `13`; crypto_alt avg `-1.8661` n `239`; crypto_major avg `-1.9439` n `8`; equity avg `-1.7605` n `158`; fx avg `-0.0581` n `6`; index avg `-0.2365` n `27`; metal avg `-0.283` n `20`; unknown avg `1.8495` n `1151`
- 24h: commodity avg `-0.2413` n `13`; crypto_alt avg `-3.4702` n `239`; crypto_major avg `-4.2522` n `8`; equity avg `-1.3574` n `158`; fx avg `-0.1521` n `6`; index avg `-0.1865` n `27`; metal avg `0.179` n `20`; unknown avg `0.9521` n `954`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
