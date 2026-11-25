# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T21:37:33.342241+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1639` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `0.0809` n `239`; crypto_major avg `0.1994` n `8`; equity avg `-0.0713` n `168`; fx avg `0.0081` n `6`; index avg `0.0079` n `27`; metal avg `0.0372` n `20`; unknown avg `0.8371` n `1267`
- 1h: commodity avg `0.0725` n `13`; crypto_alt avg `0.4208` n `239`; crypto_major avg `0.6896` n `8`; equity avg `1.0741` n `168`; fx avg `-0.0115` n `6`; index avg `0.1192` n `27`; metal avg `0.0977` n `20`; unknown avg `1.9329` n `1221`
- 4h: commodity avg `-0.0259` n `13`; crypto_alt avg `1.6659` n `239`; crypto_major avg `2.138` n `8`; equity avg `3.0224` n `168`; fx avg `0.0129` n `6`; index avg `0.2721` n `27`; metal avg `0.7155` n `20`; unknown avg `177.8744` n `1215`
- 24h: commodity avg `0.4001` n `13`; crypto_alt avg `2.4919` n `239`; crypto_major avg `1.5004` n `8`; equity avg `-0.4083` n `168`; fx avg `0.0539` n `6`; index avg `-0.0525` n `27`; metal avg `0.1629` n `20`; unknown avg `216.4142` n `1069`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.172`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
