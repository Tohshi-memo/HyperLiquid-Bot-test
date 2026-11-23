# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T11:07:29.945802+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0349` n `13`; crypto_alt avg `-0.1233` n `239`; crypto_major avg `-0.0842` n `8`; equity avg `-0.0798` n `166`; fx avg `-0.0095` n `6`; index avg `-0.0158` n `27`; metal avg `-0.0099` n `20`; unknown avg `-0.1201` n `1256`
- 1h: commodity avg `-0.2097` n `13`; crypto_alt avg `-0.069` n `239`; crypto_major avg `0.1113` n `8`; equity avg `-0.0465` n `166`; fx avg `-0.0192` n `6`; index avg `0.0256` n `27`; metal avg `0.0355` n `20`; unknown avg `-0.159` n `1262`
- 4h: commodity avg `-0.3238` n `13`; crypto_alt avg `0.0055` n `239`; crypto_major avg `0.1923` n `8`; equity avg `0.8796` n `166`; fx avg `-0.0395` n `6`; index avg `0.1098` n `27`; metal avg `-0.0335` n `20`; unknown avg `442.8496` n `1112`
- 24h: commodity avg `-0.9378` n `13`; crypto_alt avg `0.5385` n `239`; crypto_major avg `0.9388` n `8`; equity avg `2.1378` n `166`; fx avg `0.1947` n `6`; index avg `0.128` n `27`; metal avg `0.4143` n `20`; unknown avg `0.0036` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1542`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1539`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1295`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
