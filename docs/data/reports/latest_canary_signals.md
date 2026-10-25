# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T17:22:32.968918+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.032` n `13`; crypto_alt avg `0.1909` n `237`; crypto_major avg `0.08` n `8`; equity avg `-0.0116` n `152`; fx avg `-0.0014` n `6`; index avg `-0.0055` n `26`; metal avg `0.002` n `20`; unknown avg `3.1142` n `1240`
- 1h: commodity avg `0.0315` n `13`; crypto_alt avg `0.9305` n `237`; crypto_major avg `0.5472` n `8`; equity avg `0.1811` n `152`; fx avg `0.0051` n `6`; index avg `0.0253` n `26`; metal avg `0.0446` n `20`; unknown avg `1.254` n `1200`
- 4h: commodity avg `-0.047` n `13`; crypto_alt avg `1.3056` n `237`; crypto_major avg `0.8652` n `8`; equity avg `0.3369` n `152`; fx avg `-0.0076` n `6`; index avg `0.0513` n `26`; metal avg `0.085` n `20`; unknown avg `0.1054` n `1185`
- 24h: commodity avg `-0.1862` n `13`; crypto_alt avg `1.2124` n `237`; crypto_major avg `1.6476` n `8`; equity avg `0.8364` n `152`; fx avg `0.0184` n `6`; index avg `0.1517` n `26`; metal avg `0.171` n `20`; unknown avg `10.4378` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2258`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1696`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1379`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
