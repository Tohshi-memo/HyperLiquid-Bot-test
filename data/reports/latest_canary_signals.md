# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T16:07:29.807581+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.0629` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.9176` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.27` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0214` n `12`; crypto_alt avg `-0.1859` n `232`; crypto_major avg `-0.3036` n `8`; equity avg `-0.151` n `133`; fx avg `0.0052` n `6`; index avg `-0.016` n `26`; metal avg `0.0167` n `20`; unknown avg `0.1904` n `790`
- 1h: commodity avg `-0.2593` n `12`; crypto_alt avg `0.5215` n `232`; crypto_major avg `0.13` n `8`; equity avg `0.2671` n `133`; fx avg `-0.0102` n `6`; index avg `0.0521` n `26`; metal avg `0.0016` n `20`; unknown avg `1.4658` n `790`
- 4h: commodity avg `-0.5643` n `12`; crypto_alt avg `2.1167` n `232`; crypto_major avg `3.4986` n `8`; equity avg `1.2286` n `133`; fx avg `-0.0105` n `6`; index avg `0.2753` n `26`; metal avg `0.581` n `20`; unknown avg `8.6908` n `790`
- 24h: commodity avg `-0.139` n `12`; crypto_alt avg `3.8843` n `232`; crypto_major avg `4.8441` n `8`; equity avg `1.7853` n `133`; fx avg `-0.3052` n `6`; index avg `0.1645` n `26`; metal avg `0.921` n `20`; unknown avg `1.3669` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1047`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
