# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T20:22:30.121449+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0002` n `13`; crypto_alt avg `-0.0605` n `239`; crypto_major avg `-0.0192` n `8`; equity avg `0.0311` n `166`; fx avg `0.0055` n `6`; index avg `-0.0018` n `27`; metal avg `0.0023` n `20`; unknown avg `159.2781` n `1258`
- 1h: commodity avg `0.0344` n `13`; crypto_alt avg `0.045` n `239`; crypto_major avg `0.1313` n `8`; equity avg `0.0665` n `166`; fx avg `0.0045` n `6`; index avg `0.0378` n `27`; metal avg `-0.0057` n `20`; unknown avg `140.1435` n `1256`
- 4h: commodity avg `0.1002` n `13`; crypto_alt avg `0.0301` n `239`; crypto_major avg `0.6781` n `8`; equity avg `0.1703` n `166`; fx avg `0.0286` n `6`; index avg `0.0527` n `27`; metal avg `0.075` n `20`; unknown avg `384.9655` n `1204`
- 24h: commodity avg `0.1296` n `13`; crypto_alt avg `1.2466` n `239`; crypto_major avg `2.7677` n `8`; equity avg `1.4695` n `166`; fx avg `-0.0744` n `6`; index avg `0.2177` n `27`; metal avg `0.2526` n `20`; unknown avg `184.2757` n `1090`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1172`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
