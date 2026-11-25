# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T14:52:33.538548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.2411` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.4864` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1148` n `13`; crypto_alt avg `0.0045` n `239`; crypto_major avg `-0.1563` n `8`; equity avg `-0.2599` n `168`; fx avg `-0.0124` n `6`; index avg `-0.0429` n `27`; metal avg `-0.1171` n `20`; unknown avg `160.7882` n `1265`
- 1h: commodity avg `0.1266` n `13`; crypto_alt avg `-0.6462` n `239`; crypto_major avg `-0.6751` n `8`; equity avg `-1.3943` n `168`; fx avg `-0.0037` n `6`; index avg `-0.1384` n `27`; metal avg `-0.2825` n `20`; unknown avg `160.9897` n `1249`
- 4h: commodity avg `0.491` n `13`; crypto_alt avg `-1.7832` n `239`; crypto_major avg `-1.7501` n `8`; equity avg `-2.3825` n `168`; fx avg `-0.0013` n `6`; index avg `-0.2637` n `27`; metal avg `-0.585` n `20`; unknown avg `282.6162` n `1177`
- 24h: commodity avg `0.3208` n `13`; crypto_alt avg `-3.5034` n `239`; crypto_major avg `-4.509` n `8`; equity avg `-7.0635` n `168`; fx avg `-0.0607` n `6`; index avg `-0.7106` n `27`; metal avg `-1.6553` n `20`; unknown avg `631.6156` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0978`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
