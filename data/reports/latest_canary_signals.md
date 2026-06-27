# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T11:52:34.778931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0033` n `12`; crypto_alt avg `0.2597` n `228`; crypto_major avg `0.2407` n `8`; equity avg `-0.0006` n `88`; fx avg `0.0` n `6`; index avg `0.0091` n `23`; metal avg `0.0135` n `20`; unknown avg `0.0493` n `764`
- 1h: commodity avg `0.0344` n `12`; crypto_alt avg `-0.0384` n `228`; crypto_major avg `-0.0194` n `8`; equity avg `-0.0603` n `88`; fx avg `-0.0103` n `6`; index avg `-0.0115` n `23`; metal avg `0.0088` n `20`; unknown avg `0.1747` n `764`
- 4h: commodity avg `0.0671` n `12`; crypto_alt avg `-0.2664` n `228`; crypto_major avg `-0.2723` n `8`; equity avg `0.011` n `88`; fx avg `0.0337` n `6`; index avg `-0.0227` n `23`; metal avg `-0.0147` n `20`; unknown avg `0.0375` n `764`
- 24h: commodity avg `-0.0236` n `12`; crypto_alt avg `2.2019` n `228`; crypto_major avg `2.2538` n `8`; equity avg `1.9777` n `87`; fx avg `0.0331` n `6`; index avg `0.0776` n `23`; metal avg `0.4303` n `20`; unknown avg `0.1863` n `700`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2059`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1357`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0772`, n `668`, weak_sample_signal
