# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T15:40:06.454557+00:00`
- Correlation status: `ready`
- Asset price records: `466`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `8.67` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-3.2552` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7551` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4564` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0585` n `12`; crypto_alt avg `-0.3073` n `228`; crypto_major avg `-0.2593` n `8`; equity avg `-0.1251` n `65`; fx avg `-0.0185` n `4`; index avg `-0.0637` n `23`; metal avg `-0.0812` n `18`; unknown avg `-0.0015` n `356`
- 1h: commodity avg `-0.0678` n `12`; crypto_alt avg `-0.0963` n `228`; crypto_major avg `-0.1672` n `8`; equity avg `0.2564` n `65`; fx avg `0.0041` n `4`; index avg `0.2248` n `23`; metal avg `-0.0114` n `18`; unknown avg `0.0923` n `356`
- 4h: commodity avg `1.3394` n `7`; crypto_alt avg `-1.3814` n `223`; crypto_major avg `-1.9158` n `7`; equity avg `-1.0831` n `47`; fx avg `0.0724` n `4`; index avg `-0.4594` n `6`; metal avg `-0.1607` n `7`; unknown avg `8.2919` n `313`
- 24h: commodity avg `-2.4112` n `7`; crypto_alt avg `2.5384` n `223`; crypto_major avg `0.591` n `7`; equity avg `1.9865` n `47`; fx avg `-0.4596` n `4`; index avg `1.8677` n `6`; metal avg `2.7571` n `7`; unknown avg `19.3501` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2728`, n `462`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1938`, n `458`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1823`, n `458`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.182`, n `458`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1798`, n `462`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1756`, n `458`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.136`, n `462`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1234`, n `462`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1227`, n `462`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1152`, n `462`, weak_sample_signal
