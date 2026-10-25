# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-25T18:07:25.483993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `-0.0595` n `237`; crypto_major avg `-0.0743` n `8`; equity avg `0.0134` n `152`; fx avg `-0.0086` n `6`; index avg `0.0064` n `26`; metal avg `0.0021` n `20`; unknown avg `-0.1527` n `1238`
- 1h: commodity avg `0.0374` n `13`; crypto_alt avg `-0.0432` n `237`; crypto_major avg `-0.1388` n `8`; equity avg `0.0169` n `152`; fx avg `-0.0061` n `6`; index avg `-0.0029` n `26`; metal avg `0.0123` n `20`; unknown avg `3.0574` n `1240`
- 4h: commodity avg `-0.0174` n `13`; crypto_alt avg `1.2154` n `237`; crypto_major avg `0.7058` n `8`; equity avg `0.44` n `152`; fx avg `-0.0219` n `6`; index avg `0.044` n `26`; metal avg `0.0648` n `20`; unknown avg `3.2439` n `1185`
- 24h: commodity avg `-0.2517` n `13`; crypto_alt avg `1.0436` n `237`; crypto_major avg `1.3413` n `8`; equity avg `0.9128` n `152`; fx avg `0.0116` n `6`; index avg `0.1604` n `26`; metal avg `0.1816` n `20`; unknown avg `10.5853` n `1043`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2253`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1374`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
