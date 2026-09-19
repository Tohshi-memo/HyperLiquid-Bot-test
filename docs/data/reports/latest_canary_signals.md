# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T02:37:28.004826+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.1414` n `234`; crypto_major avg `0.1651` n `8`; equity avg `-0.0173` n `140`; fx avg `0.0056` n `6`; index avg `-0.0048` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.1618` n `942`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `1.0729` n `234`; crypto_major avg `0.8232` n `8`; equity avg `0.0082` n `140`; fx avg `-0.0044` n `6`; index avg `-0.016` n `26`; metal avg `0.0039` n `20`; unknown avg `2.1951` n `940`
- 4h: commodity avg `0.1695` n `12`; crypto_alt avg `0.9` n `234`; crypto_major avg `0.6775` n `8`; equity avg `-0.09` n `140`; fx avg `-0.0002` n `6`; index avg `-0.0152` n `26`; metal avg `-0.0383` n `20`; unknown avg `0.9034` n `934`
- 24h: commodity avg `0.1411` n `12`; crypto_alt avg `5.6236` n `234`; crypto_major avg `6.1361` n `8`; equity avg `1.2292` n `140`; fx avg `0.1669` n `6`; index avg `0.1104` n `26`; metal avg `0.1553` n `20`; unknown avg `4.193` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.165`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.139`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1263`, n `668`, weak_sample_signal
