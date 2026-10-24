# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T18:07:27.203227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0658` n `13`; crypto_alt avg `0.0128` n `237`; crypto_major avg `-0.022` n `8`; equity avg `-0.0107` n `152`; fx avg `0.0044` n `6`; index avg `-0.0017` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.1243` n `1229`
- 1h: commodity avg `0.0721` n `13`; crypto_alt avg `0.0441` n `237`; crypto_major avg `0.1462` n `8`; equity avg `-0.0093` n `152`; fx avg `0.0048` n `6`; index avg `-0.0011` n `26`; metal avg `0.0094` n `20`; unknown avg `0.5948` n `1231`
- 4h: commodity avg `0.0879` n `13`; crypto_alt avg `-1.0768` n `237`; crypto_major avg `-0.7998` n `8`; equity avg `-0.3162` n `152`; fx avg `-0.0103` n `6`; index avg `-0.0435` n `26`; metal avg `-0.1124` n `20`; unknown avg `0.1344` n `1198`
- 24h: commodity avg `0.2362` n `13`; crypto_alt avg `-3.965` n `237`; crypto_major avg `-2.6373` n `8`; equity avg `-0.8576` n `152`; fx avg `-0.0284` n `6`; index avg `-0.1002` n `26`; metal avg `-0.2314` n `20`; unknown avg `-0.6165` n `1045`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1836`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
