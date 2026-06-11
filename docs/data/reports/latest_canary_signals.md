# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T04:22:25.643156+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0999` n `12`; crypto_alt avg `0.0213` n `228`; crypto_major avg `0.001` n `8`; equity avg `-0.0383` n `74`; fx avg `0.0116` n `6`; index avg `0.0332` n `23`; metal avg `0.0971` n `18`; unknown avg `15.014` n `550`
- 1h: commodity avg `0.0187` n `12`; crypto_alt avg `1.2338` n `228`; crypto_major avg `0.8287` n `8`; equity avg `0.5642` n `74`; fx avg `0.0151` n `6`; index avg `0.3278` n `23`; metal avg `0.4849` n `18`; unknown avg `10.9709` n `550`
- 4h: commodity avg `-0.1022` n `12`; crypto_alt avg `1.7059` n `228`; crypto_major avg `1.3315` n `8`; equity avg `0.7982` n `74`; fx avg `0.054` n `6`; index avg `0.5902` n `23`; metal avg `0.6159` n `18`; unknown avg `2.0253` n `550`
- 24h: commodity avg `1.5213` n `12`; crypto_alt avg `0.8053` n `228`; crypto_major avg `0.4978` n `8`; equity avg `-0.3723` n `74`; fx avg `0.0345` n `6`; index avg `-0.612` n `23`; metal avg `-0.4739` n `18`; unknown avg `2.7454` n `537`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
