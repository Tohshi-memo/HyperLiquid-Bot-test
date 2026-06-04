# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T20:37:21.481459+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0552` n `12`; crypto_alt avg `0.1426` n `228`; crypto_major avg `0.2751` n `8`; equity avg `0.0291` n `74`; fx avg `0.0047` n `6`; index avg `-0.0089` n `23`; metal avg `-0.0431` n `18`; unknown avg `0.2691` n `424`
- 1h: commodity avg `0.0248` n `12`; crypto_alt avg `-0.7258` n `228`; crypto_major avg `-0.2265` n `8`; equity avg `-0.6831` n `74`; fx avg `-0.0059` n `6`; index avg `-0.2468` n `23`; metal avg `-0.163` n `18`; unknown avg `0.236` n `424`
- 4h: commodity avg `0.126` n `12`; crypto_alt avg `-0.574` n `228`; crypto_major avg `-0.1908` n `8`; equity avg `-0.6083` n `74`; fx avg `-0.0564` n `6`; index avg `-0.0329` n `23`; metal avg `-0.0887` n `18`; unknown avg `0.8226` n `424`
- 24h: commodity avg `-0.6966` n `12`; crypto_alt avg `-4.9884` n `228`; crypto_major avg `-3.0697` n `8`; equity avg `-0.8122` n `73`; fx avg `-0.0` n `6`; index avg `0.0314` n `23`; metal avg `0.9541` n `18`; unknown avg `0.0634` n `401`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1424`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1236`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
