# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T21:37:26.379980+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0308` n `12`; crypto_alt avg `0.2578` n `228`; crypto_major avg `0.11` n `8`; equity avg `-0.0008` n `74`; fx avg `-0.0996` n `6`; index avg `-0.1377` n `23`; metal avg `0.0255` n `18`; unknown avg `-0.062` n `517`
- 1h: commodity avg `0.1547` n `12`; crypto_alt avg `0.7929` n `228`; crypto_major avg `0.8686` n `8`; equity avg `0.0729` n `74`; fx avg `-0.0887` n `6`; index avg `-0.0629` n `23`; metal avg `0.2384` n `18`; unknown avg `0.3237` n `517`
- 4h: commodity avg `0.1714` n `12`; crypto_alt avg `0.7214` n `228`; crypto_major avg `1.0466` n `8`; equity avg `-0.1158` n `74`; fx avg `-0.1056` n `6`; index avg `-0.0867` n `23`; metal avg `0.0806` n `18`; unknown avg `-0.1338` n `517`
- 24h: commodity avg `-0.8534` n `12`; crypto_alt avg `4.2057` n `228`; crypto_major avg `4.5461` n `8`; equity avg `2.419` n `74`; fx avg `-0.3821` n `6`; index avg `0.8339` n `23`; metal avg `0.3148` n `18`; unknown avg `-1.9293` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
