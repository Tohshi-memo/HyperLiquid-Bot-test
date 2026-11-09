# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T19:37:29.491563+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0318` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1889` n `13`; crypto_alt avg `-0.002` n `239`; crypto_major avg `-0.0431` n `8`; equity avg `0.1315` n `160`; fx avg `-0.0138` n `6`; index avg `0.036` n `27`; metal avg `0.1007` n `20`; unknown avg `1.249` n `1261`
- 1h: commodity avg `-0.2394` n `13`; crypto_alt avg `0.0991` n `239`; crypto_major avg `0.0047` n `8`; equity avg `0.0312` n `160`; fx avg `-0.0148` n `6`; index avg `0.0252` n `27`; metal avg `0.1` n `20`; unknown avg `19.0491` n `1255`
- 4h: commodity avg `-0.1579` n `13`; crypto_alt avg `-0.7818` n `239`; crypto_major avg `-0.9489` n `8`; equity avg `0.2003` n `160`; fx avg `-0.0067` n `6`; index avg `0.0829` n `27`; metal avg `0.0258` n `20`; unknown avg `-0.1924` n `1249`
- 24h: commodity avg `-0.2935` n `13`; crypto_alt avg `0.3291` n `239`; crypto_major avg `-2.7017` n `8`; equity avg `3.3171` n `160`; fx avg `-0.152` n `6`; index avg `0.4387` n `27`; metal avg `0.4899` n `20`; unknown avg `5.2319` n `1074`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
