# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T06:22:37.109357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.182` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0982` n `13`; crypto_alt avg `-0.276` n `239`; crypto_major avg `-0.3279` n `8`; equity avg `-0.2305` n `158`; fx avg `-0.0333` n `6`; index avg `-0.0371` n `27`; metal avg `-0.0205` n `20`; unknown avg `2.7698` n `1263`
- 1h: commodity avg `-0.1529` n `13`; crypto_alt avg `-0.3584` n `239`; crypto_major avg `-0.5386` n `8`; equity avg `-0.4988` n `158`; fx avg `-0.0573` n `6`; index avg `-0.0896` n `27`; metal avg `-0.0732` n `20`; unknown avg `2.7747` n `1225`
- 4h: commodity avg `-0.0965` n `13`; crypto_alt avg `-1.0044` n `239`; crypto_major avg `-1.3269` n `8`; equity avg `-1.1097` n `158`; fx avg `-0.0903` n `6`; index avg `-0.1449` n `27`; metal avg `-0.1183` n `20`; unknown avg `3.447` n `1208`
- 24h: commodity avg `-0.0908` n `13`; crypto_alt avg `-2.5568` n `239`; crypto_major avg `-3.2677` n `8`; equity avg `-0.3647` n `158`; fx avg `-0.169` n `6`; index avg `-0.0583` n `27`; metal avg `0.4198` n `20`; unknown avg `1.8082` n `980`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
