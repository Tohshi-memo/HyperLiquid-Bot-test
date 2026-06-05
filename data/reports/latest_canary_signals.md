# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T14:52:26.381579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0905` n `12`; crypto_alt avg `-0.5352` n `228`; crypto_major avg `-0.7876` n `8`; equity avg `-0.2348` n `74`; fx avg `-0.0004` n `6`; index avg `-0.0992` n `23`; metal avg `-0.0698` n `18`; unknown avg `0.5169` n `424`
- 1h: commodity avg `-0.3471` n `12`; crypto_alt avg `-0.3676` n `228`; crypto_major avg `-0.3842` n `8`; equity avg `0.1125` n `74`; fx avg `-0.0646` n `6`; index avg `-0.004` n `23`; metal avg `-0.9603` n `18`; unknown avg `-0.701` n `424`
- 4h: commodity avg `-0.8323` n `12`; crypto_alt avg `-1.1019` n `228`; crypto_major avg `-1.6527` n `8`; equity avg `-2.3549` n `74`; fx avg `-0.1234` n `6`; index avg `-1.4757` n `23`; metal avg `-2.6536` n `18`; unknown avg `0.858` n `424`
- 24h: commodity avg `-0.9137` n `12`; crypto_alt avg `-6.7732` n `228`; crypto_major avg `-5.5221` n `8`; equity avg `-3.3942` n `74`; fx avg `-0.0075` n `6`; index avg `-1.6288` n `23`; metal avg `-2.9267` n `18`; unknown avg `-0.6845` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0622`, n `668`, weak_sample_signal
