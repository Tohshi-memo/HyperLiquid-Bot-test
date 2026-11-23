# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T03:52:33.012632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.012` n `13`; crypto_alt avg `-0.3831` n `239`; crypto_major avg `-0.5147` n `8`; equity avg `-0.3654` n `166`; fx avg `0.036` n `6`; index avg `-0.0486` n `27`; metal avg `-0.0691` n `20`; unknown avg `0.2028` n `1264`
- 1h: commodity avg `0.0631` n `13`; crypto_alt avg `1.112` n `239`; crypto_major avg `1.1539` n `8`; equity avg `1.1196` n `166`; fx avg `0.0344` n `6`; index avg `0.1126` n `27`; metal avg `0.2067` n `20`; unknown avg `-0.1386` n `1253`
- 4h: commodity avg `0.0332` n `13`; crypto_alt avg `0.0717` n `239`; crypto_major avg `0.0654` n `8`; equity avg `0.331` n `166`; fx avg `0.1396` n `6`; index avg `-0.0155` n `27`; metal avg `-0.1031` n `20`; unknown avg `-0.3579` n `1239`
- 24h: commodity avg `-0.3485` n `13`; crypto_alt avg `1.9152` n `239`; crypto_major avg `2.5806` n `8`; equity avg `1.8954` n `166`; fx avg `0.2257` n `6`; index avg `0.1836` n `27`; metal avg `0.389` n `20`; unknown avg `244.8593` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1397`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
