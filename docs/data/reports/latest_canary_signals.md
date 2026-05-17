# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T16:07:13.656026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `12`; crypto_alt avg `0.1683` n `228`; crypto_major avg `0.1317` n `8`; equity avg `-0.004` n `65`; fx avg `-0.0009` n `5`; index avg `0.0164` n `23`; metal avg `-0.0012` n `18`; unknown avg `-0.0295` n `384`
- 1h: commodity avg `0.0511` n `12`; crypto_alt avg `0.0611` n `228`; crypto_major avg `-0.0433` n `8`; equity avg `0.1489` n `65`; fx avg `-0.0009` n `5`; index avg `0.0555` n `23`; metal avg `0.0263` n `18`; unknown avg `-0.1053` n `384`
- 4h: commodity avg `0.0527` n `12`; crypto_alt avg `-0.196` n `228`; crypto_major avg `-0.1033` n `8`; equity avg `0.022` n `65`; fx avg `0.0207` n `5`; index avg `0.0747` n `23`; metal avg `0.0199` n `18`; unknown avg `-0.0882` n `383`
- 24h: commodity avg `1.8107` n `12`; crypto_alt avg `-9.1513` n `228`; crypto_major avg `-2.378` n `8`; equity avg `-2.5752` n `65`; fx avg `-0.1657` n `5`; index avg `-1.5806` n `23`; metal avg `-5.8292` n `18`; unknown avg `550.0024` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
