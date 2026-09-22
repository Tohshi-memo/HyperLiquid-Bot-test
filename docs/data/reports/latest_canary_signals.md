# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T11:07:27.060846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.137` n `12`; crypto_alt avg `-0.2705` n `234`; crypto_major avg `-0.1695` n `8`; equity avg `-0.0579` n `140`; fx avg `0.007` n `6`; index avg `-0.0132` n `26`; metal avg `-0.0594` n `20`; unknown avg `0.6124` n `942`
- 1h: commodity avg `0.0851` n `12`; crypto_alt avg `-0.522` n `234`; crypto_major avg `-0.2677` n `8`; equity avg `-0.0569` n `140`; fx avg `0.0216` n `6`; index avg `-0.0225` n `26`; metal avg `-0.019` n `20`; unknown avg `0.7346` n `940`
- 4h: commodity avg `-0.5823` n `12`; crypto_alt avg `-0.6875` n `234`; crypto_major avg `-0.0599` n `8`; equity avg `0.4937` n `140`; fx avg `-0.1016` n `6`; index avg `0.0699` n `26`; metal avg `0.0838` n `20`; unknown avg `3.6089` n `934`
- 24h: commodity avg `-0.5888` n `12`; crypto_alt avg `-0.3793` n `234`; crypto_major avg `1.1358` n `8`; equity avg `1.0933` n `140`; fx avg `-0.2626` n `6`; index avg `0.2743` n `26`; metal avg `-0.0621` n `20`; unknown avg `1125.2359` n `790`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1482`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
