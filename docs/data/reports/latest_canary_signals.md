# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-19T09:37:23.379296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `12`; crypto_alt avg `0.0969` n `230`; crypto_major avg `0.0665` n `8`; equity avg `-0.0321` n `96`; fx avg `0.0008` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0014` n `20`; unknown avg `0.005` n `770`
- 1h: commodity avg `0.0213` n `12`; crypto_alt avg `-0.0247` n `230`; crypto_major avg `0.0059` n `8`; equity avg `-0.069` n `96`; fx avg `-0.0077` n `6`; index avg `0.0096` n `25`; metal avg `-0.0262` n `20`; unknown avg `-0.0098` n `770`
- 4h: commodity avg `0.0636` n `12`; crypto_alt avg `0.0365` n `230`; crypto_major avg `0.1432` n `8`; equity avg `0.0765` n `96`; fx avg `-0.0027` n `6`; index avg `0.0402` n `25`; metal avg `-0.0443` n `20`; unknown avg `0.0234` n `752`
- 24h: commodity avg `0.3113` n `12`; crypto_alt avg `0.6211` n `230`; crypto_major avg `1.2239` n `8`; equity avg `0.2138` n `96`; fx avg `-0.0176` n `6`; index avg `-0.0175` n `25`; metal avg `-0.0828` n `20`; unknown avg `0.0514` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0885`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
