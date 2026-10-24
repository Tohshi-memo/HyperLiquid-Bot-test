# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T13:52:27.161771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `13`; crypto_alt avg `0.1708` n `237`; crypto_major avg `0.1245` n `8`; equity avg `0.0335` n `152`; fx avg `0.0007` n `6`; index avg `-0.0003` n `26`; metal avg `0.0078` n `20`; unknown avg `0.9344` n `1230`
- 1h: commodity avg `-0.0258` n `13`; crypto_alt avg `-0.4149` n `237`; crypto_major avg `-0.0772` n `8`; equity avg `-0.0592` n `152`; fx avg `-0.0049` n `6`; index avg `-0.0142` n `26`; metal avg `0.0104` n `20`; unknown avg `-0.0484` n `1198`
- 4h: commodity avg `0.0767` n `13`; crypto_alt avg `-0.1889` n `237`; crypto_major avg `0.2976` n `8`; equity avg `0.1533` n `152`; fx avg `-0.0079` n `6`; index avg `0.005` n `26`; metal avg `0.0156` n `20`; unknown avg `0.5052` n `1190`
- 24h: commodity avg `0.2214` n `13`; crypto_alt avg `-2.9546` n `237`; crypto_major avg `-2.2251` n `8`; equity avg `-0.2635` n `152`; fx avg `-0.0068` n `6`; index avg `0.0264` n `26`; metal avg `-0.1694` n `20`; unknown avg `194.0694` n `1053`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1923`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.192`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
