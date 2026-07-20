# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T02:07:30.712012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0212` n `12`; crypto_alt avg `-0.0749` n `230`; crypto_major avg `-0.0611` n `8`; equity avg `0.0992` n `98`; fx avg `-0.0001` n `6`; index avg `0.0172` n `25`; metal avg `0.0693` n `20`; unknown avg `-0.1053` n `769`
- 1h: commodity avg `0.0338` n `12`; crypto_alt avg `0.2353` n `230`; crypto_major avg `0.2791` n `8`; equity avg `-0.1914` n `98`; fx avg `-0.0204` n `6`; index avg `-0.0084` n `25`; metal avg `-0.0098` n `20`; unknown avg `-0.0866` n `769`
- 4h: commodity avg `-0.0972` n `12`; crypto_alt avg `0.7044` n `230`; crypto_major avg `0.655` n `8`; equity avg `0.2373` n `98`; fx avg `-0.039` n `6`; index avg `0.1193` n `25`; metal avg `0.1868` n `20`; unknown avg `0.3495` n `767`
- 24h: commodity avg `-0.0439` n `12`; crypto_alt avg `0.0377` n `230`; crypto_major avg `0.1172` n `8`; equity avg `0.2797` n `97`; fx avg `-0.019` n `6`; index avg `0.0921` n `25`; metal avg `0.0228` n `20`; unknown avg `0.0491` n `749`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1465`, n `670`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1207`, n `670`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1142`, n `670`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.105`, n `670`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
