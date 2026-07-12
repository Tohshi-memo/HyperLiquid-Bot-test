# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T15:22:30.421647+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0223` n `12`; crypto_alt avg `-0.0673` n `230`; crypto_major avg `-0.0905` n `8`; equity avg `0.006` n `92`; fx avg `0.0024` n `6`; index avg `-0.0011` n `25`; metal avg `0.0061` n `20`; unknown avg `0.0233` n `765`
- 1h: commodity avg `-0.0252` n `12`; crypto_alt avg `0.3711` n `230`; crypto_major avg `0.4333` n `8`; equity avg `0.0438` n `92`; fx avg `-0.0012` n `6`; index avg `0.0131` n `25`; metal avg `0.0153` n `20`; unknown avg `0.0474` n `765`
- 4h: commodity avg `-0.1048` n `12`; crypto_alt avg `0.4842` n `230`; crypto_major avg `0.7814` n `8`; equity avg `0.066` n `92`; fx avg `0.0036` n `6`; index avg `0.034` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.0082` n `765`
- 24h: commodity avg `0.4492` n `12`; crypto_alt avg `-1.2123` n `230`; crypto_major avg `-0.7108` n `8`; equity avg `-0.0659` n `92`; fx avg `0.0321` n `6`; index avg `-0.1154` n `25`; metal avg `-0.0895` n `20`; unknown avg `0.0953` n `745`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1321`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
