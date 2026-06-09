# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T06:52:25.318941+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0245` n `12`; crypto_alt avg `-0.2172` n `228`; crypto_major avg `-0.2553` n `8`; equity avg `-0.1479` n `74`; fx avg `0.0217` n `6`; index avg `-0.0558` n `23`; metal avg `0.1439` n `18`; unknown avg `0.0019` n `547`
- 1h: commodity avg `0.0017` n `12`; crypto_alt avg `-0.1396` n `228`; crypto_major avg `-0.2542` n `8`; equity avg `-0.0835` n `74`; fx avg `0.0592` n `6`; index avg `-0.1061` n `23`; metal avg `-0.0258` n `18`; unknown avg `0.0897` n `503`
- 4h: commodity avg `-0.1568` n `12`; crypto_alt avg `1.7628` n `228`; crypto_major avg `1.1904` n `8`; equity avg `1.0618` n `74`; fx avg `0.0121` n `6`; index avg `0.4706` n `23`; metal avg `0.3855` n `18`; unknown avg `0.5291` n `503`
- 24h: commodity avg `-1.3408` n `12`; crypto_alt avg `0.5373` n `228`; crypto_major avg `0.8382` n `8`; equity avg `3.1671` n `74`; fx avg `-0.1064` n `6`; index avg `1.2462` n `23`; metal avg `0.781` n `18`; unknown avg `-2.8697` n `503`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0885`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
