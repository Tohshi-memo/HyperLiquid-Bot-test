# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T09:37:26.399754+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `0.0921` n `228`; crypto_major avg `0.2255` n `8`; equity avg `-0.0406` n `78`; fx avg `0.2883` n `6`; index avg `0.0005` n `23`; metal avg `-0.0044` n `18`; unknown avg `-0.0306` n `687`
- 1h: commodity avg `-0.0101` n `12`; crypto_alt avg `0.3674` n `228`; crypto_major avg `0.3032` n `8`; equity avg `-0.1061` n `78`; fx avg `0.008` n `6`; index avg `-0.0077` n `23`; metal avg `-0.0136` n `18`; unknown avg `-0.0775` n `687`
- 4h: commodity avg `0.0191` n `12`; crypto_alt avg `0.3824` n `228`; crypto_major avg `0.3135` n `8`; equity avg `-0.0767` n `78`; fx avg `0.312` n `6`; index avg `-0.0336` n `23`; metal avg `-0.0059` n `18`; unknown avg `-0.1022` n `639`
- 24h: commodity avg `0.514` n `12`; crypto_alt avg `-2.8812` n `228`; crypto_major avg `-3.2874` n `8`; equity avg `1.2008` n `78`; fx avg `-0.0919` n `6`; index avg `0.2974` n `23`; metal avg `-4.1085` n `18`; unknown avg `0.007` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
