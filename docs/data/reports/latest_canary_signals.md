# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T06:52:21.960341+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0504` n `12`; crypto_alt avg `0.1475` n `228`; crypto_major avg `-0.0246` n `8`; equity avg `-0.0141` n `67`; fx avg `-0.017` n `6`; index avg `-0.0112` n `23`; metal avg `-0.0388` n `18`; unknown avg `-0.041` n `417`
- 1h: commodity avg `-0.1164` n `12`; crypto_alt avg `0.1544` n `228`; crypto_major avg `0.0508` n `8`; equity avg `0.0794` n `67`; fx avg `-0.0165` n `6`; index avg `0.0352` n `23`; metal avg `0.1328` n `18`; unknown avg `0.0389` n `397`
- 4h: commodity avg `0.027` n `12`; crypto_alt avg `0.8927` n `228`; crypto_major avg `0.6217` n `8`; equity avg `0.1153` n `67`; fx avg `-0.0559` n `6`; index avg `0.0426` n `23`; metal avg `-0.0331` n `18`; unknown avg `-0.0501` n `397`
- 24h: commodity avg `0.204` n `12`; crypto_alt avg `-0.2414` n `228`; crypto_major avg `-0.9504` n `8`; equity avg `-0.4249` n `67`; fx avg `-0.1086` n `6`; index avg `-0.0794` n `23`; metal avg `-0.2575` n `18`; unknown avg `0.3871` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1602`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
