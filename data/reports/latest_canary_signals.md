# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T16:37:31.958461+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0748` n `12`; crypto_alt avg `-0.4127` n `228`; crypto_major avg `-0.4796` n `8`; equity avg `-0.2292` n `74`; fx avg `-0.0056` n `6`; index avg `-0.122` n `23`; metal avg `0.0715` n `18`; unknown avg `-0.0451` n `517`
- 1h: commodity avg `-0.031` n `12`; crypto_alt avg `-0.1087` n `228`; crypto_major avg `-0.3249` n `8`; equity avg `0.014` n `74`; fx avg `-0.0157` n `6`; index avg `-0.0895` n `23`; metal avg `0.1399` n `18`; unknown avg `-0.0727` n `517`
- 4h: commodity avg `-0.047` n `12`; crypto_alt avg `0.4256` n `228`; crypto_major avg `0.7607` n `8`; equity avg `0.5439` n `74`; fx avg `0.0075` n `6`; index avg `0.1282` n `23`; metal avg `-0.2499` n `18`; unknown avg `0.2316` n `517`
- 24h: commodity avg `-0.6254` n `12`; crypto_alt avg `2.003` n `228`; crypto_major avg `3.1803` n `8`; equity avg `2.287` n `74`; fx avg `-0.2826` n `6`; index avg `1.0182` n `23`; metal avg `0.1215` n `18`; unknown avg `-3.1887` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1127`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0781`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0709`, n `668`, weak_sample_signal
