# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T01:07:28.564692+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.0452` n `234`; crypto_major avg `0.0565` n `8`; equity avg `-0.0335` n `140`; fx avg `-0.0262` n `6`; index avg `0.0293` n `26`; metal avg `-0.0238` n `20`; unknown avg `-0.1319` n `940`
- 1h: commodity avg `0.0079` n `12`; crypto_alt avg `0.1087` n `234`; crypto_major avg `0.5791` n `8`; equity avg `0.0` n `140`; fx avg `-0.0411` n `6`; index avg `0.0221` n `26`; metal avg `-0.0265` n `20`; unknown avg `0.2572` n `940`
- 4h: commodity avg `0.2048` n `12`; crypto_alt avg `0.28` n `234`; crypto_major avg `0.0775` n `8`; equity avg `-0.0098` n `140`; fx avg `-0.0441` n `6`; index avg `0.0132` n `26`; metal avg `-0.029` n `20`; unknown avg `25.2811` n `908`
- 24h: commodity avg `0.1393` n `12`; crypto_alt avg `6.2614` n `234`; crypto_major avg `6.5357` n `8`; equity avg `1.4482` n `140`; fx avg `0.1503` n `6`; index avg `0.1473` n `26`; metal avg `0.1379` n `20`; unknown avg `4.097` n `777`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1421`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1348`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
