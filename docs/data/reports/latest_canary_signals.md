# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T12:52:33.266894+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.1179` n `228`; crypto_major avg `0.1394` n `8`; equity avg `0.046` n `78`; fx avg `-0.1261` n `6`; index avg `-0.0047` n `23`; metal avg `0.0281` n `18`; unknown avg `0.0693` n `702`
- 1h: commodity avg `0.1735` n `12`; crypto_alt avg `0.1935` n `228`; crypto_major avg `-0.0052` n `8`; equity avg `0.0189` n `78`; fx avg `-0.0917` n `6`; index avg `-0.0105` n `23`; metal avg `0.001` n `18`; unknown avg `0.1364` n `702`
- 4h: commodity avg `0.1198` n `12`; crypto_alt avg `0.2454` n `228`; crypto_major avg `0.0468` n `8`; equity avg `0.0013` n `78`; fx avg `-0.0839` n `6`; index avg `-0.0084` n `23`; metal avg `-0.0293` n `18`; unknown avg `-0.104` n `702`
- 24h: commodity avg `0.2894` n `12`; crypto_alt avg `1.5451` n `228`; crypto_major avg `-0.2231` n `8`; equity avg `0.3797` n `78`; fx avg `-0.0701` n `6`; index avg `0.0148` n `23`; metal avg `-0.0761` n `18`; unknown avg `0.164` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0547`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0545`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
