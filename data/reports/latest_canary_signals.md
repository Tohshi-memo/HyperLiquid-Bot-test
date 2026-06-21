# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T13:22:29.049066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.045` n `12`; crypto_alt avg `0.0538` n `228`; crypto_major avg `0.047` n `8`; equity avg `0.0031` n `78`; fx avg `-0.0167` n `6`; index avg `0.0007` n `23`; metal avg `0.0012` n `18`; unknown avg `0.0574` n `702`
- 1h: commodity avg `-0.2071` n `12`; crypto_alt avg `0.4406` n `228`; crypto_major avg `0.4185` n `8`; equity avg `0.0526` n `78`; fx avg `-0.065` n `6`; index avg `-0.0069` n `23`; metal avg `0.0196` n `18`; unknown avg `0.1957` n `702`
- 4h: commodity avg `-0.0665` n `12`; crypto_alt avg `0.3981` n `228`; crypto_major avg `-0.0154` n `8`; equity avg `-0.007` n `78`; fx avg `-0.0759` n `6`; index avg `-0.0121` n `23`; metal avg `-0.0367` n `18`; unknown avg `0.1126` n `702`
- 24h: commodity avg `-0.3105` n `12`; crypto_alt avg `2.0709` n `228`; crypto_major avg `0.2554` n `8`; equity avg `0.5774` n `78`; fx avg `-0.0461` n `6`; index avg `0.0215` n `23`; metal avg `-0.0393` n `18`; unknown avg `0.7513` n `653`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.055`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0543`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0529`, n `668`, weak_sample_signal
