# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T16:37:38.177632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.0618` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.6904` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0008` n `13`; crypto_alt avg `-0.1447` n `239`; crypto_major avg `-0.3886` n `8`; equity avg `-0.2228` n `168`; fx avg `-0.0074` n `6`; index avg `-0.0245` n `27`; metal avg `-0.0373` n `20`; unknown avg `158.1374` n `1265`
- 1h: commodity avg `0.0577` n `13`; crypto_alt avg `-0.5103` n `239`; crypto_major avg `-0.7231` n `8`; equity avg `-1.1373` n `168`; fx avg `0.0204` n `6`; index avg `-0.1015` n `27`; metal avg `-0.2685` n `20`; unknown avg `159.2932` n `1257`
- 4h: commodity avg `0.1994` n `13`; crypto_alt avg `-1.5893` n `239`; crypto_major avg `-1.8624` n `8`; equity avg `-2.4973` n `168`; fx avg `0.0643` n `6`; index avg `-0.172` n `27`; metal avg `-0.7125` n `20`; unknown avg `160.5254` n `1243`
- 24h: commodity avg `0.4683` n `13`; crypto_alt avg `-5.4139` n `239`; crypto_major avg `-5.4028` n `8`; equity avg `-5.1119` n `167`; fx avg `0.2404` n `6`; index avg `-0.396` n `27`; metal avg `-1.3696` n `20`; unknown avg `6.3731` n `1133`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
