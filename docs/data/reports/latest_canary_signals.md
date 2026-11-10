# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T20:52:32.436328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0276` n `13`; crypto_alt avg `0.3229` n `239`; crypto_major avg `0.3531` n `8`; equity avg `0.4532` n `160`; fx avg `-0.0022` n `6`; index avg `0.038` n `27`; metal avg `0.0294` n `20`; unknown avg `0.4165` n `1262`
- 1h: commodity avg `0.051` n `13`; crypto_alt avg `0.0655` n `239`; crypto_major avg `0.1987` n `8`; equity avg `0.5761` n `160`; fx avg `0.0029` n `6`; index avg `0.04` n `27`; metal avg `0.0352` n `20`; unknown avg `21.7306` n `1248`
- 4h: commodity avg `0.0886` n `13`; crypto_alt avg `0.4506` n `239`; crypto_major avg `1.1784` n `8`; equity avg `0.8936` n `160`; fx avg `0.0379` n `6`; index avg `0.0593` n `27`; metal avg `0.1493` n `20`; unknown avg `19.4484` n `1248`
- 24h: commodity avg `0.0567` n `13`; crypto_alt avg `-1.7065` n `239`; crypto_major avg `-2.6565` n `8`; equity avg `-1.2633` n `160`; fx avg `-0.0781` n `6`; index avg `-0.1923` n `27`; metal avg `-0.6247` n `20`; unknown avg `-0.1017` n `1161`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2579`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
