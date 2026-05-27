# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T16:07:19.626753+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.086` n `12`; crypto_alt avg `0.0422` n `228`; crypto_major avg `-0.0529` n `8`; equity avg `0.0465` n `67`; fx avg `-0.0131` n `6`; index avg `0.0618` n `23`; metal avg `0.1003` n `18`; unknown avg `-0.2658` n `418`
- 1h: commodity avg `-0.0498` n `12`; crypto_alt avg `0.7116` n `228`; crypto_major avg `0.3404` n `8`; equity avg `-0.1671` n `67`; fx avg `0.0088` n `6`; index avg `-0.0559` n `23`; metal avg `0.0749` n `18`; unknown avg `0.6915` n `418`
- 4h: commodity avg `0.2063` n `12`; crypto_alt avg `1.0655` n `228`; crypto_major avg `-0.1205` n `8`; equity avg `-1.2014` n `67`; fx avg `-0.0347` n `6`; index avg `-0.9999` n `23`; metal avg `0.1451` n `18`; unknown avg `0.787` n `418`
- 24h: commodity avg `-1.0938` n `12`; crypto_alt avg `-0.6183` n `228`; crypto_major avg `-0.7291` n `8`; equity avg `-0.4637` n `67`; fx avg `-0.0569` n `6`; index avg `-0.6051` n `23`; metal avg `-1.0335` n `18`; unknown avg `1.0514` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1702`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
