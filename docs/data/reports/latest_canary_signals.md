# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T18:22:36.329206+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0179` n `12`; crypto_alt avg `-0.0118` n `228`; crypto_major avg `0.0396` n `8`; equity avg `0.0052` n `78`; fx avg `-0.0058` n `6`; index avg `0.0105` n `23`; metal avg `0.0093` n `18`; unknown avg `-0.337` n `701`
- 1h: commodity avg `0.0165` n `12`; crypto_alt avg `-0.0495` n `228`; crypto_major avg `-0.0134` n `8`; equity avg `-0.0774` n `78`; fx avg `-0.0008` n `6`; index avg `-0.0009` n `23`; metal avg `-0.0345` n `18`; unknown avg `-0.2841` n `701`
- 4h: commodity avg `-0.1162` n `12`; crypto_alt avg `1.1737` n `228`; crypto_major avg `0.6909` n `8`; equity avg `0.1894` n `78`; fx avg `0.0227` n `6`; index avg `0.0101` n `23`; metal avg `-0.0054` n `18`; unknown avg `1.096` n `701`
- 24h: commodity avg `0.3812` n `12`; crypto_alt avg `0.396` n `228`; crypto_major avg `0.7963` n `8`; equity avg `0.3139` n `78`; fx avg `0.0568` n `6`; index avg `0.0438` n `23`; metal avg `0.1083` n `18`; unknown avg `0.077` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
