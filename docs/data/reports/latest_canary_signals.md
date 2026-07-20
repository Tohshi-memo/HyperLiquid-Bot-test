# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T13:37:27.454402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1302` n `12`; crypto_alt avg `0.1658` n `230`; crypto_major avg `0.1156` n `8`; equity avg `0.2398` n `98`; fx avg `-0.0075` n `6`; index avg `0.091` n `25`; metal avg `-0.003` n `20`; unknown avg `0.1581` n `770`
- 1h: commodity avg `-0.1788` n `12`; crypto_alt avg `0.0232` n `230`; crypto_major avg `-0.0075` n `8`; equity avg `0.2377` n `98`; fx avg `-0.0201` n `6`; index avg `0.0791` n `25`; metal avg `0.0166` n `20`; unknown avg `0.0667` n `770`
- 4h: commodity avg `0.0643` n `12`; crypto_alt avg `0.6286` n `230`; crypto_major avg `0.6171` n `8`; equity avg `0.788` n `98`; fx avg `-0.0264` n `6`; index avg `0.1953` n `25`; metal avg `-0.0408` n `20`; unknown avg `0.4222` n `770`
- 24h: commodity avg `-0.6123` n `12`; crypto_alt avg `0.8456` n `230`; crypto_major avg `0.4354` n `8`; equity avg `1.1045` n `97`; fx avg `-0.0733` n `6`; index avg `0.2924` n `25`; metal avg `0.1444` n `20`; unknown avg `0.0654` n `745`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1073`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.099`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0882`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0767`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
