# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T06:37:25.763207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.1488` n `228`; crypto_major avg `0.181` n `8`; equity avg `0.0525` n `78`; fx avg `-0.0005` n `6`; index avg `-0.0113` n `23`; metal avg `0.0405` n `18`; unknown avg `-0.0844` n `702`
- 1h: commodity avg `-0.0052` n `12`; crypto_alt avg `0.1641` n `228`; crypto_major avg `0.092` n `8`; equity avg `0.0531` n `78`; fx avg `-0.0012` n `6`; index avg `-0.0099` n `23`; metal avg `0.0587` n `18`; unknown avg `-0.4123` n `670`
- 4h: commodity avg `0.0043` n `12`; crypto_alt avg `0.1427` n `228`; crypto_major avg `-0.1225` n `8`; equity avg `0.1948` n `78`; fx avg `-0.0007` n `6`; index avg `0.0105` n `23`; metal avg `0.0702` n `18`; unknown avg `0.1247` n `662`
- 24h: commodity avg `0.1282` n `12`; crypto_alt avg `1.0032` n `228`; crypto_major avg `0.1095` n `8`; equity avg `0.216` n `78`; fx avg `0.0621` n `6`; index avg `-0.0241` n `23`; metal avg `0.0235` n `18`; unknown avg `-0.2673` n `533`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0628`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0589`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0571`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0516`, n `668`, weak_sample_signal
