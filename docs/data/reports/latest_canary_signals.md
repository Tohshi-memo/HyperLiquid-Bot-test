# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T17:22:29.280392+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.0414` n `228`; crypto_major avg `0.0039` n `8`; equity avg `-0.2077` n `74`; fx avg `-0.0019` n `6`; index avg `-0.2314` n `23`; metal avg `-0.1653` n `18`; unknown avg `-0.0215` n `517`
- 1h: commodity avg `-0.0018` n `12`; crypto_alt avg `-0.5967` n `228`; crypto_major avg `-0.7811` n `8`; equity avg `-0.5696` n `74`; fx avg `-0.003` n `6`; index avg `-0.3664` n `23`; metal avg `-0.094` n `18`; unknown avg `-0.0832` n `517`
- 4h: commodity avg `0.1617` n `12`; crypto_alt avg `-0.2116` n `228`; crypto_major avg `-0.3334` n `8`; equity avg `-0.1063` n `74`; fx avg `-0.0185` n `6`; index avg `-0.1678` n `23`; metal avg `-0.2072` n `18`; unknown avg `-0.3193` n `517`
- 24h: commodity avg `-0.5375` n `12`; crypto_alt avg `1.6154` n `228`; crypto_major avg `2.4544` n `8`; equity avg `1.902` n `74`; fx avg `-0.285` n `6`; index avg `0.793` n `23`; metal avg `-0.1332` n `18`; unknown avg `-2.114` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
