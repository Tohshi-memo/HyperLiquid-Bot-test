# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T22:52:24.031259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.015` n `12`; crypto_alt avg `0.1482` n `230`; crypto_major avg `0.0448` n `8`; equity avg `0.0598` n `98`; fx avg `-0.0007` n `6`; index avg `-0.0044` n `25`; metal avg `0.0302` n `20`; unknown avg `0.4952` n `769`
- 1h: commodity avg `0.0435` n `12`; crypto_alt avg `0.5617` n `230`; crypto_major avg `0.3402` n `8`; equity avg `0.1805` n `98`; fx avg `-0.0648` n `6`; index avg `0.0367` n `25`; metal avg `-0.0862` n `20`; unknown avg `1.5013` n `769`
- 4h: commodity avg `0.034` n `12`; crypto_alt avg `0.643` n `230`; crypto_major avg `0.4869` n `8`; equity avg `0.2715` n `98`; fx avg `0.0142` n `6`; index avg `0.0641` n `25`; metal avg `-0.0951` n `20`; unknown avg `0.8896` n `769`
- 24h: commodity avg `-0.0154` n `12`; crypto_alt avg `0.0502` n `230`; crypto_major avg `0.228` n `8`; equity avg `0.6212` n `97`; fx avg `0.0778` n `6`; index avg `0.0076` n `25`; metal avg `-0.0757` n `20`; unknown avg `-0.1025` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1473`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1411`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1376`, n `666`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1279`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1087`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0988`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0959`, n `666`, weak_sample_signal
