# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T04:07:14.421145+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `12`; crypto_alt avg `0.1589` n `228`; crypto_major avg `0.0599` n `8`; equity avg `0.0629` n `66`; fx avg `0.0` n `6`; index avg `0.0378` n `23`; metal avg `0.0602` n `18`; unknown avg `0.1` n `384`
- 1h: commodity avg `-0.0135` n `12`; crypto_alt avg `0.3263` n `228`; crypto_major avg `0.3964` n `8`; equity avg `0.1276` n `66`; fx avg `-0.0048` n `6`; index avg `0.1349` n `23`; metal avg `-0.0238` n `18`; unknown avg `-0.4637` n `384`
- 4h: commodity avg `-0.0586` n `12`; crypto_alt avg `1.2153` n `228`; crypto_major avg `1.1217` n `8`; equity avg `0.8702` n `66`; fx avg `0.0598` n `6`; index avg `0.5359` n `23`; metal avg `-0.2441` n `18`; unknown avg `1.062` n `384`
- 24h: commodity avg `-2.0029` n `12`; crypto_alt avg `3.94` n `228`; crypto_major avg `4.0373` n `8`; equity avg `2.486` n `66`; fx avg `0.0249` n `6`; index avg `1.7434` n `23`; metal avg `1.3442` n `18`; unknown avg `5.2136` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0604`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0534`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0533`, n `668`, weak_sample_signal
