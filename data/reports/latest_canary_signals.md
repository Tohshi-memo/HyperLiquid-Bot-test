# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T15:52:28.235959+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `13`; crypto_alt avg `0.1801` n `239`; crypto_major avg `0.1496` n `8`; equity avg `0.0955` n `168`; fx avg `0.0038` n `6`; index avg `0.0057` n `27`; metal avg `-0.02` n `20`; unknown avg `194.7527` n `1267`
- 1h: commodity avg `0.0912` n `13`; crypto_alt avg `-0.2266` n `239`; crypto_major avg `-0.3393` n `8`; equity avg `-0.0116` n `168`; fx avg `0.0073` n `6`; index avg `-0.0013` n `27`; metal avg `-0.0324` n `20`; unknown avg `0.9551` n `1263`
- 4h: commodity avg `0.1253` n `13`; crypto_alt avg `-0.6023` n `239`; crypto_major avg `-0.4185` n `8`; equity avg `-0.0118` n `168`; fx avg `0.0055` n `6`; index avg `-0.0122` n `27`; metal avg `0.0349` n `20`; unknown avg `2.0566` n `1253`
- 24h: commodity avg `0.2305` n `13`; crypto_alt avg `4.233` n `239`; crypto_major avg `3.3689` n `8`; equity avg `6.1181` n `168`; fx avg `0.0662` n `6`; index avg `0.5721` n `27`; metal avg `1.424` n `20`; unknown avg `26.8827` n `1062`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1023`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0793`, n `668`, weak_sample_signal
