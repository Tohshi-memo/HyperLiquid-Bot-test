# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T02:37:20.288429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0871` n `12`; crypto_alt avg `-0.0758` n `228`; crypto_major avg `-0.0668` n `8`; equity avg `0.0129` n `67`; fx avg `0.0066` n `6`; index avg `0.0201` n `23`; metal avg `0.0656` n `18`; unknown avg `0.2393` n `407`
- 1h: commodity avg `-0.2403` n `12`; crypto_alt avg `0.1016` n `228`; crypto_major avg `0.0315` n `8`; equity avg `0.2508` n `67`; fx avg `0.0281` n `6`; index avg `0.0998` n `23`; metal avg `0.1308` n `18`; unknown avg `0.001` n `407`
- 4h: commodity avg `0.4603` n `12`; crypto_alt avg `-1.1928` n `228`; crypto_major avg `-0.9321` n `8`; equity avg `-0.812` n `67`; fx avg `-0.0924` n `6`; index avg `-0.255` n `23`; metal avg `-0.7468` n `18`; unknown avg `0.7374` n `405`
- 24h: commodity avg `-0.0291` n `12`; crypto_alt avg `-0.2396` n `228`; crypto_major avg `-0.8727` n `8`; equity avg `-0.2271` n `67`; fx avg `-0.0052` n `6`; index avg `0.1112` n `23`; metal avg `-0.2471` n `18`; unknown avg `1.4482` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1691`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1245`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
