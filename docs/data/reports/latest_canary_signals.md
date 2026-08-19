# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-19T08:07:31.229905+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `12`; crypto_alt avg `0.0524` n `230`; crypto_major avg `-0.0356` n `8`; equity avg `0.3337` n `120`; fx avg `-0.0398` n `6`; index avg `0.0744` n `25`; metal avg `0.0526` n `20`; unknown avg `-0.0111` n `789`
- 1h: commodity avg `-0.0618` n `12`; crypto_alt avg `0.1105` n `230`; crypto_major avg `-0.0015` n `8`; equity avg `0.9665` n `120`; fx avg `-0.0461` n `6`; index avg `0.126` n `25`; metal avg `0.0829` n `20`; unknown avg `0.006` n `789`
- 4h: commodity avg `-0.0167` n `12`; crypto_alt avg `0.1687` n `230`; crypto_major avg `0.0514` n `8`; equity avg `1.2665` n `120`; fx avg `-0.0583` n `6`; index avg `0.2383` n `25`; metal avg `0.0396` n `20`; unknown avg `-0.02` n `757`
- 24h: commodity avg `0.2701` n `12`; crypto_alt avg `0.5604` n `230`; crypto_major avg `0.3388` n `8`; equity avg `-1.2763` n `120`; fx avg `-0.1969` n `6`; index avg `-0.1434` n `25`; metal avg `-0.4217` n `20`; unknown avg `-0.2174` n `757`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
