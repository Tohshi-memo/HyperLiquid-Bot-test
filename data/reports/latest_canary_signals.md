# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T05:07:30.505640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.021` n `12`; crypto_alt avg `0.2671` n `228`; crypto_major avg `0.2163` n `8`; equity avg `0.0545` n `78`; fx avg `0.015` n `6`; index avg `-0.0097` n `23`; metal avg `0.0007` n `18`; unknown avg `0.2358` n `687`
- 1h: commodity avg `-0.0112` n `12`; crypto_alt avg `0.5175` n `228`; crypto_major avg `0.7339` n `8`; equity avg `0.1461` n `78`; fx avg `-0.0123` n `6`; index avg `0.0073` n `23`; metal avg `0.027` n `18`; unknown avg `0.1728` n `687`
- 4h: commodity avg `0.1568` n `12`; crypto_alt avg `0.3108` n `228`; crypto_major avg `0.7853` n `8`; equity avg `0.3058` n `78`; fx avg `-0.0219` n `6`; index avg `0.024` n `23`; metal avg `0.0015` n `18`; unknown avg `0.1173` n `679`
- 24h: commodity avg `0.4233` n `12`; crypto_alt avg `-3.1919` n `228`; crypto_major avg `-3.7598` n `8`; equity avg `1.2128` n `78`; fx avg `-0.1068` n `6`; index avg `0.2967` n `23`; metal avg `-4.1147` n `18`; unknown avg `-0.5026` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0583`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
