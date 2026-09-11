# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T15:37:31.634434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.9502` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.8395` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- polymarket_volume_spike: score `3.64` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `3.2932` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0129` n `12`; crypto_alt avg `0.3036` n `233`; crypto_major avg `0.2481` n `8`; equity avg `0.096` n `136`; fx avg `0.0015` n `6`; index avg `0.0024` n `26`; metal avg `0.0233` n `20`; unknown avg `0.617` n `796`
- 1h: commodity avg `-0.099` n `12`; crypto_alt avg `0.6545` n `233`; crypto_major avg `0.3223` n `8`; equity avg `0.1844` n `136`; fx avg `-0.009` n `6`; index avg `0.0591` n `26`; metal avg `-0.0046` n `20`; unknown avg `1.5771` n `794`
- 4h: commodity avg `0.0767` n `12`; crypto_alt avg `4.1259` n `233`; crypto_major avg `4.0269` n `8`; equity avg `0.7337` n `136`; fx avg `-0.0322` n `6`; index avg `0.141` n `26`; metal avg `0.1874` n `20`; unknown avg `1.1217` n `772`
- 24h: commodity avg `-0.1444` n `12`; crypto_alt avg `2.3035` n `233`; crypto_major avg `3.1715` n `8`; equity avg `0.1815` n `136`; fx avg `-0.1332` n `6`; index avg `0.251` n `26`; metal avg `0.0486` n `20`; unknown avg `2.2812` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
