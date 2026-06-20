# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T22:52:28.327948+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0049` n `12`; crypto_alt avg `0.1004` n `228`; crypto_major avg `-0.0005` n `8`; equity avg `0.0167` n `78`; fx avg `-0.0369` n `6`; index avg `0.0044` n `23`; metal avg `-0.0123` n `18`; unknown avg `0.6709` n `701`
- 1h: commodity avg `-0.006` n `12`; crypto_alt avg `0.5951` n `228`; crypto_major avg `0.6096` n `8`; equity avg `0.1095` n `78`; fx avg `-0.0253` n `6`; index avg `0.0371` n `23`; metal avg `0.0281` n `18`; unknown avg `0.7922` n `701`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `0.7123` n `228`; crypto_major avg `1.0013` n `8`; equity avg `0.3084` n `78`; fx avg `-0.034` n `6`; index avg `0.0459` n `23`; metal avg `0.019` n `18`; unknown avg `0.0573` n `701`
- 24h: commodity avg `0.1711` n `12`; crypto_alt avg `1.3547` n `228`; crypto_major avg `1.83` n `8`; equity avg `0.5317` n `78`; fx avg `0.0275` n `6`; index avg `0.1047` n `23`; metal avg `-0.0677` n `18`; unknown avg `-0.3521` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
