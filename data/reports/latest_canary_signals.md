# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T10:07:30.020205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `0.1366` n `229`; crypto_major avg `0.169` n `8`; equity avg `0.0847` n `91`; fx avg `-0.0131` n `6`; index avg `0.0036` n `25`; metal avg `0.0703` n `20`; unknown avg `0.0781` n `763`
- 1h: commodity avg `-0.1234` n `12`; crypto_alt avg `0.2692` n `229`; crypto_major avg `0.2534` n `8`; equity avg `-0.079` n `91`; fx avg `-0.0428` n `6`; index avg `0.0117` n `25`; metal avg `0.1345` n `20`; unknown avg `0.0406` n `761`
- 4h: commodity avg `0.0144` n `12`; crypto_alt avg `0.3724` n `229`; crypto_major avg `0.5599` n `8`; equity avg `-0.0691` n `91`; fx avg `-0.0994` n `6`; index avg `0.0017` n `25`; metal avg `0.2534` n `20`; unknown avg `-0.1063` n `757`
- 24h: commodity avg `0.304` n `12`; crypto_alt avg `0.6534` n `229`; crypto_major avg `0.2482` n `8`; equity avg `-1.4851` n `90`; fx avg `-0.1078` n `6`; index avg `-0.3373` n `25`; metal avg `-0.1127` n `20`; unknown avg `-0.4438` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0613`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0519`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.05`, n `668`, weak_sample_signal
