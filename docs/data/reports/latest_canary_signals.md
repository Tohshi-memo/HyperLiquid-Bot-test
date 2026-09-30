# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T13:07:30.737243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.59` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `2.136` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.0871` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5326` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0076` n `12`; crypto_alt avg `0.0523` n `234`; crypto_major avg `-0.1321` n `8`; equity avg `0.1127` n `142`; fx avg `-0.0125` n `6`; index avg `0.0368` n `26`; metal avg `-0.0041` n `20`; unknown avg `3.1531` n `961`
- 1h: commodity avg `-0.0573` n `12`; crypto_alt avg `1.3634` n `234`; crypto_major avg `1.379` n `8`; equity avg `0.7712` n `142`; fx avg `-0.0411` n `6`; index avg `0.1727` n `26`; metal avg `0.1274` n `20`; unknown avg `3.9902` n `961`
- 4h: commodity avg `-0.0102` n `12`; crypto_alt avg `1.6888` n `234`; crypto_major avg `2.1258` n `8`; equity avg `0.5932` n `142`; fx avg `-0.0048` n `6`; index avg `0.1136` n `26`; metal avg `0.0387` n `20`; unknown avg `4.2369` n `955`
- 24h: commodity avg `-0.0398` n `12`; crypto_alt avg `0.8092` n `234`; crypto_major avg `0.3427` n `8`; equity avg `0.4441` n `142`; fx avg `0.0119` n `6`; index avg `0.1305` n `26`; metal avg `0.2486` n `20`; unknown avg `2935.3143` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
