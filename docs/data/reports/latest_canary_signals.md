# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T11:37:34.626989+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0253` n `13`; crypto_alt avg `-0.3026` n `239`; crypto_major avg `-0.3326` n `8`; equity avg `-0.3996` n `168`; fx avg `-0.0134` n `6`; index avg `-0.0647` n `27`; metal avg `-0.1619` n `20`; unknown avg `113.1043` n `1265`
- 1h: commodity avg `0.0853` n `13`; crypto_alt avg `-0.5753` n `239`; crypto_major avg `-0.4809` n `8`; equity avg `-0.2952` n `168`; fx avg `-0.0061` n `6`; index avg `-0.0802` n `27`; metal avg `-0.1512` n `20`; unknown avg `85.3614` n `1195`
- 4h: commodity avg `0.3712` n `13`; crypto_alt avg `-0.368` n `239`; crypto_major avg `-0.2198` n `8`; equity avg `-0.5093` n `168`; fx avg `0.0354` n `6`; index avg `-0.1255` n `27`; metal avg `-0.122` n `20`; unknown avg `86.7649` n `1175`
- 24h: commodity avg `0.3611` n `13`; crypto_alt avg `-2.1627` n `239`; crypto_major avg `-2.9738` n `8`; equity avg `-4.7061` n `167`; fx avg `-0.0115` n `6`; index avg `-0.4423` n `27`; metal avg `-1.0872` n `20`; unknown avg `482.7229` n `1067`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
