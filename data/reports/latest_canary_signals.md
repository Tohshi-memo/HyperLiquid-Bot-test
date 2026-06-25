# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T07:07:29.077090+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.048` n `12`; crypto_alt avg `-0.0984` n `228`; crypto_major avg `-0.1408` n `8`; equity avg `0.1192` n `86`; fx avg `-0.0014` n `6`; index avg `0.0084` n `23`; metal avg `-0.0122` n `20`; unknown avg `0.0724` n `757`
- 1h: commodity avg `0.1002` n `12`; crypto_alt avg `-0.1297` n `228`; crypto_major avg `0.1879` n `8`; equity avg `0.0762` n `86`; fx avg `-0.0095` n `6`; index avg `-0.0157` n `23`; metal avg `-0.1077` n `20`; unknown avg `0.0826` n `757`
- 4h: commodity avg `0.1395` n `12`; crypto_alt avg `0.9922` n `228`; crypto_major avg `1.3287` n `8`; equity avg `0.4888` n `86`; fx avg `-0.0383` n `6`; index avg `0.0497` n `23`; metal avg `-0.0033` n `20`; unknown avg `-0.0221` n `740`
- 24h: commodity avg `-0.3599` n `12`; crypto_alt avg `-1.0571` n `228`; crypto_major avg `-0.5744` n `8`; equity avg `0.1164` n `86`; fx avg `-0.0641` n `6`; index avg `0.526` n `23`; metal avg `-1.8351` n `20`; unknown avg `-0.87` n `708`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
