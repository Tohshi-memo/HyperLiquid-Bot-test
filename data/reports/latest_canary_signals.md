# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T05:07:17.553072+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.059` n `12`; crypto_alt avg `0.0374` n `228`; crypto_major avg `-0.0069` n `8`; equity avg `0.1033` n `66`; fx avg `-0.0035` n `6`; index avg `-0.0286` n `23`; metal avg `-0.0227` n `18`; unknown avg `-0.5039` n `384`
- 1h: commodity avg `-0.1036` n `12`; crypto_alt avg `-0.1398` n `228`; crypto_major avg `-0.1219` n `8`; equity avg `0.2226` n `66`; fx avg `-0.0025` n `6`; index avg `0.0275` n `23`; metal avg `0.0522` n `18`; unknown avg `0.0573` n `384`
- 4h: commodity avg `-0.032` n `12`; crypto_alt avg `0.2509` n `228`; crypto_major avg `0.2707` n `8`; equity avg `0.5435` n `66`; fx avg `0.0323` n `6`; index avg `0.3004` n `23`; metal avg `-0.2865` n `18`; unknown avg `1.0976` n `384`
- 24h: commodity avg `-2.2843` n `12`; crypto_alt avg `3.3994` n `228`; crypto_major avg `3.6214` n `8`; equity avg `2.7238` n `66`; fx avg `0.0151` n `6`; index avg `1.7498` n `23`; metal avg `1.3121` n `18`; unknown avg `5.8793` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0764`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
