# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T02:07:15.732352+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1533` n `12`; crypto_alt avg `-0.1608` n `228`; crypto_major avg `-0.0815` n `8`; equity avg `0.122` n `67`; fx avg `-0.0129` n `6`; index avg `0.0647` n `23`; metal avg `0.1843` n `18`; unknown avg `-0.1049` n `407`
- 1h: commodity avg `-0.0803` n `12`; crypto_alt avg `-0.3483` n `228`; crypto_major avg `-0.3014` n `8`; equity avg `-0.1094` n `67`; fx avg `-0.0331` n `6`; index avg `0.0017` n `23`; metal avg `-0.3248` n `18`; unknown avg `0.4365` n `407`
- 4h: commodity avg `0.4498` n `12`; crypto_alt avg `-1.8649` n `228`; crypto_major avg `-1.3252` n `8`; equity avg `-0.9576` n `67`; fx avg `-0.1062` n `6`; index avg `-0.3436` n `23`; metal avg `-0.9667` n `18`; unknown avg `2.6069` n `405`
- 24h: commodity avg `0.0032` n `12`; crypto_alt avg `-0.5251` n `228`; crypto_major avg `-1.3376` n `8`; equity avg `-0.3698` n `67`; fx avg `-0.0427` n `6`; index avg `0.0905` n `23`; metal avg `-0.4341` n `18`; unknown avg `1.0332` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1696`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.125`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
