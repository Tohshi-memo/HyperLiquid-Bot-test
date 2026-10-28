# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T14:22:32.065742+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.58` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.7437` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-1.7293` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.1278` n `13`; crypto_alt avg `-0.4615` n `238`; crypto_major avg `-0.3923` n `8`; equity avg `-0.1283` n `155`; fx avg `-0.0034` n `6`; index avg `-0.019` n `27`; metal avg `-0.0333` n `20`; unknown avg `0.3733` n `1194`
- 1h: commodity avg `0.1536` n `13`; crypto_alt avg `-0.6216` n `238`; crypto_major avg `-0.5311` n `8`; equity avg `-0.2357` n `155`; fx avg `0.0397` n `6`; index avg `-0.0111` n `27`; metal avg `-0.1049` n `20`; unknown avg `1.6264` n `1154`
- 4h: commodity avg `0.2477` n `13`; crypto_alt avg `-1.7052` n `238`; crypto_major avg `-1.7243` n `8`; equity avg `-0.8127` n `155`; fx avg `0.0797` n `6`; index avg `0.0194` n `27`; metal avg `0.005` n `20`; unknown avg `2.556` n `1150`
- 24h: commodity avg `0.4503` n `13`; crypto_alt avg `0.3786` n `238`; crypto_major avg `0.5534` n `8`; equity avg `1.8812` n `154`; fx avg `0.1452` n `6`; index avg `0.426` n `27`; metal avg `-0.0038` n `20`; unknown avg `8.6774` n `1066`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1663`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
