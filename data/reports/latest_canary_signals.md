# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T18:22:30.696502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0369` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3274` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.055` n `13`; crypto_alt avg `0.0307` n `239`; crypto_major avg `0.0764` n `8`; equity avg `-0.0888` n `160`; fx avg `0.0022` n `6`; index avg `-0.013` n `27`; metal avg `0.0175` n `20`; unknown avg `-0.1585` n `1262`
- 1h: commodity avg `0.0699` n `13`; crypto_alt avg `0.2573` n `239`; crypto_major avg `0.0678` n `8`; equity avg `-0.2293` n `160`; fx avg `0.023` n `6`; index avg `-0.0286` n `27`; metal avg `0.023` n `20`; unknown avg `18.5586` n `1256`
- 4h: commodity avg `0.6133` n `13`; crypto_alt avg `-1.1182` n `239`; crypto_major avg `-1.4236` n `8`; equity avg `-0.5206` n `160`; fx avg `-0.0799` n `6`; index avg `-0.0962` n `27`; metal avg `-0.2492` n `20`; unknown avg `-0.6985` n `1250`
- 24h: commodity avg `-0.3207` n `13`; crypto_alt avg `-1.9048` n `239`; crypto_major avg `-3.3488` n `8`; equity avg `-2.154` n `160`; fx avg `-0.1019` n `6`; index avg `-0.2263` n `27`; metal avg `-0.4717` n `20`; unknown avg `0.2209` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2459`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1758`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
