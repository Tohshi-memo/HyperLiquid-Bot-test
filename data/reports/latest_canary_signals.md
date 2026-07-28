# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T16:22:41.371883+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.09` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.9336` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0555` n `12`; crypto_alt avg `-0.05` n `230`; crypto_major avg `-0.021` n `8`; equity avg `-0.1677` n `102`; fx avg `-0.0138` n `6`; index avg `-0.0252` n `25`; metal avg `0.0102` n `20`; unknown avg `0.0345` n `774`
- 1h: commodity avg `-0.3181` n `12`; crypto_alt avg `0.1441` n `230`; crypto_major avg `0.1758` n `8`; equity avg `0.2851` n `102`; fx avg `-0.0128` n `6`; index avg `0.0361` n `25`; metal avg `0.118` n `20`; unknown avg `-0.2036` n `774`
- 4h: commodity avg `-0.8192` n `12`; crypto_alt avg `0.5269` n `230`; crypto_major avg `1.0709` n `8`; equity avg `-0.8627` n `102`; fx avg `-0.0209` n `6`; index avg `0.0619` n `25`; metal avg `0.1921` n `20`; unknown avg `0.1008` n `774`
- 24h: commodity avg `-1.4149` n `12`; crypto_alt avg `-1.28` n `230`; crypto_major avg `-1.2473` n `8`; equity avg `-2.4008` n `102`; fx avg `-0.1234` n `6`; index avg `-0.1715` n `25`; metal avg `-0.3118` n `20`; unknown avg `1225.4314` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
