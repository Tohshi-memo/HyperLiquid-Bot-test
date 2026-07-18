# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-18T22:07:23.063706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0429` n `12`; crypto_alt avg `0.1069` n `230`; crypto_major avg `0.0944` n `8`; equity avg `0.04` n `96`; fx avg `-0.0018` n `6`; index avg `0.0004` n `25`; metal avg `-0.0006` n `20`; unknown avg `0.009` n `770`
- 1h: commodity avg `0.0162` n `12`; crypto_alt avg `0.174` n `230`; crypto_major avg `0.1251` n `8`; equity avg `0.087` n `96`; fx avg `-0.001` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0085` n `20`; unknown avg `0.0206` n `770`
- 4h: commodity avg `0.0917` n `12`; crypto_alt avg `0.1607` n `230`; crypto_major avg `0.3098` n `8`; equity avg `0.0737` n `96`; fx avg `-0.0136` n `6`; index avg `-0.0326` n `25`; metal avg `-0.0144` n `20`; unknown avg `0.2538` n `770`
- 24h: commodity avg `0.3439` n `12`; crypto_alt avg `-0.0483` n `230`; crypto_major avg `0.5883` n `8`; equity avg `-0.1099` n `96`; fx avg `-0.0746` n `6`; index avg `0.0307` n `25`; metal avg `-0.0071` n `20`; unknown avg `0.1811` n `737`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0872`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
