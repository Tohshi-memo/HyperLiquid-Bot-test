# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T08:37:28.018121+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0741` n `12`; crypto_alt avg `-0.0672` n `231`; crypto_major avg `-0.0422` n `8`; equity avg `0.1056` n `127`; fx avg `-0.0125` n `6`; index avg `0.0227` n `26`; metal avg `0.0088` n `20`; unknown avg `-0.0128` n `792`
- 1h: commodity avg `-0.0645` n `12`; crypto_alt avg `0.0793` n `231`; crypto_major avg `0.0987` n `8`; equity avg `-0.0521` n `127`; fx avg `0.0033` n `6`; index avg `-0.0047` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.0845` n `792`
- 4h: commodity avg `-0.2032` n `12`; crypto_alt avg `0.2298` n `231`; crypto_major avg `0.3022` n `8`; equity avg `-0.2943` n `127`; fx avg `-0.0694` n `6`; index avg `-0.0284` n `26`; metal avg `0.4005` n `20`; unknown avg `0.1944` n `760`
- 24h: commodity avg `0.2163` n `12`; crypto_alt avg `-1.0435` n `231`; crypto_major avg `0.1326` n `8`; equity avg `-1.0345` n `127`; fx avg `-0.088` n `6`; index avg `-0.0333` n `26`; metal avg `0.5526` n `20`; unknown avg `0.3546` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
