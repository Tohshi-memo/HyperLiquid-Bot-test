# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T21:37:27.195593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0267` n `12`; crypto_alt avg `0.2103` n `232`; crypto_major avg `0.199` n `8`; equity avg `0.0292` n `133`; fx avg `-0.0071` n `6`; index avg `0.0017` n `26`; metal avg `0.0033` n `20`; unknown avg `2.8422` n `792`
- 1h: commodity avg `0.0089` n `12`; crypto_alt avg `0.3842` n `232`; crypto_major avg `0.1693` n `8`; equity avg `-0.0055` n `133`; fx avg `0.0006` n `6`; index avg `-0.0065` n `26`; metal avg `0.0057` n `20`; unknown avg `3.3292` n `784`
- 4h: commodity avg `0.0152` n `12`; crypto_alt avg `0.5272` n `232`; crypto_major avg `0.4128` n `8`; equity avg `0.0759` n `133`; fx avg `0.0069` n `6`; index avg `0.0053` n `26`; metal avg `-0.1057` n `20`; unknown avg `3.9025` n `772`
- 24h: commodity avg `-0.0674` n `12`; crypto_alt avg `4.8284` n `232`; crypto_major avg `5.6172` n `8`; equity avg `1.299` n `133`; fx avg `-0.2221` n `6`; index avg `0.1706` n `26`; metal avg `0.7813` n `20`; unknown avg `221.6955` n `736`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
