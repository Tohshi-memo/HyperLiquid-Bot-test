# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T02:37:30.232329+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.005` n `12`; crypto_alt avg `-0.2142` n `228`; crypto_major avg `-0.1071` n `8`; equity avg `0.2946` n `74`; fx avg `0.0324` n `6`; index avg `0.173` n `23`; metal avg `0.0284` n `18`; unknown avg `-0.0415` n `517`
- 1h: commodity avg `-0.0228` n `12`; crypto_alt avg `0.246` n `228`; crypto_major avg `0.4666` n `8`; equity avg `0.812` n `74`; fx avg `0.0688` n `6`; index avg `0.3811` n `23`; metal avg `0.0841` n `18`; unknown avg `-0.3102` n `517`
- 4h: commodity avg `0.1389` n `12`; crypto_alt avg `-0.9363` n `228`; crypto_major avg `-0.0666` n `8`; equity avg `0.6961` n `74`; fx avg `0.004` n `6`; index avg `0.4575` n `23`; metal avg `-0.1877` n `18`; unknown avg `-0.4424` n `516`
- 24h: commodity avg `0.4479` n `12`; crypto_alt avg `1.3995` n `228`; crypto_major avg `3.9504` n `8`; equity avg `1.8918` n `74`; fx avg `-0.046` n `6`; index avg `0.6159` n `23`; metal avg `-0.1488` n `18`; unknown avg `-5.3175` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
