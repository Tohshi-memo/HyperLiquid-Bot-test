# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T19:09:44.731523+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.419` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.645` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0834` n `13`; crypto_alt avg `0.4073` n `239`; crypto_major avg `0.3433` n `8`; equity avg `0.5024` n `168`; fx avg `-0.0075` n `6`; index avg `0.0171` n `27`; metal avg `0.102` n `20`; unknown avg `0.6014` n `1257`
- 1h: commodity avg `-0.0875` n `13`; crypto_alt avg `0.6758` n `239`; crypto_major avg `0.6165` n `8`; equity avg `2.0664` n `168`; fx avg `0.0146` n `6`; index avg `0.1895` n `27`; metal avg `0.2965` n `20`; unknown avg `201.2801` n `1261`
- 4h: commodity avg `0.0724` n `13`; crypto_alt avg `3.4769` n `239`; crypto_major avg `3.4914` n `8`; equity avg `4.3778` n `168`; fx avg `0.091` n `6`; index avg `0.4255` n `27`; metal avg `0.8464` n `20`; unknown avg `192.3376` n `1253`
- 24h: commodity avg `0.2848` n `13`; crypto_alt avg `1.4584` n `239`; crypto_major avg `0.6401` n `8`; equity avg `-0.4913` n `168`; fx avg `0.0153` n `6`; index avg `-0.0661` n `27`; metal avg `-0.001` n `20`; unknown avg `205.6126` n `1083`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
