# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T16:07:33.797928+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0959` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9713` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0065` n `13`; crypto_alt avg `-0.2604` n `239`; crypto_major avg `-0.1431` n `8`; equity avg `0.0457` n `166`; fx avg `-0.0147` n `6`; index avg `0.0088` n `27`; metal avg `-0.0041` n `20`; unknown avg `0.2424` n `1248`
- 1h: commodity avg `-0.0369` n `13`; crypto_alt avg `-0.5396` n `239`; crypto_major avg `-0.679` n `8`; equity avg `-0.0696` n `166`; fx avg `-0.0045` n `6`; index avg `-0.0037` n `27`; metal avg `-0.0343` n `20`; unknown avg `0.689` n `1244`
- 4h: commodity avg `0.0043` n `13`; crypto_alt avg `2.0423` n `239`; crypto_major avg `2.1002` n `8`; equity avg `0.8841` n `166`; fx avg `0.0036` n `6`; index avg `0.0981` n `27`; metal avg `0.1289` n `20`; unknown avg `160.95` n `1244`
- 24h: commodity avg `0.5316` n `13`; crypto_alt avg `0.7114` n `239`; crypto_major avg `0.5239` n `8`; equity avg `-1.1148` n `166`; fx avg `-0.1055` n `6`; index avg `-0.1756` n `27`; metal avg `-0.0193` n `20`; unknown avg `175.3223` n `1141`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
