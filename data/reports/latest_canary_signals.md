# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T17:22:16.750922+00:00`
- Correlation status: `ready`
- Asset price records: `665`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0383` n `12`; crypto_alt avg `0.1439` n `228`; crypto_major avg `0.1669` n `8`; equity avg `0.093` n `65`; fx avg `-0.0017` n `5`; index avg `0.111` n `23`; metal avg `0.0941` n `18`; unknown avg `-0.1336` n `375`
- 1h: commodity avg `-0.5339` n `12`; crypto_alt avg `0.3823` n `228`; crypto_major avg `0.158` n `8`; equity avg `0.0423` n `65`; fx avg `-0.0056` n `5`; index avg `0.2323` n `23`; metal avg `0.1408` n `18`; unknown avg `-0.2325` n `375`
- 4h: commodity avg `0.3224` n `12`; crypto_alt avg `1.7246` n `228`; crypto_major avg `0.8682` n `8`; equity avg `1.0519` n `65`; fx avg `-0.0096` n `5`; index avg `0.6025` n `23`; metal avg `-0.043` n `18`; unknown avg `-0.048` n `375`
- 24h: commodity avg `0.3395` n `12`; crypto_alt avg `3.0071` n `228`; crypto_major avg `0.6414` n `8`; equity avg `2.5465` n `65`; fx avg `0.1364` n `5`; index avg `1.389` n `23`; metal avg `0.4705` n `18`; unknown avg `0.2803` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1203`, n `657`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1159`, n `657`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.114`, n `661`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0999`, n `657`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.098`, n `661`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.097`, n `657`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `661`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0807`, n `661`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0735`, n `661`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.072`, n `661`, weak_sample_signal
