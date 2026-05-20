# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T02:07:20.914399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `12`; crypto_alt avg `0.1247` n `228`; crypto_major avg `0.1249` n `8`; equity avg `0.1339` n `66`; fx avg `-0.0175` n `6`; index avg `0.0479` n `23`; metal avg `0.0769` n `18`; unknown avg `-0.1223` n `384`
- 1h: commodity avg `-0.2484` n `12`; crypto_alt avg `0.3485` n `228`; crypto_major avg `0.1723` n `8`; equity avg `0.289` n `66`; fx avg `-0.055` n `6`; index avg `0.0609` n `23`; metal avg `-0.0551` n `18`; unknown avg `0.0818` n `384`
- 4h: commodity avg `-0.3466` n `12`; crypto_alt avg `0.167` n `228`; crypto_major avg `-0.0887` n `8`; equity avg `-0.1016` n `66`; fx avg `-0.0609` n `6`; index avg `-0.0742` n `23`; metal avg `-0.044` n `18`; unknown avg `-0.4722` n `383`
- 24h: commodity avg `0.6514` n `12`; crypto_alt avg `-0.6384` n `228`; crypto_major avg `-0.3902` n `8`; equity avg `0.5061` n `66`; fx avg `-0.1259` n `6`; index avg `-0.3385` n `23`; metal avg `-2.1382` n `18`; unknown avg `0.9146` n `363`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0525`, n `668`, weak_sample_signal
