# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T18:22:24.604977+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.051` n `12`; crypto_alt avg `-0.068` n `228`; crypto_major avg `-0.0979` n `8`; equity avg `-0.0781` n `74`; fx avg `0.0026` n `6`; index avg `-0.0324` n `23`; metal avg `0.1825` n `18`; unknown avg `-0.0364` n `517`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `0.6875` n `228`; crypto_major avg `0.5288` n `8`; equity avg `0.3324` n `74`; fx avg `0.0049` n `6`; index avg `0.2092` n `23`; metal avg `0.2722` n `18`; unknown avg `-0.0465` n `517`
- 4h: commodity avg `0.0816` n `12`; crypto_alt avg `0.8914` n `228`; crypto_major avg `0.4257` n `8`; equity avg `0.9169` n `74`; fx avg `-0.0051` n `6`; index avg `0.265` n `23`; metal avg `0.6622` n `18`; unknown avg `-0.3544` n `517`
- 24h: commodity avg `-0.6283` n `12`; crypto_alt avg `2.6352` n `228`; crypto_major avg `3.0601` n `8`; equity avg `2.5346` n `74`; fx avg `-0.2723` n `6`; index avg `1.1678` n `23`; metal avg `0.2022` n `18`; unknown avg `-2.1162` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1158`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
