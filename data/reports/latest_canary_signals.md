# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T23:07:26.406879+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `13`; crypto_alt avg `-0.0486` n `237`; crypto_major avg `-0.0418` n `8`; equity avg `0.0` n `152`; fx avg `0.0016` n `6`; index avg `0.0074` n `26`; metal avg `0.0066` n `20`; unknown avg `-0.0116` n `1229`
- 1h: commodity avg `-0.0276` n `13`; crypto_alt avg `0.0669` n `237`; crypto_major avg `0.1571` n `8`; equity avg `0.0624` n `152`; fx avg `-0.0062` n `6`; index avg `0.0055` n `26`; metal avg `0.0246` n `20`; unknown avg `0.0114` n `1227`
- 4h: commodity avg `-0.0299` n `13`; crypto_alt avg `0.3635` n `237`; crypto_major avg `0.3256` n `8`; equity avg `0.0631` n `152`; fx avg `-0.0007` n `6`; index avg `0.0153` n `26`; metal avg `0.0114` n `20`; unknown avg `0.9528` n `1139`
- 24h: commodity avg `-0.1159` n `13`; crypto_alt avg `-0.1184` n `237`; crypto_major avg `-0.2996` n `8`; equity avg `0.1647` n `152`; fx avg `-0.0721` n `6`; index avg `0.0226` n `26`; metal avg `-0.0622` n `20`; unknown avg `1.302` n `1064`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1921`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1783`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1587`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1502`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
