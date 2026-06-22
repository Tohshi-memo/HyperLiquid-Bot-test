# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T03:22:26.901693+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0279` n `12`; crypto_alt avg `0.295` n `228`; crypto_major avg `0.4305` n `8`; equity avg `0.2221` n `79`; fx avg `-0.0022` n `6`; index avg `0.0461` n `23`; metal avg `-0.0081` n `18`; unknown avg `5.5926` n `701`
- 1h: commodity avg `0.0569` n `12`; crypto_alt avg `-0.3293` n `228`; crypto_major avg `-0.4241` n `8`; equity avg `-0.1505` n `79`; fx avg `-0.0007` n `6`; index avg `0.0159` n `23`; metal avg `-0.0961` n `18`; unknown avg `1.2155` n `701`
- 4h: commodity avg `-0.3609` n `12`; crypto_alt avg `0.9179` n `228`; crypto_major avg `0.7162` n `8`; equity avg `0.0705` n `79`; fx avg `0.1397` n `6`; index avg `0.1532` n `23`; metal avg `0.2068` n `18`; unknown avg `0.3019` n `685`
- 24h: commodity avg `-0.251` n `12`; crypto_alt avg `0.0266` n `228`; crypto_major avg `-0.7846` n `8`; equity avg `-0.3872` n `79`; fx avg `0.0214` n `6`; index avg `0.0224` n `23`; metal avg `0.1191` n `18`; unknown avg `0.1075` n `629`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0806`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
