# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T22:52:26.052411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0185` n `13`; crypto_alt avg `-0.0934` n `237`; crypto_major avg `-0.0158` n `8`; equity avg `-0.0163` n `152`; fx avg `-0.0071` n `6`; index avg `-0.0027` n `26`; metal avg `0.0002` n `20`; unknown avg `-0.0957` n `1231`
- 1h: commodity avg `-0.0302` n `13`; crypto_alt avg `0.2033` n `237`; crypto_major avg `0.3033` n `8`; equity avg `0.0501` n `152`; fx avg `-0.0091` n `6`; index avg `0.0029` n `26`; metal avg `0.0132` n `20`; unknown avg `0.0538` n `1205`
- 4h: commodity avg `-0.0132` n `13`; crypto_alt avg `0.4255` n `237`; crypto_major avg `0.4817` n `8`; equity avg `0.1604` n `152`; fx avg `-0.0146` n `6`; index avg `0.0374` n `26`; metal avg `0.0233` n `20`; unknown avg `0.766` n `1137`
- 24h: commodity avg `-0.0501` n `13`; crypto_alt avg `-0.123` n `237`; crypto_major avg `-0.275` n `8`; equity avg `0.1118` n `152`; fx avg `-0.0702` n `6`; index avg `0.0089` n `26`; metal avg `-0.0352` n `20`; unknown avg `0.3656` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.192`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1585`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
