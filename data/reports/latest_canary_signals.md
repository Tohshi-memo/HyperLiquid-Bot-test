# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T14:22:27.993617+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.261` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.1675` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.9` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.8382` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 1h_crypto_metal_divergence: score `1.8864` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 1h_crypto_equity_divergence: score `1.7842` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.1506` n `12`; crypto_alt avg `0.2178` n `233`; crypto_major avg `-0.204` n `8`; equity avg `0.3853` n `136`; fx avg `0.0118` n `6`; index avg `0.0723` n `26`; metal avg `-0.0418` n `20`; unknown avg `1.0116` n `796`
- 1h: commodity avg `0.1811` n `12`; crypto_alt avg `1.7182` n `233`; crypto_major avg `1.9131` n `8`; equity avg `0.1289` n `136`; fx avg `0.0175` n `6`; index avg `0.0061` n `26`; metal avg `0.0267` n `20`; unknown avg `7.494` n `778`
- 4h: commodity avg `0.2783` n `12`; crypto_alt avg `3.0703` n `233`; crypto_major avg `3.4458` n `8`; equity avg `0.6076` n `136`; fx avg `-0.0579` n `6`; index avg `0.1155` n `26`; metal avg `0.1848` n `20`; unknown avg `5.2238` n `772`
- 24h: commodity avg `0.158` n `12`; crypto_alt avg `2.2712` n `233`; crypto_major avg `3.1572` n `8`; equity avg `0.6289` n `136`; fx avg `-0.1238` n `6`; index avg `0.2679` n `26`; metal avg `0.1088` n `20`; unknown avg `5.8499` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1152`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
