# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T10:22:19.775006+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0936` n `12`; crypto_alt avg `0.709` n `228`; crypto_major avg `0.6158` n `8`; equity avg `0.1124` n `67`; fx avg `0.0002` n `6`; index avg `0.0661` n `23`; metal avg `0.2093` n `18`; unknown avg `0.2466` n `417`
- 1h: commodity avg `-0.2923` n `12`; crypto_alt avg `0.5623` n `228`; crypto_major avg `0.5708` n `8`; equity avg `0.1924` n `67`; fx avg `0.0` n `6`; index avg `0.1391` n `23`; metal avg `0.0141` n `18`; unknown avg `0.2917` n `417`
- 4h: commodity avg `0.3854` n `12`; crypto_alt avg `0.6964` n `228`; crypto_major avg `0.3138` n `8`; equity avg `0.2661` n `67`; fx avg `0.0315` n `6`; index avg `0.156` n `23`; metal avg `-0.2301` n `18`; unknown avg `0.1525` n `417`
- 24h: commodity avg `0.7758` n `12`; crypto_alt avg `-0.3649` n `228`; crypto_major avg `-1.0753` n `8`; equity avg `-0.4275` n `67`; fx avg `-0.0826` n `6`; index avg `0.0488` n `23`; metal avg `-0.8904` n `18`; unknown avg `-0.148` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1744`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1717`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
