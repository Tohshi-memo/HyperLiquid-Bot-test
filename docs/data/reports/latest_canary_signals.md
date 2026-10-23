# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T09:07:32.445464+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `13`; crypto_alt avg `-0.116` n `237`; crypto_major avg `-0.1187` n `8`; equity avg `-0.0953` n `152`; fx avg `-0.0189` n `6`; index avg `-0.0076` n `26`; metal avg `0.0005` n `20`; unknown avg `0.6764` n `1219`
- 1h: commodity avg `-0.0468` n `13`; crypto_alt avg `0.1548` n `237`; crypto_major avg `0.1562` n `8`; equity avg `0.1449` n `152`; fx avg `-0.0365` n `6`; index avg `-0.0045` n `26`; metal avg `0.0757` n `20`; unknown avg `0.0837` n `1213`
- 4h: commodity avg `0.0157` n `13`; crypto_alt avg `0.3219` n `237`; crypto_major avg `0.4409` n `8`; equity avg `1.0114` n `152`; fx avg `-0.0662` n `6`; index avg `0.0455` n `26`; metal avg `0.0614` n `20`; unknown avg `-0.0042` n `1146`
- 24h: commodity avg `0.1484` n `13`; crypto_alt avg `0.5156` n `237`; crypto_major avg `0.655` n `8`; equity avg `-0.4853` n `152`; fx avg `-0.0893` n `6`; index avg `-0.0411` n `26`; metal avg `-0.3394` n `20`; unknown avg `53.5131` n `880`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1802`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1597`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
