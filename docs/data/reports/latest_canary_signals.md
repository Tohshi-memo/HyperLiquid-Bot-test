# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T16:37:35.043440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `13`; crypto_alt avg `-0.521` n `237`; crypto_major avg `-0.4141` n `8`; equity avg `-0.1243` n `154`; fx avg `0.0007` n `6`; index avg `-0.0123` n `27`; metal avg `-0.0158` n `20`; unknown avg `-0.0011` n `1238`
- 1h: commodity avg `0.2938` n `13`; crypto_alt avg `-1.3614` n `237`; crypto_major avg `-1.0419` n `8`; equity avg `-0.4881` n `154`; fx avg `-0.003` n `6`; index avg `-0.0594` n `27`; metal avg `-0.0665` n `20`; unknown avg `2.355` n `1232`
- 4h: commodity avg `0.4339` n `13`; crypto_alt avg `-0.4217` n `237`; crypto_major avg `-0.4336` n `8`; equity avg `0.7745` n `153`; fx avg `0.0182` n `6`; index avg `0.1409` n `27`; metal avg `-0.0496` n `20`; unknown avg `599.4082` n `1154`
- 24h: commodity avg `0.139` n `13`; crypto_alt avg `-0.3697` n `237`; crypto_major avg `-0.2492` n `8`; equity avg `0.6518` n `153`; fx avg `0.0721` n `6`; index avg `-0.0701` n `27`; metal avg `0.1139` n `20`; unknown avg `789.7048` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2256`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1898`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1867`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1027`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
