# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T11:52:30.711346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0164` n `13`; crypto_alt avg `0.0696` n `237`; crypto_major avg `0.1019` n `8`; equity avg `0.324` n `152`; fx avg `0.0012` n `6`; index avg `0.0584` n `26`; metal avg `0.0509` n `20`; unknown avg `0.3297` n `1240`
- 1h: commodity avg `0.1281` n `13`; crypto_alt avg `0.0998` n `237`; crypto_major avg `0.0357` n `8`; equity avg `0.429` n `152`; fx avg `0.0089` n `6`; index avg `0.0857` n `26`; metal avg `0.0603` n `20`; unknown avg `1.0054` n `1240`
- 4h: commodity avg `0.0747` n `13`; crypto_alt avg `0.9081` n `237`; crypto_major avg `0.6592` n `8`; equity avg `0.6888` n `152`; fx avg `0.0248` n `6`; index avg `0.1324` n `26`; metal avg `0.0998` n `20`; unknown avg `0.5144` n `1150`
- 24h: commodity avg `-0.3831` n `13`; crypto_alt avg `0.0849` n `237`; crypto_major avg `0.0454` n `8`; equity avg `0.0326` n `152`; fx avg `0.0452` n `6`; index avg `0.0727` n `26`; metal avg `0.1818` n `20`; unknown avg `-0.1947` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2605`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2261`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2023`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
