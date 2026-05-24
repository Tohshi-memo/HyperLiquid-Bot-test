# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T11:07:15.202105+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0118` n `12`; crypto_alt avg `0.1495` n `228`; crypto_major avg `0.2098` n `8`; equity avg `0.1032` n `67`; fx avg `0.002` n `6`; index avg `-0.0026` n `23`; metal avg `0.0064` n `18`; unknown avg `0.1037` n `396`
- 1h: commodity avg `0.0004` n `12`; crypto_alt avg `0.0136` n `228`; crypto_major avg `0.0664` n `8`; equity avg `0.1926` n `67`; fx avg `0.0025` n `6`; index avg `0.0075` n `23`; metal avg `-0.0585` n `18`; unknown avg `0.3265` n `396`
- 4h: commodity avg `0.2955` n `12`; crypto_alt avg `-0.0069` n `228`; crypto_major avg `0.4802` n `8`; equity avg `0.2354` n `67`; fx avg `0.0059` n `6`; index avg `-0.031` n `23`; metal avg `0.0238` n `18`; unknown avg `-0.2175` n `396`
- 24h: commodity avg `-2.7007` n `12`; crypto_alt avg `3.7727` n `228`; crypto_major avg `4.6876` n `8`; equity avg `2.7807` n `67`; fx avg `0.0606` n `6`; index avg `1.4316` n `23`; metal avg `1.3542` n `18`; unknown avg `1.5064` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1141`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0871`, n `668`, weak_sample_signal
