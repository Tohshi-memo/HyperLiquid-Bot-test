# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T12:22:33.893955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `13`; crypto_alt avg `-0.126` n `237`; crypto_major avg `-0.0739` n `8`; equity avg `-0.0036` n `152`; fx avg `-0.0012` n `6`; index avg `0.0034` n `26`; metal avg `0.0021` n `20`; unknown avg `0.8958` n `1231`
- 1h: commodity avg `-0.069` n `13`; crypto_alt avg `0.1888` n `237`; crypto_major avg `0.0841` n `8`; equity avg `0.0802` n `152`; fx avg `0.0009` n `6`; index avg `0.0226` n `26`; metal avg `0.0178` n `20`; unknown avg `-0.0337` n `1225`
- 4h: commodity avg `-0.0691` n `13`; crypto_alt avg `-0.1168` n `237`; crypto_major avg `-0.1411` n `8`; equity avg `0.1072` n `152`; fx avg `0.0239` n `6`; index avg `0.0145` n `26`; metal avg `0.0293` n `20`; unknown avg `15.7368` n `1191`
- 24h: commodity avg `-0.1321` n `13`; crypto_alt avg `-1.5131` n `237`; crypto_major avg `-0.0323` n `8`; equity avg `-0.0142` n `152`; fx avg `0.0003` n `6`; index avg `0.0282` n `26`; metal avg `-0.0253` n `20`; unknown avg `17.4775` n `1048`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1711`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1447`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
