# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T00:52:28.166953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-2.2059` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.8211` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0281` n `13`; crypto_alt avg `0.4649` n `239`; crypto_major avg `0.2905` n `8`; equity avg `0.3011` n `158`; fx avg `0.0023` n `6`; index avg `0.0657` n `27`; metal avg `0.1161` n `20`; unknown avg `0.3017` n `1262`
- 1h: commodity avg `-0.0005` n `13`; crypto_alt avg `1.1021` n `239`; crypto_major avg `0.7457` n `8`; equity avg `0.3654` n `158`; fx avg `-0.0268` n `6`; index avg `0.0949` n `27`; metal avg `0.3661` n `20`; unknown avg `3.1167` n `1250`
- 4h: commodity avg `0.0186` n `13`; crypto_alt avg `-0.913` n `239`; crypto_major avg `-1.8365` n `8`; equity avg `-0.4519` n `158`; fx avg `-0.0584` n `6`; index avg `-0.0154` n `27`; metal avg `0.3694` n `20`; unknown avg `0.962` n `1194`
- 24h: commodity avg `-0.0087` n `13`; crypto_alt avg `-2.2719` n `239`; crypto_major avg `-2.1669` n `8`; equity avg `-0.5253` n `158`; fx avg `-0.0251` n `6`; index avg `-0.0816` n `27`; metal avg `0.3413` n `20`; unknown avg `0.072` n `1000`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
