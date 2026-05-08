# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T13:07:11.064593+00:00`
- Correlation status: `ready`
- Asset price records: `648`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.102` n `12`; crypto_alt avg `-0.08` n `228`; crypto_major avg `-0.0883` n `8`; equity avg `-0.05` n `65`; fx avg `-0.0015` n `5`; index avg `-0.0923` n `23`; metal avg `-0.3922` n `18`; unknown avg `0.1137` n `375`
- 1h: commodity avg `0.2867` n `12`; crypto_alt avg `-0.2616` n `228`; crypto_major avg `-0.3303` n `8`; equity avg `0.193` n `65`; fx avg `-0.0209` n `5`; index avg `0.0878` n `23`; metal avg `-0.0923` n `18`; unknown avg `-0.218` n `375`
- 4h: commodity avg `0.3086` n `12`; crypto_alt avg `0.0821` n `228`; crypto_major avg `-0.0968` n `8`; equity avg `0.0705` n `65`; fx avg `-0.0226` n `5`; index avg `0.1262` n `23`; metal avg `-0.0965` n `18`; unknown avg `0.0278` n `375`
- 24h: commodity avg `1.9902` n `12`; crypto_alt avg `0.2924` n `228`; crypto_major avg `-1.6265` n `8`; equity avg `-0.2763` n `65`; fx avg `0.2177` n `5`; index avg `-0.1265` n `23`; metal avg `-0.8969` n `18`; unknown avg `-0.7235` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1298`, n `640`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1281`, n `640`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `644`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `644`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `644`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0905`, n `644`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.09`, n `640`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0892`, n `640`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0723`, n `644`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.07`, n `644`, weak_sample_signal
