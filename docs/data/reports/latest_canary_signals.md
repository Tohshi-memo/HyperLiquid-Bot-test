# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T17:52:17.462194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0325` n `12`; crypto_alt avg `0.1204` n `228`; crypto_major avg `0.1159` n `8`; equity avg `0.0517` n `65`; fx avg `0.0` n `5`; index avg `0.0203` n `23`; metal avg `-0.0056` n `18`; unknown avg `0.0943` n `384`
- 1h: commodity avg `0.0087` n `12`; crypto_alt avg `-0.354` n `228`; crypto_major avg `-0.0118` n `8`; equity avg `-0.0922` n `65`; fx avg `0.011` n `5`; index avg `0.0083` n `23`; metal avg `-0.0173` n `18`; unknown avg `0.2037` n `384`
- 4h: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.612` n `228`; crypto_major avg `-0.1328` n `8`; equity avg `0.0041` n `65`; fx avg `0.0322` n `5`; index avg `-0.0034` n `23`; metal avg `-0.0259` n `18`; unknown avg `0.0702` n `383`
- 24h: commodity avg `1.7888` n `12`; crypto_alt avg `-9.6691` n `228`; crypto_major avg `-2.5268` n `8`; equity avg `-2.6179` n `65`; fx avg `-0.1543` n `5`; index avg `-1.6035` n `23`; metal avg `-5.8415` n `18`; unknown avg `550.0544` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
