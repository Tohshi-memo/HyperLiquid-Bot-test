# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T07:07:31.262163+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.85` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1637` n `12`; crypto_alt avg `-0.147` n `228`; crypto_major avg `-0.0768` n `8`; equity avg `-0.0148` n `74`; fx avg `-0.0036` n `6`; index avg `0.0317` n `23`; metal avg `0.0128` n `16`; unknown avg `0.0` n `674`
- 1h: commodity avg `-0.3238` n `12`; crypto_alt avg `-0.2555` n `228`; crypto_major avg `-0.0681` n `8`; equity avg `0.0325` n `74`; fx avg `0.01` n `6`; index avg `0.0243` n `23`; metal avg `0.0464` n `16`; unknown avg `-0.0527` n `674`
- 4h: commodity avg `-0.0086` n `12`; crypto_alt avg `0.3063` n `228`; crypto_major avg `0.1694` n `8`; equity avg `0.0967` n `74`; fx avg `0.0224` n `6`; index avg `0.205` n `23`; metal avg `-0.3788` n `16`; unknown avg `-0.1137` n `514`
- 24h: commodity avg `-1.0041` n `12`; crypto_alt avg `3.1036` n `228`; crypto_major avg `3.0411` n `8`; equity avg `1.8182` n `74`; fx avg `0.0393` n `6`; index avg `0.979` n `23`; metal avg `1.5659` n `16`; unknown avg `1.7055` n `514`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
