# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T15:37:33.245491+00:00`
- Correlation status: `ready`
- Asset price records: `466`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `8.67` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `-3.2458` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-1.7903` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4688` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0749` n `12`; crypto_alt avg `-0.3199` n `228`; crypto_major avg `-0.2694` n `8`; equity avg `-0.1108` n `65`; fx avg `-0.0177` n `4`; index avg `-0.056` n `23`; metal avg `-0.0582` n `18`; unknown avg `-0.0223` n `356`
- 1h: commodity avg `-0.084` n `12`; crypto_alt avg `-0.1088` n `228`; crypto_major avg `-0.1772` n `8`; equity avg `0.2705` n `65`; fx avg `0.0049` n `4`; index avg `0.2324` n `23`; metal avg `0.0115` n `18`; unknown avg `0.0715` n `356`
- 4h: commodity avg `1.3188` n `7`; crypto_alt avg `-1.3946` n `223`; crypto_major avg `-1.927` n `7`; equity avg `-1.07` n `47`; fx avg `0.0732` n `4`; index avg `-0.4582` n `6`; metal avg `-0.1367` n `7`; unknown avg `8.4037` n `313`
- 24h: commodity avg `-2.429` n `7`; crypto_alt avg `2.5237` n `223`; crypto_major avg `0.5795` n `7`; equity avg `2.0` n `47`; fx avg `-0.4588` n `4`; index avg `1.869` n `6`; metal avg `2.782` n `7`; unknown avg `19.6164` n `311`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.2719`, n `462`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1951`, n `458`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1835`, n `458`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1835`, n `458`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1786`, n `462`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1769`, n `458`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.136`, n `462`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1252`, n `462`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1228`, n `462`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1145`, n `462`, weak_sample_signal
