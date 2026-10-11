# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T09:22:30.292395+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0064` n `13`; crypto_alt avg `-0.0363` n `235`; crypto_major avg `-0.0222` n `8`; equity avg `0.0087` n `150`; fx avg `0.0007` n `6`; index avg `0.001` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.0012` n `1117`
- 1h: commodity avg `-0.0013` n `13`; crypto_alt avg `0.0652` n `235`; crypto_major avg `0.0338` n `8`; equity avg `0.0419` n `150`; fx avg `-0.0025` n `6`; index avg `0.0037` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.048` n `1115`
- 4h: commodity avg `0.0` n `5`; crypto_alt avg `0.3763` n `235`; crypto_major avg `-0.0843` n `8`; equity avg `0.0473` n `41`; fx avg `0.0` n `1`; index avg `0.0` n `17`; metal avg `0.0088` n `12`; unknown avg `0.137` n `1053`
- 24h: commodity avg `0.1962` n `13`; crypto_alt avg `1.1476` n `235`; crypto_major avg `-0.2569` n `8`; equity avg `0.0917` n `150`; fx avg `-0.0011` n `6`; index avg `-0.0007` n `26`; metal avg `0.0131` n `20`; unknown avg `0.6517` n `943`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
