# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T11:07:25.420394+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0718` n `13`; crypto_alt avg `-0.2493` n `237`; crypto_major avg `-0.2505` n `8`; equity avg `-0.1724` n `152`; fx avg `0.0113` n `6`; index avg `-0.0204` n `26`; metal avg `-0.0123` n `20`; unknown avg `-0.0741` n `1238`
- 1h: commodity avg `-0.0361` n `13`; crypto_alt avg `-0.2685` n `237`; crypto_major avg `-0.1883` n `8`; equity avg `-0.4315` n `152`; fx avg `0.0055` n `6`; index avg `-0.0804` n `26`; metal avg `-0.0802` n `20`; unknown avg `0.0235` n `1240`
- 4h: commodity avg `0.1048` n `13`; crypto_alt avg `0.2471` n `237`; crypto_major avg `0.1419` n `8`; equity avg `-0.0466` n `152`; fx avg `0.0171` n `6`; index avg `0.0208` n `26`; metal avg `0.0504` n `20`; unknown avg `10.4712` n `1144`
- 24h: commodity avg `-0.4681` n `13`; crypto_alt avg `0.4335` n `237`; crypto_major avg `0.2776` n `8`; equity avg `-0.4431` n `152`; fx avg `0.0398` n `6`; index avg `-0.0098` n `26`; metal avg `0.1359` n `20`; unknown avg `-0.3002` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2608`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2312`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2311`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2018`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
