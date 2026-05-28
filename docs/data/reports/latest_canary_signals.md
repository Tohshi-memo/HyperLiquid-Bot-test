# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T10:52:18.069836+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1982` n `12`; crypto_alt avg `-0.3658` n `228`; crypto_major avg `-0.245` n `8`; equity avg `-0.0844` n `67`; fx avg `-0.0105` n `6`; index avg `-0.072` n `23`; metal avg `-0.1561` n `18`; unknown avg `0.0287` n `419`
- 1h: commodity avg `0.3846` n `12`; crypto_alt avg `-0.6605` n `228`; crypto_major avg `-0.3812` n `8`; equity avg `-0.3027` n `67`; fx avg `-0.024` n `6`; index avg `-0.1846` n `23`; metal avg `-0.3614` n `18`; unknown avg `0.0661` n `419`
- 4h: commodity avg `0.1417` n `12`; crypto_alt avg `-0.2925` n `228`; crypto_major avg `-0.0042` n `8`; equity avg `0.0025` n `67`; fx avg `-0.0263` n `6`; index avg `-0.16` n `23`; metal avg `-0.2619` n `18`; unknown avg `0.1237` n `419`
- 24h: commodity avg `0.5694` n `12`; crypto_alt avg `-5.0305` n `228`; crypto_major avg `-3.839` n `8`; equity avg `-1.7795` n `67`; fx avg `-0.0949` n `6`; index avg `-1.2027` n `23`; metal avg `-1.2662` n `18`; unknown avg `-1.2775` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1843`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1742`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1719`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1521`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
