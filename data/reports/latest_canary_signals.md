# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T20:07:36.508056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `13`; crypto_alt avg `0.347` n `237`; crypto_major avg `0.2366` n `8`; equity avg `0.0554` n `152`; fx avg `0.0125` n `6`; index avg `0.0066` n `26`; metal avg `0.008` n `20`; unknown avg `-0.0367` n `1199`
- 1h: commodity avg `-0.0058` n `13`; crypto_alt avg `0.2375` n `237`; crypto_major avg `0.2213` n `8`; equity avg `0.0593` n `152`; fx avg `0.009` n `6`; index avg `0.005` n `26`; metal avg `0.0132` n `20`; unknown avg `0.7867` n `1183`
- 4h: commodity avg `-0.0287` n `13`; crypto_alt avg `1.445` n `237`; crypto_major avg `1.4232` n `8`; equity avg `0.6172` n `152`; fx avg `-0.0067` n `6`; index avg `0.0789` n `26`; metal avg `0.0675` n `20`; unknown avg `1.394` n `1159`
- 24h: commodity avg `0.0314` n `13`; crypto_alt avg `-2.1995` n `237`; crypto_major avg `-1.3596` n `8`; equity avg `-0.1236` n `152`; fx avg `-0.021` n `6`; index avg `-0.0196` n `26`; metal avg `-0.1371` n `20`; unknown avg `-0.6326` n `1026`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1918`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1819`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
