# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T10:52:27.551947+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.0524` n `228`; crypto_major avg `-0.0122` n `8`; equity avg `0.0362` n `78`; fx avg `-0.0912` n `6`; index avg `-0.0004` n `23`; metal avg `0.0201` n `18`; unknown avg `0.0742` n `702`
- 1h: commodity avg `-0.0109` n `12`; crypto_alt avg `0.1545` n `228`; crypto_major avg `0.1498` n `8`; equity avg `0.0335` n `78`; fx avg `-0.0887` n `6`; index avg `-0.0004` n `23`; metal avg `0.0197` n `18`; unknown avg `0.0137` n `702`
- 4h: commodity avg `-0.0438` n `12`; crypto_alt avg `0.7578` n `228`; crypto_major avg `0.0654` n `8`; equity avg `-0.0152` n `78`; fx avg `-0.0984` n `6`; index avg `0.0031` n `23`; metal avg `-0.0061` n `18`; unknown avg `-0.154` n `694`
- 24h: commodity avg `0.0712` n `12`; crypto_alt avg `1.6681` n `228`; crypto_major avg `0.1959` n `8`; equity avg `0.3955` n `78`; fx avg `-0.0622` n `6`; index avg `0.0414` n `23`; metal avg `0.0064` n `18`; unknown avg `0.2803` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0573`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
