# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T02:22:26.417151+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.2281` n `228`; crypto_major avg `-0.2094` n `8`; equity avg `0.0108` n `78`; fx avg `0.0015` n `6`; index avg `-0.0008` n `23`; metal avg `-0.0054` n `18`; unknown avg `-0.0373` n `687`
- 1h: commodity avg `0.199` n `12`; crypto_alt avg `-0.4077` n `228`; crypto_major avg `-0.1856` n `8`; equity avg `-0.0408` n `78`; fx avg `0.0019` n `6`; index avg `0.0093` n `23`; metal avg `-0.0019` n `18`; unknown avg `-0.3898` n `679`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `-0.1986` n `228`; crypto_major avg `-0.0937` n `8`; equity avg `0.1674` n `78`; fx avg `0.0222` n `6`; index avg `0.0693` n `23`; metal avg `-0.0217` n `18`; unknown avg `-0.723` n `671`
- 24h: commodity avg `0.4446` n `12`; crypto_alt avg `-3.8046` n `228`; crypto_major avg `-4.5956` n `8`; equity avg `0.8585` n `78`; fx avg `-0.083` n `6`; index avg `0.2774` n `23`; metal avg `-4.1313` n `18`; unknown avg `-0.7076` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0546`, n `668`, weak_sample_signal
