# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-28T15:37:31.652221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.57` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.397` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0835` n `13`; crypto_alt avg `-0.2179` n `238`; crypto_major avg `-0.1843` n `8`; equity avg `-0.0786` n `155`; fx avg `0.0078` n `6`; index avg `-0.0066` n `27`; metal avg `-0.0203` n `20`; unknown avg `0.028` n `1238`
- 1h: commodity avg `0.0217` n `13`; crypto_alt avg `0.4535` n `238`; crypto_major avg `0.2297` n `8`; equity avg `0.3093` n `155`; fx avg `0.027` n `6`; index avg `0.0473` n `27`; metal avg `0.0092` n `20`; unknown avg `-0.2476` n `1232`
- 4h: commodity avg `0.1398` n `13`; crypto_alt avg `-1.231` n `238`; crypto_major avg `-1.3632` n `8`; equity avg `-0.5557` n `155`; fx avg `0.0941` n `6`; index avg `0.0338` n `27`; metal avg `-0.0742` n `20`; unknown avg `1.2544` n `1152`
- 24h: commodity avg `0.5501` n `13`; crypto_alt avg `0.0746` n `238`; crypto_major avg `0.0958` n `8`; equity avg `1.3484` n `154`; fx avg `0.2187` n `6`; index avg `0.2769` n `27`; metal avg `-0.1584` n `20`; unknown avg `2.6417` n `1100`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1469`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1462`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0658`, n `668`, weak_sample_signal
