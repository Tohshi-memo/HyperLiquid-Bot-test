# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T17:07:16.649932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.85` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0427` n `12`; crypto_alt avg `0.1645` n `228`; crypto_major avg `0.1645` n `8`; equity avg `0.1815` n `67`; fx avg `-0.0007` n `6`; index avg `0.064` n `23`; metal avg `0.0179` n `18`; unknown avg `-0.0563` n `385`
- 1h: commodity avg `-0.0602` n `12`; crypto_alt avg `-0.2033` n `228`; crypto_major avg `-0.3421` n `8`; equity avg `0.104` n `67`; fx avg `0.0069` n `6`; index avg `-0.0203` n `23`; metal avg `-0.2378` n `18`; unknown avg `-0.2798` n `385`
- 4h: commodity avg `-0.3415` n `12`; crypto_alt avg `0.4788` n `228`; crypto_major avg `0.3231` n `8`; equity avg `0.5907` n `67`; fx avg `-0.0417` n `6`; index avg `0.0967` n `23`; metal avg `0.694` n `18`; unknown avg `1.3704` n `385`
- 24h: commodity avg `0.7239` n `12`; crypto_alt avg `1.114` n `228`; crypto_major avg `1.8359` n `8`; equity avg `1.2318` n `66`; fx avg `0.0092` n `6`; index avg `0.2735` n `23`; metal avg `-0.122` n `18`; unknown avg `6.6344` n `374`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0524`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0473`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.046`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
