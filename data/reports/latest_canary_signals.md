# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T03:37:26.925328+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `-0.1284` n `234`; crypto_major avg `-0.1099` n `8`; equity avg `-0.0087` n `140`; fx avg `0.0046` n `6`; index avg `0.0344` n `26`; metal avg `-0.0126` n `20`; unknown avg `-0.0623` n `940`
- 1h: commodity avg `-0.001` n `12`; crypto_alt avg `-0.1538` n `234`; crypto_major avg `-0.3978` n `8`; equity avg `-0.0277` n `140`; fx avg `0.0019` n `6`; index avg `0.022` n `26`; metal avg `0.0001` n `20`; unknown avg `2.3115` n `938`
- 4h: commodity avg `0.085` n `12`; crypto_alt avg `0.5659` n `234`; crypto_major avg `0.4751` n `8`; equity avg `-0.1031` n `140`; fx avg `-0.0085` n `6`; index avg `0.0034` n `26`; metal avg `-0.0387` n `20`; unknown avg `0.4583` n `932`
- 24h: commodity avg `0.1332` n `12`; crypto_alt avg `4.3919` n `234`; crypto_major avg `5.1505` n `8`; equity avg `0.786` n `140`; fx avg `0.045` n `6`; index avg `0.0609` n `26`; metal avg `0.1286` n `20`; unknown avg `3.9918` n `785`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.167`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1492`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
