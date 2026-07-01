# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T00:22:30.133726+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0332` n `12`; crypto_alt avg `-0.0792` n `228`; crypto_major avg `-0.3584` n `8`; equity avg `-0.2325` n `88`; fx avg `-0.0155` n `6`; index avg `-0.0659` n `23`; metal avg `-0.0511` n `20`; unknown avg `-0.0469` n `765`
- 1h: commodity avg `-0.0363` n `12`; crypto_alt avg `0.0535` n `228`; crypto_major avg `-0.0802` n `8`; equity avg `-0.2251` n `88`; fx avg `0.0438` n `6`; index avg `-0.052` n `23`; metal avg `-0.1326` n `20`; unknown avg `-0.2108` n `765`
- 4h: commodity avg `-0.029` n `12`; crypto_alt avg `-0.2745` n `228`; crypto_major avg `-0.3493` n `8`; equity avg `-0.0341` n `88`; fx avg `0.008` n `6`; index avg `-0.048` n `23`; metal avg `-0.2666` n `20`; unknown avg `-0.6887` n `765`
- 24h: commodity avg `0.1072` n `12`; crypto_alt avg `-2.0543` n `228`; crypto_major avg `-2.0296` n `8`; equity avg `1.233` n `88`; fx avg `0.09` n `6`; index avg `0.2394` n `23`; metal avg `-0.1393` n `20`; unknown avg `7.3227` n `735`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
