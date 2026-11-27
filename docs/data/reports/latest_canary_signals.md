# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T03:52:24.740861+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1242` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0029` n `13`; crypto_alt avg `-0.1117` n `239`; crypto_major avg `-0.1816` n `8`; equity avg `0.041` n `168`; fx avg `0.0073` n `6`; index avg `0.0184` n `27`; metal avg `-0.0008` n `20`; unknown avg `61.7364` n `1263`
- 1h: commodity avg `-0.0049` n `13`; crypto_alt avg `0.1707` n `239`; crypto_major avg `0.4319` n `8`; equity avg `0.5018` n `168`; fx avg `-0.0299` n `6`; index avg `0.0538` n `27`; metal avg `0.0442` n `20`; unknown avg `55.5144` n `1251`
- 4h: commodity avg `0.1498` n `13`; crypto_alt avg `1.5716` n `239`; crypto_major avg `2.274` n `8`; equity avg `2.8193` n `168`; fx avg `-0.0259` n `6`; index avg `0.2772` n `27`; metal avg `0.9398` n `20`; unknown avg `1.5555` n `1243`
- 24h: commodity avg `0.1611` n `13`; crypto_alt avg `1.5265` n `239`; crypto_major avg `1.7117` n `8`; equity avg `2.3541` n `168`; fx avg `0.0249` n `6`; index avg `0.2401` n `27`; metal avg `0.7279` n `20`; unknown avg `203.2527` n `993`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
