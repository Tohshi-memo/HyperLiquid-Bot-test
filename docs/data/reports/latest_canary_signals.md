# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T15:15:19.105407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.4185` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4728` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `2.3296` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0521` n `12`; crypto_alt avg `-0.2133` n `232`; crypto_major avg `-0.3688` n `8`; equity avg `0.0159` n `133`; fx avg `0.0068` n `6`; index avg `0.0116` n `26`; metal avg `0.0463` n `20`; unknown avg `19.1982` n `792`
- 1h: commodity avg `-0.2432` n `12`; crypto_alt avg `0.8936` n `232`; crypto_major avg `1.6087` n `8`; equity avg `0.5508` n `133`; fx avg `0.0333` n `6`; index avg `0.1079` n `26`; metal avg `0.378` n `20`; unknown avg `-0.4455` n `790`
- 4h: commodity avg `-0.2506` n `12`; crypto_alt avg `1.5267` n `232`; crypto_major avg `3.1679` n `8`; equity avg `0.8383` n `133`; fx avg `0.0155` n `6`; index avg `0.2215` n `26`; metal avg `0.6951` n `20`; unknown avg `22.7088` n `790`
- 24h: commodity avg `0.0589` n `12`; crypto_alt avg `3.6726` n `232`; crypto_major avg `4.7654` n `8`; equity avg `1.7108` n `133`; fx avg `-0.2609` n `6`; index avg `0.153` n `26`; metal avg `0.9737` n `20`; unknown avg `20.2478` n `736`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0549`, n `668`, weak_sample_signal
