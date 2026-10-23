# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T06:07:27.726375+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `13`; crypto_alt avg `-0.1049` n `237`; crypto_major avg `-0.0787` n `8`; equity avg `0.0871` n `151`; fx avg `-0.0011` n `6`; index avg `0.0023` n `26`; metal avg `-0.0538` n `20`; unknown avg `0.6286` n `1212`
- 1h: commodity avg `0.058` n `13`; crypto_alt avg `0.1583` n `237`; crypto_major avg `0.1626` n `8`; equity avg `0.4412` n `151`; fx avg `-0.0061` n `6`; index avg `0.0289` n `26`; metal avg `0.0895` n `20`; unknown avg `0.3566` n `1211`
- 4h: commodity avg `-0.0476` n `13`; crypto_alt avg `0.8663` n `237`; crypto_major avg `0.6594` n `8`; equity avg `1.3236` n `151`; fx avg `0.0304` n `6`; index avg `0.1664` n `26`; metal avg `0.1867` n `20`; unknown avg `1.1564` n `1203`
- 24h: commodity avg `0.2793` n `13`; crypto_alt avg `-0.8748` n `237`; crypto_major avg `-0.8` n `8`; equity avg `-1.8455` n `151`; fx avg `-0.1071` n `6`; index avg `-0.1724` n `26`; metal avg `-0.5416` n `20`; unknown avg `52.6208` n `899`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1901`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1732`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1103`, n `668`, weak_sample_signal
