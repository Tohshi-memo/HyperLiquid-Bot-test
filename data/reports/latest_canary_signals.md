# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-15T11:52:29.408485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0353` n `12`; crypto_alt avg `0.0279` n `230`; crypto_major avg `0.0633` n `8`; equity avg `-0.0004` n `93`; fx avg `-0.0017` n `6`; index avg `-0.0062` n `25`; metal avg `0.0359` n `20`; unknown avg `0.0569` n `767`
- 1h: commodity avg `-0.1245` n `12`; crypto_alt avg `0.105` n `230`; crypto_major avg `0.1591` n `8`; equity avg `-0.0038` n `93`; fx avg `0.02` n `6`; index avg `-0.0039` n `25`; metal avg `0.0576` n `20`; unknown avg `0.0549` n `767`
- 4h: commodity avg `-0.1517` n `12`; crypto_alt avg `0.3454` n `230`; crypto_major avg `0.4307` n `8`; equity avg `-0.2213` n `93`; fx avg `-0.0036` n `6`; index avg `-0.0629` n `25`; metal avg `-0.0237` n `20`; unknown avg `-0.0227` n `767`
- 24h: commodity avg `-0.0487` n `12`; crypto_alt avg `1.6737` n `230`; crypto_major avg `3.0199` n `8`; equity avg `1.3137` n `92`; fx avg `0.0095` n `6`; index avg `0.3091` n `25`; metal avg `0.2481` n `20`; unknown avg `0.2553` n `738`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
