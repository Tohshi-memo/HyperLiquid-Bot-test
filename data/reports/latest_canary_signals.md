# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T06:52:33.378984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.078` n `13`; crypto_alt avg `0.0779` n `237`; crypto_major avg `0.1308` n `8`; equity avg `0.0602` n `152`; fx avg `0.013` n `6`; index avg `-0.0049` n `26`; metal avg `-0.018` n `20`; unknown avg `0.1334` n `1233`
- 1h: commodity avg `-0.0546` n `13`; crypto_alt avg `0.0771` n `237`; crypto_major avg `0.1904` n `8`; equity avg `0.5449` n `152`; fx avg `0.0157` n `6`; index avg `0.0456` n `26`; metal avg `-0.0798` n `20`; unknown avg `0.8922` n `1211`
- 4h: commodity avg `0.0292` n `13`; crypto_alt avg `0.2843` n `237`; crypto_major avg `0.2805` n `8`; equity avg `1.3806` n `152`; fx avg `0.0201` n `6`; index avg `0.1292` n `26`; metal avg `-0.0034` n `20`; unknown avg `0.2938` n `1202`
- 24h: commodity avg `0.1958` n `13`; crypto_alt avg `-0.2697` n `237`; crypto_major avg `-0.205` n `8`; equity avg `-1.1441` n `152`; fx avg `-0.0376` n `6`; index avg `-0.0901` n `26`; metal avg `-0.493` n `20`; unknown avg `52.865` n `898`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
