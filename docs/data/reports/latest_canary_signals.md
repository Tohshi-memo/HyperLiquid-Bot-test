# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T01:22:14.216420+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `0.215` n `228`; crypto_major avg `0.2059` n `8`; equity avg `0.2966` n `66`; fx avg `0.0092` n `6`; index avg `0.0501` n `23`; metal avg `0.2213` n `18`; unknown avg `0.1578` n `384`
- 1h: commodity avg `0.0697` n `12`; crypto_alt avg `0.4168` n `228`; crypto_major avg `0.4114` n `8`; equity avg `0.6437` n `66`; fx avg `-0.0175` n `6`; index avg `0.2436` n `23`; metal avg `0.3187` n `18`; unknown avg `-0.0036` n `384`
- 4h: commodity avg `-0.1317` n `12`; crypto_alt avg `-0.417` n `228`; crypto_major avg `-0.4176` n `8`; equity avg `0.0348` n `66`; fx avg `0.0076` n `6`; index avg `-0.0848` n `23`; metal avg `0.3119` n `18`; unknown avg `-0.5376` n `383`
- 24h: commodity avg `0.688` n `12`; crypto_alt avg `-1.027` n `228`; crypto_major avg `-0.7599` n `8`; equity avg `0.4369` n `66`; fx avg `-0.0643` n `6`; index avg `-0.4464` n `23`; metal avg `-2.0904` n `18`; unknown avg `0.4451` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0458`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.045`, n `668`, weak_sample_signal
