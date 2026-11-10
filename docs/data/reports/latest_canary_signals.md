# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T18:37:33.578628+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1275` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0072` n `13`; crypto_alt avg `0.474` n `239`; crypto_major avg `0.6321` n `8`; equity avg `0.3324` n `160`; fx avg `-0.0013` n `6`; index avg `0.0324` n `27`; metal avg `0.0529` n `20`; unknown avg `0.3717` n `1262`
- 1h: commodity avg `0.0538` n `13`; crypto_alt avg `1.0081` n `239`; crypto_major avg `1.0678` n `8`; equity avg `0.5112` n `160`; fx avg `0.013` n `6`; index avg `0.0516` n `27`; metal avg `0.1246` n `20`; unknown avg `0.3933` n `1256`
- 4h: commodity avg `0.6052` n `13`; crypto_alt avg `-1.1121` n `239`; crypto_major avg `-1.2331` n `8`; equity avg `-0.8925` n `160`; fx avg `-0.066` n `6`; index avg `-0.1056` n `27`; metal avg `-0.113` n `20`; unknown avg `-0.8093` n `1250`
- 24h: commodity avg `-0.3515` n `13`; crypto_alt avg `-1.2787` n `239`; crypto_major avg `-2.5675` n `8`; equity avg `-1.8384` n `160`; fx avg `-0.1054` n `6`; index avg `-0.2025` n `27`; metal avg `-0.4512` n `20`; unknown avg `0.162` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2458`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1204`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
