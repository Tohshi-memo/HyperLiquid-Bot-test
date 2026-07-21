# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T06:22:33.853278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `0.0142` n `230`; crypto_major avg `0.0626` n `8`; equity avg `0.0058` n `98`; fx avg `0.0119` n `6`; index avg `-0.0147` n `25`; metal avg `0.084` n `20`; unknown avg `0.0034` n `771`
- 1h: commodity avg `-0.0102` n `12`; crypto_alt avg `0.2769` n `230`; crypto_major avg `0.2283` n `8`; equity avg `0.4606` n `98`; fx avg `-0.0011` n `6`; index avg `0.0918` n `25`; metal avg `0.2476` n `20`; unknown avg `-0.0137` n `755`
- 4h: commodity avg `0.0455` n `12`; crypto_alt avg `1.0488` n `230`; crypto_major avg `0.9545` n `8`; equity avg `1.7485` n `98`; fx avg `-0.0309` n `6`; index avg `0.2235` n `25`; metal avg `0.5108` n `20`; unknown avg `0.0935` n `755`
- 24h: commodity avg `-0.3952` n `12`; crypto_alt avg `3.0945` n `230`; crypto_major avg `2.7039` n `8`; equity avg `1.7942` n `98`; fx avg `-0.0829` n `6`; index avg `0.3229` n `25`; metal avg `0.7035` n `20`; unknown avg `0.1889` n `747`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.079`, n `666`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0747`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.074`, n `666`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0684`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
