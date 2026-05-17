# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T19:57:17.075954+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `12`; crypto_alt avg `0.1825` n `228`; crypto_major avg `0.2477` n `8`; equity avg `0.1228` n `65`; fx avg `0.0` n `5`; index avg `0.0301` n `23`; metal avg `-0.005` n `18`; unknown avg `0.1634` n `384`
- 1h: commodity avg `-0.0157` n `12`; crypto_alt avg `0.5418` n `228`; crypto_major avg `0.9191` n `8`; equity avg `0.2563` n `65`; fx avg `-0.0011` n `5`; index avg `0.0579` n `23`; metal avg `-0.0587` n `18`; unknown avg `1.1405` n `384`
- 4h: commodity avg `0.0395` n `12`; crypto_alt avg `0.2422` n `228`; crypto_major avg `1.2458` n `8`; equity avg `0.2776` n `65`; fx avg `0.0101` n `5`; index avg `0.0573` n `23`; metal avg `-0.1287` n `18`; unknown avg `1.219` n `384`
- 24h: commodity avg `1.8455` n `12`; crypto_alt avg `-9.0889` n `228`; crypto_major avg `-1.2302` n `8`; equity avg `-2.2982` n `65`; fx avg `-0.1549` n `5`; index avg `-1.5382` n `23`; metal avg `-5.9511` n `18`; unknown avg `551.2881` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
