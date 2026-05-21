# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T04:40:39.518351+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0575` n `12`; crypto_alt avg `-0.0551` n `228`; crypto_major avg `-0.1209` n `8`; equity avg `0.0148` n `66`; fx avg `-0.0011` n `6`; index avg `0.0418` n `23`; metal avg `-0.0057` n `18`; unknown avg `-0.0533` n `384`
- 1h: commodity avg `-0.0325` n `12`; crypto_alt avg `-0.2055` n `228`; crypto_major avg `-0.138` n `8`; equity avg `0.1282` n `66`; fx avg `0.0193` n `6`; index avg `0.0882` n `23`; metal avg `0.0969` n `18`; unknown avg `-0.2944` n `384`
- 4h: commodity avg `-0.1012` n `12`; crypto_alt avg `0.5029` n `228`; crypto_major avg `0.5831` n `8`; equity avg `0.6076` n `66`; fx avg `0.0645` n `6`; index avg `0.4134` n `23`; metal avg `-0.2273` n `18`; unknown avg `0.4904` n `384`
- 24h: commodity avg `-2.1561` n `12`; crypto_alt avg `3.7758` n `228`; crypto_major avg `3.832` n `8`; equity avg `2.507` n `66`; fx avg `0.0445` n `6`; index avg `1.8279` n `23`; metal avg `1.5069` n `18`; unknown avg `5.0707` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
