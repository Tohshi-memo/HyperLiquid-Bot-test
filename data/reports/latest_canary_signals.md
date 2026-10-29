# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T20:07:32.886718+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.7322` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.4649` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.2544` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.024` n `13`; crypto_alt avg `-1.2963` n `238`; crypto_major avg `-0.9881` n `8`; equity avg `-1.696` n `156`; fx avg `0.0021` n `6`; index avg `-0.1844` n `27`; metal avg `0.0036` n `20`; unknown avg `3.8052` n `1210`
- 1h: commodity avg `0.1426` n `13`; crypto_alt avg `-1.1267` n `238`; crypto_major avg `-0.9578` n `8`; equity avg `-1.3423` n `156`; fx avg `0.0095` n `6`; index avg `-0.1294` n `27`; metal avg `0.0659` n `20`; unknown avg `3.8077` n `1210`
- 4h: commodity avg `0.2608` n `13`; crypto_alt avg `-3.3716` n `238`; crypto_major avg `-2.4714` n `8`; equity avg `-2.5358` n `156`; fx avg `-0.0108` n `6`; index avg `-0.217` n `27`; metal avg `-0.0065` n `20`; unknown avg `16.9344` n `1212`
- 24h: commodity avg `-0.0725` n `13`; crypto_alt avg `-3.3585` n `238`; crypto_major avg `-0.6552` n `8`; equity avg `-3.5636` n `155`; fx avg `0.0274` n `6`; index avg `-0.4258` n `27`; metal avg `-0.664` n `20`; unknown avg `17.0782` n `958`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
