# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T07:22:30.826062+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0496` n `12`; crypto_alt avg `0.1741` n `228`; crypto_major avg `0.168` n `8`; equity avg `0.008` n `74`; fx avg `0.0056` n `6`; index avg `-0.0157` n `23`; metal avg `-0.0074` n `18`; unknown avg `0.0541` n `645`
- 1h: commodity avg `-0.1045` n `12`; crypto_alt avg `-0.2545` n `228`; crypto_major avg `-0.0959` n `8`; equity avg `0.0128` n `74`; fx avg `0.0071` n `6`; index avg `0.0275` n `23`; metal avg `-0.0201` n `18`; unknown avg `3.2579` n `641`
- 4h: commodity avg `-0.1837` n `12`; crypto_alt avg `-0.3914` n `228`; crypto_major avg `-0.3558` n `8`; equity avg `0.0087` n `74`; fx avg `-0.0092` n `6`; index avg `-0.0214` n `23`; metal avg `-0.0044` n `18`; unknown avg `2.425` n `625`
- 24h: commodity avg `-0.7184` n `12`; crypto_alt avg `0.6991` n `228`; crypto_major avg `1.156` n `8`; equity avg `0.6712` n `74`; fx avg `-0.0113` n `6`; index avg `0.1943` n `23`; metal avg `0.2532` n `18`; unknown avg `-0.4361` n `599`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
