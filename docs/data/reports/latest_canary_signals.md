# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T18:07:25.157961+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.4804` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.7525` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.5812` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0203` n `13`; crypto_alt avg `0.1554` n `239`; crypto_major avg `-0.0123` n `8`; equity avg `0.0059` n `160`; fx avg `0.0093` n `6`; index avg `0.0104` n `27`; metal avg `-0.007` n `20`; unknown avg `-0.1134` n `1258`
- 1h: commodity avg `-0.0298` n `13`; crypto_alt avg `0.7869` n `239`; crypto_major avg `0.4085` n `8`; equity avg `-0.0009` n `160`; fx avg `0.0196` n `6`; index avg `-0.0004` n `27`; metal avg `-0.0188` n `20`; unknown avg `18.8903` n `1256`
- 4h: commodity avg `0.6425` n `13`; crypto_alt avg `-1.2774` n `239`; crypto_major avg `-1.8379` n `8`; equity avg `-0.5633` n `160`; fx avg `-0.0751` n `6`; index avg `-0.0854` n `27`; metal avg `-0.2567` n `20`; unknown avg `18.3957` n `1250`
- 24h: commodity avg `-0.2668` n `13`; crypto_alt avg `-1.9297` n `239`; crypto_major avg `-3.4209` n `8`; equity avg `-2.0663` n `160`; fx avg `-0.1041` n `6`; index avg `-0.2135` n `27`; metal avg `-0.489` n `20`; unknown avg `0.2216` n `1159`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2455`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
