# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T16:07:30.485413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `0.1769` n `236`; crypto_major avg `0.1085` n `8`; equity avg `-0.0316` n `151`; fx avg `-0.0004` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0091` n `20`; unknown avg `-0.4763` n `1185`
- 1h: commodity avg `0.031` n `13`; crypto_alt avg `-0.5247` n `236`; crypto_major avg `-0.4524` n `8`; equity avg `-0.2518` n `151`; fx avg `-0.0091` n `6`; index avg `-0.0425` n `26`; metal avg `-0.0204` n `20`; unknown avg `-0.0988` n `1185`
- 4h: commodity avg `0.0685` n `13`; crypto_alt avg `-1.1519` n `236`; crypto_major avg `-0.5687` n `8`; equity avg `-0.3354` n `151`; fx avg `-0.0216` n `6`; index avg `-0.0585` n `26`; metal avg `-0.0417` n `20`; unknown avg `3.7006` n `1167`
- 24h: commodity avg `0.5085` n `13`; crypto_alt avg `-2.3249` n `236`; crypto_major avg `-0.6389` n `8`; equity avg `-1.4723` n `151`; fx avg `0.0042` n `6`; index avg `-0.2812` n `26`; metal avg `-0.0775` n `20`; unknown avg `3.4783` n `1056`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1713`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.146`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1147`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1122`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0714`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
