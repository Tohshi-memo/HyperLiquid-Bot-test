# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T18:22:32.456205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7071` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.5351` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `0.1582` n `239`; crypto_major avg `-0.0071` n `8`; equity avg `0.484` n `168`; fx avg `0.0063` n `6`; index avg `0.0523` n `27`; metal avg `-0.0085` n `20`; unknown avg `0.2193` n `1265`
- 1h: commodity avg `-0.0214` n `13`; crypto_alt avg `0.7854` n `239`; crypto_major avg `1.0002` n `8`; equity avg `1.7117` n `168`; fx avg `0.0032` n `6`; index avg `0.1799` n `27`; metal avg `0.2168` n `20`; unknown avg `1.1293` n `1262`
- 4h: commodity avg `0.308` n `13`; crypto_alt avg `3.0959` n `239`; crypto_major avg `3.0151` n `8`; equity avg `2.4384` n `168`; fx avg `0.0677` n `6`; index avg `0.2833` n `27`; metal avg `0.48` n `20`; unknown avg `274.1381` n `1247`
- 24h: commodity avg `0.4148` n `13`; crypto_alt avg `0.7355` n `239`; crypto_major avg `-0.2778` n `8`; equity avg `-2.0585` n `168`; fx avg `0.0068` n `6`; index avg `-0.2142` n `27`; metal avg `-0.2969` n `20`; unknown avg `448.2983` n `1077`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
