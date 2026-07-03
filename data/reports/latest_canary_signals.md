# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T08:23:29.771953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `12`; crypto_alt avg `0.0355` n `229`; crypto_major avg `-0.0495` n `8`; equity avg `-0.005` n `88`; fx avg `-0.0125` n `6`; index avg `-0.0144` n `25`; metal avg `-0.0119` n `20`; unknown avg `0.01` n `765`
- 1h: commodity avg `-0.0668` n `12`; crypto_alt avg `0.1664` n `229`; crypto_major avg `0.0404` n `8`; equity avg `0.1075` n `88`; fx avg `0.019` n `6`; index avg `-0.0006` n `25`; metal avg `0.1466` n `20`; unknown avg `0.1084` n `765`
- 4h: commodity avg `-0.0238` n `12`; crypto_alt avg `0.629` n `229`; crypto_major avg `0.6866` n `8`; equity avg `0.3139` n `88`; fx avg `-0.1429` n `6`; index avg `0.119` n `25`; metal avg `0.0403` n `20`; unknown avg `-0.0822` n `743`
- 24h: commodity avg `0.3381` n `12`; crypto_alt avg `2.2473` n `228`; crypto_major avg `3.4769` n `8`; equity avg `0.5305` n `88`; fx avg `-0.1348` n `6`; index avg `0.2538` n `25`; metal avg `1.285` n `20`; unknown avg `5.2559` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
