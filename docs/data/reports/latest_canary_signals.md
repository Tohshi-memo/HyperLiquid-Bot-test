# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T01:37:20.833854+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1077` n `12`; crypto_alt avg `-0.3481` n `228`; crypto_major avg `-0.446` n `8`; equity avg `-0.3607` n `66`; fx avg `-0.0079` n `6`; index avg `-0.2358` n `23`; metal avg `-0.6974` n `18`; unknown avg `-0.1082` n `384`
- 1h: commodity avg `0.2126` n `12`; crypto_alt avg `-0.1834` n `228`; crypto_major avg `-0.2621` n `8`; equity avg `-0.1484` n `66`; fx avg `-0.0253` n `6`; index avg `-0.2815` n `23`; metal avg `-0.7955` n `18`; unknown avg `-0.279` n `384`
- 4h: commodity avg `0.0453` n `12`; crypto_alt avg `-0.771` n `228`; crypto_major avg `-0.774` n `8`; equity avg `-0.4105` n `66`; fx avg `-0.0022` n `6`; index avg `-0.3561` n `23`; metal avg `-0.4195` n `18`; unknown avg `-0.4931` n `383`
- 24h: commodity avg `0.9133` n `12`; crypto_alt avg `-1.4339` n `228`; crypto_major avg `-1.2826` n `8`; equity avg `-0.2282` n `66`; fx avg `-0.0705` n `6`; index avg `-0.7511` n `23`; metal avg `-2.8587` n `18`; unknown avg `0.5736` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0444`, n `668`, weak_sample_signal
