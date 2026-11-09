# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T06:52:23.760019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1702` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.099` n `13`; crypto_alt avg `0.1441` n `239`; crypto_major avg `0.0692` n `8`; equity avg `-0.062` n `158`; fx avg `0.0071` n `6`; index avg `-0.0033` n `27`; metal avg `0.0046` n `20`; unknown avg `0.1122` n `1263`
- 1h: commodity avg `-0.2335` n `13`; crypto_alt avg `-0.3088` n `239`; crypto_major avg `-0.3004` n `8`; equity avg `-0.2319` n `158`; fx avg `-0.0535` n `6`; index avg `-0.0167` n `27`; metal avg `-0.1466` n `20`; unknown avg `3.7931` n `1227`
- 4h: commodity avg `-0.3252` n `13`; crypto_alt avg `-1.0864` n `239`; crypto_major avg `-1.3204` n `8`; equity avg `-1.3244` n `158`; fx avg `-0.0583` n `6`; index avg `-0.1502` n `27`; metal avg `-0.1761` n `20`; unknown avg `4.5474` n `1208`
- 24h: commodity avg `-0.2657` n `13`; crypto_alt avg `-2.2695` n `239`; crypto_major avg `-3.2337` n `8`; equity avg `-0.5766` n `158`; fx avg `-0.1642` n `6`; index avg `-0.0637` n `27`; metal avg `0.3329` n `20`; unknown avg `1.5474` n `982`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1584`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
