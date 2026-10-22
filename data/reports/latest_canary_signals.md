# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T23:21:04.126496+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.018` n `13`; crypto_alt avg `-0.0948` n `237`; crypto_major avg `-0.0804` n `8`; equity avg `-0.2024` n `151`; fx avg `-0.0055` n `6`; index avg `-0.0346` n `26`; metal avg `-0.004` n `20`; unknown avg `0.3152` n `1233`
- 1h: commodity avg `0.011` n `13`; crypto_alt avg `-0.2148` n `237`; crypto_major avg `-0.0705` n `8`; equity avg `-0.2575` n `151`; fx avg `0.0104` n `6`; index avg `-0.043` n `26`; metal avg `-0.0125` n `20`; unknown avg `0.0801` n `1191`
- 4h: commodity avg `-0.0148` n `13`; crypto_alt avg `-0.4751` n `237`; crypto_major avg `-0.2889` n `8`; equity avg `-0.3695` n `151`; fx avg `-0.0265` n `6`; index avg `-0.0402` n `26`; metal avg `-0.0157` n `20`; unknown avg `0.0224` n `1127`
- 24h: commodity avg `0.4847` n `13`; crypto_alt avg `-4.9961` n `237`; crypto_major avg `-3.5525` n `8`; equity avg `-5.1386` n `151`; fx avg `-0.1685` n `6`; index avg `-0.5651` n `26`; metal avg `-0.9683` n `20`; unknown avg `54.2642` n `905`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1559`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1536`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
