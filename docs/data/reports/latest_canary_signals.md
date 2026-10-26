# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T11:22:28.358104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0566` n `13`; crypto_alt avg `0.1399` n `237`; crypto_major avg `0.0671` n `8`; equity avg `0.0572` n `152`; fx avg `-0.0033` n `6`; index avg `0.0074` n `26`; metal avg `0.0032` n `20`; unknown avg `0.0533` n `1240`
- 1h: commodity avg `0.09` n `13`; crypto_alt avg `-0.0758` n `237`; crypto_major avg `-0.0474` n `8`; equity avg `-0.2231` n `152`; fx avg `0.0026` n `6`; index avg `-0.0383` n `26`; metal avg `-0.0676` n `20`; unknown avg `3.0936` n `1240`
- 4h: commodity avg `0.1216` n `13`; crypto_alt avg `0.3456` n `237`; crypto_major avg `0.2744` n `8`; equity avg `0.0195` n `152`; fx avg `0.013` n `6`; index avg `0.0189` n `26`; metal avg `0.0524` n `20`; unknown avg `0.0224` n `1144`
- 24h: commodity avg `-0.411` n `13`; crypto_alt avg `0.2557` n `237`; crypto_major avg `0.1039` n `8`; equity avg `-0.4787` n `152`; fx avg `0.0365` n `6`; index avg `-0.0065` n `26`; metal avg `0.1333` n `20`; unknown avg `-0.3032` n `977`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2597`, n `668`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2308`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.2303`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
