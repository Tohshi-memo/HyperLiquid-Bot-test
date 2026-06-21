# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T01:52:25.285889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0177` n `12`; crypto_alt avg `0.0187` n `228`; crypto_major avg `0.0562` n `8`; equity avg `0.0241` n `78`; fx avg `0.0074` n `6`; index avg `-0.0049` n `23`; metal avg `0.0193` n `18`; unknown avg `-0.0829` n `702`
- 1h: commodity avg `-0.0386` n `12`; crypto_alt avg `0.263` n `228`; crypto_major avg `0.0979` n `8`; equity avg `0.0518` n `78`; fx avg `0.0059` n `6`; index avg `0.0046` n `23`; metal avg `0.0118` n `18`; unknown avg `0.3774` n `701`
- 4h: commodity avg `0.0088` n `12`; crypto_alt avg `0.8947` n `228`; crypto_major avg `0.429` n `8`; equity avg `0.1303` n `78`; fx avg `0.0139` n `6`; index avg `0.0047` n `23`; metal avg `0.0021` n `18`; unknown avg `1.6501` n `701`
- 24h: commodity avg `0.3303` n `12`; crypto_alt avg `1.4601` n `228`; crypto_major avg `1.493` n `8`; equity avg `0.4959` n `78`; fx avg `0.0553` n `6`; index avg `0.0168` n `23`; metal avg `-0.0286` n `18`; unknown avg `1.4079` n `557`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0544`, n `668`, weak_sample_signal
