# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T01:23:04.964671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0462` n `12`; crypto_alt avg `0.0234` n `232`; crypto_major avg `-0.0075` n `8`; equity avg `-0.0415` n `133`; fx avg `0.0068` n `6`; index avg `-0.0036` n `26`; metal avg `0.0471` n `20`; unknown avg `0.0801` n `793`
- 1h: commodity avg `0.0473` n `12`; crypto_alt avg `-0.4379` n `232`; crypto_major avg `-0.3233` n `8`; equity avg `0.0612` n `133`; fx avg `0.0374` n `6`; index avg `0.007` n `26`; metal avg `-0.0205` n `20`; unknown avg `3.1655` n `784`
- 4h: commodity avg `0.0112` n `12`; crypto_alt avg `-0.6882` n `232`; crypto_major avg `-0.4931` n `8`; equity avg `0.2653` n `133`; fx avg `0.0422` n `6`; index avg `0.0147` n `26`; metal avg `-0.026` n `20`; unknown avg `2.591` n `784`
- 24h: commodity avg `-0.1383` n `12`; crypto_alt avg `3.0931` n `232`; crypto_major avg `4.5412` n `8`; equity avg `1.5075` n `133`; fx avg `-0.1473` n `6`; index avg `0.2004` n `26`; metal avg `0.7227` n `20`; unknown avg `1.1665` n `736`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
