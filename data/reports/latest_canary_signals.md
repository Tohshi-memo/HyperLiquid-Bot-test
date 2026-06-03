# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T19:07:31.490825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0266` n `12`; crypto_alt avg `0.2099` n `228`; crypto_major avg `-0.079` n `8`; equity avg `-0.1608` n `73`; fx avg `0.0507` n `6`; index avg `0.0316` n `23`; metal avg `0.0503` n `18`; unknown avg `-0.0895` n `419`
- 1h: commodity avg `0.11` n `12`; crypto_alt avg `0.1049` n `228`; crypto_major avg `-0.0895` n `8`; equity avg `-0.1828` n `73`; fx avg `0.0018` n `6`; index avg `0.0157` n `23`; metal avg `0.0098` n `18`; unknown avg `-0.1258` n `419`
- 4h: commodity avg `0.2291` n `12`; crypto_alt avg `-0.6084` n `228`; crypto_major avg `-0.4642` n `8`; equity avg `-0.6563` n `73`; fx avg `0.0012` n `6`; index avg `-0.2039` n `23`; metal avg `-0.5312` n `18`; unknown avg `-0.4764` n `419`
- 24h: commodity avg `0.8287` n `12`; crypto_alt avg `1.7253` n `228`; crypto_major avg `-1.6157` n `8`; equity avg `-1.8282` n `72`; fx avg `0.0448` n `6`; index avg `-0.2185` n `23`; metal avg `-1.9786` n `18`; unknown avg `0.0348` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1335`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0516`, n `668`, weak_sample_signal
