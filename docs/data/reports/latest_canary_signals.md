# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T13:37:31.030964+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0668` n `12`; crypto_alt avg `-0.5635` n `233`; crypto_major avg `-0.5075` n `8`; equity avg `-0.4721` n `136`; fx avg `-0.0293` n `6`; index avg `-0.0235` n `26`; metal avg `0.0726` n `20`; unknown avg `579.1838` n `796`
- 1h: commodity avg `0.0093` n `12`; crypto_alt avg `-0.4156` n `233`; crypto_major avg `-0.0911` n `8`; equity avg `-0.2084` n `136`; fx avg `-0.0846` n `6`; index avg `0.0612` n `26`; metal avg `0.3126` n `20`; unknown avg `2.7679` n `794`
- 4h: commodity avg `-0.0813` n `12`; crypto_alt avg `0.6301` n `233`; crypto_major avg `1.0615` n `8`; equity avg `0.0611` n `136`; fx avg `-0.113` n `6`; index avg `0.1032` n `26`; metal avg `0.3082` n `20`; unknown avg `0.5241` n `788`
- 24h: commodity avg `-0.1505` n `12`; crypto_alt avg `0.0525` n `233`; crypto_major avg `0.85` n `8`; equity avg `0.2163` n `136`; fx avg `-0.1765` n `6`; index avg `0.2589` n `26`; metal avg `0.1838` n `20`; unknown avg `2.0067` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0683`, n `668`, weak_sample_signal
