# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T19:07:33.689505+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `2.6523` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_commodity_crypto_divergence: score `-2.6001` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.4421` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `-2.1666` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0724` n `13`; crypto_alt avg `0.037` n `239`; crypto_major avg `0.2162` n `8`; equity avg `0.4001` n `166`; fx avg `0.0118` n `6`; index avg `0.0506` n `27`; metal avg `0.0447` n `20`; unknown avg `0.4456` n `1258`
- 1h: commodity avg `-0.1151` n `13`; crypto_alt avg `-0.2353` n `239`; crypto_major avg `-0.1426` n `8`; equity avg `-0.114` n `166`; fx avg `0.0144` n `6`; index avg `0.0052` n `27`; metal avg `-0.0306` n `20`; unknown avg `0.1148` n `1264`
- 4h: commodity avg `-0.0947` n `13`; crypto_alt avg `-1.9011` n `239`; crypto_major avg `-2.6948` n `8`; equity avg `-0.5282` n `166`; fx avg `-0.0819` n `6`; index avg `-0.0425` n `27`; metal avg `-0.2527` n `20`; unknown avg `126.4067` n `1258`
- 24h: commodity avg `-1.4131` n `13`; crypto_alt avg `2.2616` n `239`; crypto_major avg `2.3919` n `8`; equity avg `6.0646` n `166`; fx avg `-0.0814` n `6`; index avg `0.5624` n `27`; metal avg `0.6976` n `20`; unknown avg `334.8217` n `1066`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1298`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
