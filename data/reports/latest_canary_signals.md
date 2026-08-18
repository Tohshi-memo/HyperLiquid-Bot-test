# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-18T23:41:33.713785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `12`; crypto_alt avg `0.0586` n `230`; crypto_major avg `0.0553` n `8`; equity avg `-0.1636` n `120`; fx avg `0.001` n `6`; index avg `-0.0258` n `25`; metal avg `-0.0501` n `20`; unknown avg `-0.137` n `789`
- 1h: commodity avg `0.014` n `12`; crypto_alt avg `0.1021` n `230`; crypto_major avg `0.1378` n `8`; equity avg `-0.288` n `120`; fx avg `-0.0008` n `6`; index avg `-0.0099` n `25`; metal avg `-0.061` n `20`; unknown avg `-0.2194` n `789`
- 4h: commodity avg `0.1138` n `12`; crypto_alt avg `-0.177` n `230`; crypto_major avg `-0.0779` n `8`; equity avg `-0.6414` n `120`; fx avg `-0.0092` n `6`; index avg `-0.0659` n `25`; metal avg `-0.2145` n `20`; unknown avg `0.0576` n `789`
- 24h: commodity avg `0.3127` n `12`; crypto_alt avg `-0.4284` n `230`; crypto_major avg `0.0589` n `8`; equity avg `-4.8582` n `120`; fx avg `-0.0322` n `6`; index avg `-0.7251` n `25`; metal avg `-0.9077` n `20`; unknown avg `-0.2516` n `755`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1174`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
