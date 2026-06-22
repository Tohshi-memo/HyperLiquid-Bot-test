# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-22T07:07:39.110714+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0104` n `12`; crypto_alt avg `0.19` n `228`; crypto_major avg `0.2946` n `8`; equity avg `0.1023` n `79`; fx avg `0.0218` n `6`; index avg `0.005` n `23`; metal avg `-0.0847` n `18`; unknown avg `-0.0205` n `701`
- 1h: commodity avg `0.0996` n `12`; crypto_alt avg `0.1605` n `228`; crypto_major avg `0.1229` n `8`; equity avg `0.3409` n `79`; fx avg `0.0506` n `6`; index avg `0.0441` n `23`; metal avg `0.0737` n `18`; unknown avg `-0.1519` n `701`
- 4h: commodity avg `-0.0247` n `12`; crypto_alt avg `0.1343` n `228`; crypto_major avg `0.2537` n `8`; equity avg `0.5149` n `79`; fx avg `-0.0079` n `6`; index avg `0.0503` n `23`; metal avg `0.4158` n `18`; unknown avg `3.7135` n `669`
- 24h: commodity avg `-0.2336` n `12`; crypto_alt avg `-0.0446` n `228`; crypto_major avg `-0.4668` n `8`; equity avg `-0.3007` n `79`; fx avg `0.0154` n `6`; index avg `0.0097` n `23`; metal avg `0.4839` n `18`; unknown avg `-0.1369` n `643`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
