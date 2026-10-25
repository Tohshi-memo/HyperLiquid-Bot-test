# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T17:37:27.634374+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0076` n `13`; crypto_alt avg `-0.1852` n `237`; crypto_major avg `-0.1854` n `8`; equity avg `-0.0131` n `152`; fx avg `0.0044` n `6`; index avg `-0.0055` n `26`; metal avg `0.003` n `20`; unknown avg `2.2877` n `1240`
- 1h: commodity avg `0.0402` n `13`; crypto_alt avg `0.6273` n `237`; crypto_major avg `0.3789` n `8`; equity avg `0.1115` n `152`; fx avg `0.0102` n `6`; index avg `0.0104` n `26`; metal avg `0.0397` n `20`; unknown avg `4.2685` n `1200`
- 4h: commodity avg `0.0351` n `13`; crypto_alt avg `1.1621` n `237`; crypto_major avg `0.7193` n `8`; equity avg `0.3527` n `152`; fx avg `-0.0034` n `6`; index avg `0.0451` n `26`; metal avg `0.0841` n `20`; unknown avg `49.0451` n `1185`
- 24h: commodity avg `-0.1835` n `13`; crypto_alt avg `1.4529` n `237`; crypto_major avg `1.6282` n `8`; equity avg `0.9192` n `152`; fx avg `0.0315` n `6`; index avg `0.1531` n `26`; metal avg `0.1745` n `20`; unknown avg `10.3796` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2261`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
