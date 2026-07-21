# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-21T14:37:35.926675+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.106` n `12`; crypto_alt avg `-0.0365` n `230`; crypto_major avg `0.0919` n `8`; equity avg `0.4035` n `98`; fx avg `-0.0078` n `6`; index avg `0.0515` n `25`; metal avg `0.0253` n `20`; unknown avg `0.0081` n `771`
- 1h: commodity avg `0.1177` n `12`; crypto_alt avg `0.018` n `230`; crypto_major avg `0.02` n `8`; equity avg `0.6126` n `98`; fx avg `0.031` n `6`; index avg `0.0709` n `25`; metal avg `0.1357` n `20`; unknown avg `0.0042` n `771`
- 4h: commodity avg `0.3363` n `12`; crypto_alt avg `-0.1866` n `230`; crypto_major avg `-0.1296` n `8`; equity avg `0.7523` n `98`; fx avg `-0.0077` n `6`; index avg `0.0829` n `25`; metal avg `-0.1084` n `20`; unknown avg `0.0689` n `771`
- 24h: commodity avg `0.7307` n `12`; crypto_alt avg `1.9586` n `230`; crypto_major avg `2.556` n `8`; equity avg `2.8131` n `98`; fx avg `-0.0279` n `6`; index avg `0.3203` n `25`; metal avg `0.5805` n `20`; unknown avg `0.2529` n `754`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0846`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0582`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.055`, n `668`, weak_sample_signal
