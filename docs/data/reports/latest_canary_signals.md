# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T09:22:26.439877+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0691` n `12`; crypto_alt avg `-0.0091` n `230`; crypto_major avg `0.0603` n `8`; equity avg `0.0314` n `98`; fx avg `0.0044` n `6`; index avg `0.0186` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0051` n `771`
- 1h: commodity avg `0.1229` n `12`; crypto_alt avg `-0.1527` n `230`; crypto_major avg `-0.126` n `8`; equity avg `0.2261` n `98`; fx avg `-0.0322` n `6`; index avg `0.0445` n `25`; metal avg `0.0345` n `20`; unknown avg `0.0365` n `771`
- 4h: commodity avg `0.0502` n `12`; crypto_alt avg `0.1482` n `230`; crypto_major avg `0.454` n `8`; equity avg `1.0802` n `98`; fx avg `0.0261` n `6`; index avg `0.1721` n `25`; metal avg `0.3716` n `20`; unknown avg `0.0314` n `755`
- 24h: commodity avg `0.2871` n `12`; crypto_alt avg `2.3185` n `230`; crypto_major avg `2.7194` n `8`; equity avg `2.0104` n `98`; fx avg `-0.0737` n `6`; index avg `0.316` n `25`; metal avg `0.6583` n `20`; unknown avg `0.1837` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0823`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `666`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
