# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T01:22:38.877119+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0627` n `13`; crypto_alt avg `0.1444` n `239`; crypto_major avg `0.0044` n `8`; equity avg `0.5697` n `168`; fx avg `-0.0269` n `6`; index avg `0.0634` n `27`; metal avg `-0.0179` n `20`; unknown avg `-0.1127` n `1265`
- 1h: commodity avg `-0.0501` n `13`; crypto_alt avg `-0.1328` n `239`; crypto_major avg `-0.384` n `8`; equity avg `0.1398` n `168`; fx avg `-0.067` n `6`; index avg `0.0068` n `27`; metal avg `-0.1058` n `20`; unknown avg `-0.1628` n `1235`
- 4h: commodity avg `-0.0363` n `13`; crypto_alt avg `-0.3736` n `239`; crypto_major avg `-0.6126` n `8`; equity avg `-0.5016` n `168`; fx avg `-0.0023` n `6`; index avg `-0.0665` n `27`; metal avg `-0.2021` n `20`; unknown avg `342.4446` n `1167`
- 24h: commodity avg `0.5954` n `13`; crypto_alt avg `-3.7799` n `239`; crypto_major avg `-3.6748` n `8`; equity avg `-5.3522` n `167`; fx avg `0.1377` n `6`; index avg `-0.5078` n `27`; metal avg `-1.4561` n `20`; unknown avg `442.9095` n `1027`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
