# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T05:07:36.514615+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-3.4381` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `-3.1879` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `3.1674` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.7785` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0641` n `13`; crypto_alt avg `-0.2186` n `239`; crypto_major avg `-0.216` n `8`; equity avg `-0.3243` n `162`; fx avg `-0.0105` n `6`; index avg `-0.0297` n `27`; metal avg `-0.0073` n `20`; unknown avg `-0.0554` n `1256`
- 1h: commodity avg `-0.0734` n `13`; crypto_alt avg `-0.6223` n `239`; crypto_major avg `-0.5953` n `8`; equity avg `-0.0682` n `162`; fx avg `-0.0042` n `6`; index avg `0.0105` n `27`; metal avg `-0.0631` n `20`; unknown avg `7.5117` n `1254`
- 4h: commodity avg `-0.1155` n `13`; crypto_alt avg `-3.0024` n `239`; crypto_major avg `-3.3034` n `8`; equity avg `-1.5249` n `162`; fx avg `0.0042` n `6`; index avg `-0.136` n `27`; metal avg `0.1347` n `20`; unknown avg `1.1854` n `1242`
- 24h: commodity avg `0.8317` n `13`; crypto_alt avg `-3.3915` n `239`; crypto_major avg `-4.6747` n `8`; equity avg `-1.2287` n `162`; fx avg `0.0019` n `6`; index avg `0.0099` n `27`; metal avg `-0.4374` n `20`; unknown avg `99.5391` n `1123`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1839`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
