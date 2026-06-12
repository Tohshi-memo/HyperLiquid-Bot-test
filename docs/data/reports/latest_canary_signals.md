# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T04:37:27.977052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0058` n `12`; crypto_alt avg `0.1288` n `228`; crypto_major avg `0.0627` n `8`; equity avg `0.0651` n `74`; fx avg `-0.0022` n `6`; index avg `0.0` n `23`; metal avg `0.0718` n `18`; unknown avg `-0.4299` n `557`
- 1h: commodity avg `-0.3378` n `12`; crypto_alt avg `0.1926` n `228`; crypto_major avg `0.1805` n `8`; equity avg `0.0626` n `74`; fx avg `0.0155` n `6`; index avg `0.0884` n `23`; metal avg `-0.1908` n `18`; unknown avg `1.8311` n `557`
- 4h: commodity avg `-0.2974` n `12`; crypto_alt avg `-0.0425` n `228`; crypto_major avg `0.0216` n `8`; equity avg `-0.3304` n `74`; fx avg `0.0525` n `6`; index avg `-0.0345` n `23`; metal avg `-0.1908` n `18`; unknown avg `2.0978` n `556`
- 24h: commodity avg `-2.6805` n `12`; crypto_alt avg `2.1378` n `228`; crypto_major avg `2.6644` n `8`; equity avg `3.7618` n `74`; fx avg `0.0375` n `6`; index avg `1.9667` n `23`; metal avg `3.1784` n `18`; unknown avg `1.885` n `530`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
