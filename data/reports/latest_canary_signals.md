# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T00:59:19.123015+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.4493` n `230`; crypto_major avg `-0.3872` n `8`; equity avg `-0.4361` n `98`; fx avg `-0.0193` n `6`; index avg `-0.0923` n `25`; metal avg `0.0457` n `20`; unknown avg `0.1804` n `769`
- 1h: commodity avg `-0.0399` n `12`; crypto_alt avg `0.1163` n `230`; crypto_major avg `-0.0666` n `8`; equity avg `0.2238` n `98`; fx avg `-0.0261` n `6`; index avg `0.101` n `25`; metal avg `0.1797` n `20`; unknown avg `0.0811` n `769`
- 4h: commodity avg `-0.1011` n `12`; crypto_alt avg `0.1531` n `230`; crypto_major avg `0.0427` n `8`; equity avg `0.3179` n `98`; fx avg `-0.0685` n `6`; index avg `0.0963` n `25`; metal avg `0.0754` n `20`; unknown avg `-0.0632` n `767`
- 24h: commodity avg `-0.1093` n `12`; crypto_alt avg `0.0251` n `230`; crypto_major avg `0.1847` n `8`; equity avg `0.5727` n `97`; fx avg `0.0234` n `6`; index avg `0.0851` n `25`; metal avg `0.0618` n `20`; unknown avg `0.0915` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1075`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0982`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0974`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
