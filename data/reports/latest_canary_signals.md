# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T15:07:29.810206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `3.6792` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `3.6258` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `3.5` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `3.2115` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0675` n `12`; crypto_alt avg `0.0592` n `233`; crypto_major avg `-0.1283` n `8`; equity avg `0.0241` n `136`; fx avg `0.0165` n `6`; index avg `0.031` n `26`; metal avg `-0.1167` n `20`; unknown avg `0.0687` n `794`
- 1h: commodity avg `0.0839` n `12`; crypto_alt avg `0.0654` n `233`; crypto_major avg `-0.5152` n `8`; equity avg `0.1351` n `136`; fx avg `0.0296` n `6`; index avg `0.0493` n `26`; metal avg `-0.1888` n `20`; unknown avg `2.6511` n `794`
- 4h: commodity avg `0.1881` n `12`; crypto_alt avg `4.03` n `233`; crypto_major avg `3.8139` n `8`; equity avg `0.6024` n `136`; fx avg `0.0016` n `6`; index avg `0.1231` n `26`; metal avg `0.1347` n `20`; unknown avg `5.7061` n `772`
- 24h: commodity avg `-0.0336` n `12`; crypto_alt avg `2.0822` n `233`; crypto_major avg `2.7717` n `8`; equity avg `-0.0068` n `136`; fx avg `-0.1194` n `6`; index avg `0.2135` n `26`; metal avg `0.0438` n `20`; unknown avg `5.3451` n `697`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0925`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
