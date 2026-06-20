# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T19:07:28.025885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0124` n `12`; crypto_alt avg `-0.1102` n `228`; crypto_major avg `-0.0878` n `8`; equity avg `-0.0079` n `78`; fx avg `-0.0018` n `6`; index avg `0.0035` n `23`; metal avg `0.0028` n `18`; unknown avg `-0.1022` n `701`
- 1h: commodity avg `-0.0607` n `12`; crypto_alt avg `-0.1624` n `228`; crypto_major avg `-0.0433` n `8`; equity avg `-0.0117` n `78`; fx avg `-0.0078` n `6`; index avg `0.0127` n `23`; metal avg `0.027` n `18`; unknown avg `-0.4157` n `701`
- 4h: commodity avg `-0.0062` n `12`; crypto_alt avg `-0.0491` n `228`; crypto_major avg `-0.3871` n `8`; equity avg `-0.1214` n `78`; fx avg `0.0193` n `6`; index avg `-0.0012` n `23`; metal avg `-0.0684` n `18`; unknown avg `0.0175` n `701`
- 24h: commodity avg `0.3019` n `12`; crypto_alt avg `0.5804` n `228`; crypto_major avg `0.833` n `8`; equity avg `0.3343` n `78`; fx avg `0.0409` n `6`; index avg `0.0491` n `23`; metal avg `0.099` n `18`; unknown avg `-0.0564` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0975`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0969`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0687`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
