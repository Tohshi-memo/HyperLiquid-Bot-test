# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T09:22:22.070518+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1963` n `12`; crypto_alt avg `-0.0462` n `228`; crypto_major avg `0.1082` n `8`; equity avg `0.0816` n `67`; fx avg `-0.0143` n `6`; index avg `0.0186` n `23`; metal avg `0.1074` n `18`; unknown avg `-0.1077` n `418`
- 1h: commodity avg `-0.385` n `12`; crypto_alt avg `-0.6031` n `228`; crypto_major avg `-0.1122` n `8`; equity avg `0.0075` n `67`; fx avg `-0.0354` n `6`; index avg `-0.0694` n `23`; metal avg `0.2027` n `18`; unknown avg `0.545` n `418`
- 4h: commodity avg `-1.0908` n `12`; crypto_alt avg `0.197` n `228`; crypto_major avg `0.5367` n `8`; equity avg `0.5401` n `67`; fx avg `-0.0133` n `6`; index avg `0.0725` n `23`; metal avg `-0.5411` n `18`; unknown avg `0.1731` n `400`
- 24h: commodity avg `-1.9848` n `12`; crypto_alt avg `-1.1779` n `228`; crypto_major avg `0.1987` n `8`; equity avg `0.8153` n `67`; fx avg `-0.0742` n `6`; index avg `0.8574` n `23`; metal avg `-0.3861` n `18`; unknown avg `1.5498` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.186`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1823`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1733`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1314`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
