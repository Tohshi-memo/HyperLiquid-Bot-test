# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T10:07:30.412069+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0979` n `12`; crypto_alt avg `-0.3576` n `234`; crypto_major avg `-0.2068` n `8`; equity avg `0.1505` n `140`; fx avg `-0.0075` n `6`; index avg `0.0269` n `26`; metal avg `0.0005` n `20`; unknown avg `0.0906` n `942`
- 1h: commodity avg `-0.3085` n `12`; crypto_alt avg `-0.17` n `234`; crypto_major avg `0.1394` n `8`; equity avg `0.4882` n `140`; fx avg `-0.0343` n `6`; index avg `0.0921` n `26`; metal avg `0.0751` n `20`; unknown avg `6.928` n `942`
- 4h: commodity avg `-0.7247` n `12`; crypto_alt avg `0.1656` n `234`; crypto_major avg `0.4433` n `8`; equity avg `0.4532` n `140`; fx avg `-0.1156` n `6`; index avg `0.0623` n `26`; metal avg `0.0953` n `20`; unknown avg `6.8657` n `932`
- 24h: commodity avg `-0.7373` n `12`; crypto_alt avg `1.0527` n `234`; crypto_major avg `1.8868` n `8`; equity avg `1.1149` n `140`; fx avg `-0.2839` n `6`; index avg `0.3027` n `26`; metal avg `-0.1024` n `20`; unknown avg `1130.6438` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1368`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
