# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T13:52:39.468679+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.17` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.2429` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1624` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.9625` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0275` n `12`; crypto_alt avg `-0.1746` n `228`; crypto_major avg `-0.2213` n `8`; equity avg `0.1476` n `74`; fx avg `0.0004` n `6`; index avg `0.2124` n `23`; metal avg `-0.0677` n `18`; unknown avg `0.2307` n `690`
- 1h: commodity avg `0.2091` n `12`; crypto_alt avg `0.5381` n `228`; crypto_major avg `0.4197` n `8`; equity avg `0.7193` n `74`; fx avg `0.0104` n `6`; index avg `0.4297` n `23`; metal avg `0.138` n `18`; unknown avg `0.4047` n `689`
- 4h: commodity avg `0.4105` n `12`; crypto_alt avg `2.2259` n `228`; crypto_major avg `2.6534` n `8`; equity avg `0.6909` n `74`; fx avg `0.0059` n `6`; index avg `0.5362` n `23`; metal avg `0.491` n `18`; unknown avg `0.7213` n `689`
- 24h: commodity avg `-1.1147` n `12`; crypto_alt avg `5.9191` n `228`; crypto_major avg `6.0221` n `8`; equity avg `2.3576` n `74`; fx avg `0.0411` n `6`; index avg `1.3627` n `23`; metal avg `2.9742` n `18`; unknown avg `2.0529` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
