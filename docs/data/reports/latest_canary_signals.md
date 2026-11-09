# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T06:37:24.160063+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4056` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0304` n `13`; crypto_alt avg `-0.1166` n `239`; crypto_major avg `-0.1398` n `8`; equity avg `-0.1344` n `158`; fx avg `-0.003` n `6`; index avg `-0.0023` n `27`; metal avg `-0.0859` n `20`; unknown avg `-0.1237` n `1261`
- 1h: commodity avg `-0.1544` n `13`; crypto_alt avg `-0.3497` n `239`; crypto_major avg `-0.4255` n `8`; equity avg `-0.4825` n `158`; fx avg `-0.0602` n `6`; index avg `-0.0638` n `27`; metal avg `-0.1451` n `20`; unknown avg `3.7748` n `1225`
- 4h: commodity avg `-0.1631` n `13`; crypto_alt avg `-1.3719` n `239`; crypto_major avg `-1.5592` n `8`; equity avg `-1.3189` n `158`; fx avg `-0.0718` n `6`; index avg `-0.1536` n `27`; metal avg `-0.2002` n `20`; unknown avg `4.5027` n `1206`
- 24h: commodity avg `-0.162` n `13`; crypto_alt avg `-2.4789` n `239`; crypto_major avg `-3.3282` n `8`; equity avg `-0.4702` n `158`; fx avg `-0.1713` n `6`; index avg `-0.0545` n `27`; metal avg `0.321` n `20`; unknown avg `1.5871` n `980`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.174`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1578`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1159`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
