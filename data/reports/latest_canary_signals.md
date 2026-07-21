# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T04:37:25.337642+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0063` n `12`; crypto_alt avg `0.0098` n `230`; crypto_major avg `0.0056` n `8`; equity avg `0.0003` n `98`; fx avg `0.007` n `6`; index avg `0.0055` n `25`; metal avg `0.0076` n `20`; unknown avg `0.0665` n `771`
- 1h: commodity avg `-0.0003` n `12`; crypto_alt avg `0.0476` n `230`; crypto_major avg `0.0066` n `8`; equity avg `0.1658` n `98`; fx avg `-0.0088` n `6`; index avg `0.052` n `25`; metal avg `0.0413` n `20`; unknown avg `0.0017` n `771`
- 4h: commodity avg `-0.0669` n `12`; crypto_alt avg `0.3504` n `230`; crypto_major avg `0.3293` n `8`; equity avg `1.2093` n `98`; fx avg `-0.0107` n `6`; index avg `0.3219` n `25`; metal avg `0.2997` n `20`; unknown avg `0.3733` n `771`
- 24h: commodity avg `-0.3399` n `12`; crypto_alt avg `2.0335` n `230`; crypto_major avg `1.6322` n `8`; equity avg `0.8975` n `98`; fx avg `-0.1251` n `6`; index avg `0.2434` n `25`; metal avg `0.3169` n `20`; unknown avg `0.0457` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0951`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0728`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0719`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
