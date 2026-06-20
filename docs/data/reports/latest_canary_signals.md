# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T22:07:25.187690+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0031` n `12`; crypto_alt avg `0.0552` n `228`; crypto_major avg `0.0593` n `8`; equity avg `0.0175` n `78`; fx avg `0.0124` n `6`; index avg `-0.0023` n `23`; metal avg `0.0105` n `18`; unknown avg `0.7089` n `701`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `0.271` n `228`; crypto_major avg `0.2461` n `8`; equity avg `0.0346` n `78`; fx avg `0.0036` n `6`; index avg `0.0057` n `23`; metal avg `-0.003` n `18`; unknown avg `0.0829` n `701`
- 4h: commodity avg `-0.0515` n `12`; crypto_alt avg `0.1184` n `228`; crypto_major avg `0.4929` n `8`; equity avg `0.2124` n `78`; fx avg `-0.0022` n `6`; index avg `0.0157` n `23`; metal avg `0.0256` n `18`; unknown avg `-0.6391` n `701`
- 24h: commodity avg `0.1003` n `12`; crypto_alt avg `1.197` n `228`; crypto_major avg `1.7325` n `8`; equity avg `0.5997` n `78`; fx avg `0.1052` n `6`; index avg `0.0676` n `23`; metal avg `-0.0433` n `18`; unknown avg `-0.598` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0576`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
