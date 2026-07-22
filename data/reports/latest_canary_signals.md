# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T17:37:26.731498+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `12`; crypto_alt avg `0.0092` n `230`; crypto_major avg `0.1236` n `8`; equity avg `-0.0904` n `98`; fx avg `-0.0008` n `6`; index avg `-0.0091` n `25`; metal avg `-0.0272` n `20`; unknown avg `0.0307` n `773`
- 1h: commodity avg `0.097` n `12`; crypto_alt avg `-0.1396` n `230`; crypto_major avg `-0.2135` n `8`; equity avg `-0.2022` n `98`; fx avg `0.0085` n `6`; index avg `-0.0154` n `25`; metal avg `-0.0692` n `20`; unknown avg `0.0948` n `773`
- 4h: commodity avg `0.1512` n `12`; crypto_alt avg `0.2634` n `230`; crypto_major avg `0.4392` n `8`; equity avg `0.3954` n `98`; fx avg `-0.037` n `6`; index avg `0.1616` n `25`; metal avg `-0.0537` n `20`; unknown avg `-0.0013` n `773`
- 24h: commodity avg `0.6129` n `12`; crypto_alt avg `0.0661` n `230`; crypto_major avg `-0.4531` n `8`; equity avg `-0.3009` n `98`; fx avg `-0.0404` n `6`; index avg `-0.0704` n `25`; metal avg `0.3574` n `20`; unknown avg `0.9474` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.104`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0881`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.085`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0804`, n `666`, weak_sample_signal
