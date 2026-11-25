# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T21:22:27.694932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2973` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6188` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0287` n `13`; crypto_alt avg `-0.0842` n `239`; crypto_major avg `-0.1033` n `8`; equity avg `0.0857` n `168`; fx avg `-0.0044` n `6`; index avg `-0.0036` n `27`; metal avg `-0.0587` n `20`; unknown avg `11.8405` n `1263`
- 1h: commodity avg `0.044` n `13`; crypto_alt avg `0.0058` n `239`; crypto_major avg `0.1743` n `8`; equity avg `0.3454` n `168`; fx avg `-0.0236` n `6`; index avg `0.0319` n `27`; metal avg `-0.0296` n `20`; unknown avg `189.3567` n `1221`
- 4h: commodity avg `-0.0492` n `13`; crypto_alt avg `1.7845` n `239`; crypto_major avg `2.2481` n `8`; equity avg `3.4631` n `168`; fx avg `-0.0025` n `6`; index avg `0.3134` n `27`; metal avg `0.6293` n `20`; unknown avg `2.6146` n `1214`
- 24h: commodity avg `0.4008` n `13`; crypto_alt avg `2.2357` n `239`; crypto_major avg `1.2609` n `8`; equity avg `-0.4315` n `168`; fx avg `0.0408` n `6`; index avg `-0.0723` n `27`; metal avg `0.1136` n `20`; unknown avg `27.4287` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1709`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1021`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
