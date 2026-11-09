# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T15:22:30.375957+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-2.2542` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_equity_divergence: score `-1.8133` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0396` n `13`; crypto_alt avg `0.239` n `239`; crypto_major avg `0.4419` n `8`; equity avg `0.6178` n `160`; fx avg `-0.0381` n `6`; index avg `0.0615` n `27`; metal avg `0.0344` n `20`; unknown avg `0.1577` n `1261`
- 1h: commodity avg `0.2368` n `13`; crypto_alt avg `0.5878` n `239`; crypto_major avg `0.8804` n `8`; equity avg `2.6937` n `160`; fx avg `-0.0341` n `6`; index avg `0.3153` n `27`; metal avg `-0.0472` n `20`; unknown avg `1.8226` n `1255`
- 4h: commodity avg `0.217` n `13`; crypto_alt avg `1.5206` n `239`; crypto_major avg `1.1273` n `8`; equity avg `3.3815` n `160`; fx avg `-0.0035` n `6`; index avg `0.3801` n `27`; metal avg `0.1094` n `20`; unknown avg `23.8238` n `1249`
- 24h: commodity avg `-0.3675` n `13`; crypto_alt avg `0.5652` n `239`; crypto_major avg `-2.0874` n `8`; equity avg `3.2945` n `160`; fx avg `-0.1508` n `6`; index avg `0.4068` n `27`; metal avg `0.4337` n `20`; unknown avg `6.2546` n `1026`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
