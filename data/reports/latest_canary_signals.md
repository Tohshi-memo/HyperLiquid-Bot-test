# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T16:37:43.299373+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.1684` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `2.8846` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_metal_divergence: score `-2.8449` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0944` n `13`; crypto_alt avg `0.231` n `239`; crypto_major avg `0.3057` n `8`; equity avg `-0.7295` n `166`; fx avg `-0.0041` n `6`; index avg `-0.0788` n `27`; metal avg `-0.0125` n `20`; unknown avg `159.0259` n `1261`
- 1h: commodity avg `0.2559` n `13`; crypto_alt avg `0.2238` n `239`; crypto_major avg `0.0419` n `8`; equity avg `-0.8398` n `166`; fx avg `0.0065` n `6`; index avg `-0.1287` n `27`; metal avg `-0.1249` n `20`; unknown avg `0.3001` n `1247`
- 4h: commodity avg `0.0429` n `13`; crypto_alt avg `-2.8949` n `239`; crypto_major avg `-3.1255` n `8`; equity avg `-2.6616` n `166`; fx avg `-0.0135` n `6`; index avg `-0.2409` n `27`; metal avg `-0.2806` n `20`; unknown avg `0.6616` n `1245`
- 24h: commodity avg `-0.3181` n `13`; crypto_alt avg `-5.8211` n `239`; crypto_major avg `-6.055` n `8`; equity avg `-9.8416` n `166`; fx avg `-0.0354` n `6`; index avg `-0.8936` n `27`; metal avg `-1.2326` n `20`; unknown avg `45.0503` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1677`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1533`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
