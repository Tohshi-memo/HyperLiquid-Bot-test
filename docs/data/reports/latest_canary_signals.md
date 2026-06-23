# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T21:07:30.679566+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0083` n `12`; crypto_alt avg `0.2144` n `228`; crypto_major avg `0.1534` n `8`; equity avg `0.1132` n `86`; fx avg `-0.0099` n `6`; index avg `0.0146` n `23`; metal avg `0.0521` n `20`; unknown avg `0.0703` n `764`
- 1h: commodity avg `-0.0626` n `12`; crypto_alt avg `0.1372` n `228`; crypto_major avg `-0.0872` n `8`; equity avg `0.1432` n `86`; fx avg `-0.001` n `6`; index avg `0.0275` n `23`; metal avg `0.0165` n `20`; unknown avg `0.2535` n `764`
- 4h: commodity avg `0.0268` n `12`; crypto_alt avg `0.7632` n `228`; crypto_major avg `0.3191` n `8`; equity avg `-0.3804` n `86`; fx avg `0.0007` n `6`; index avg `-0.05` n `23`; metal avg `-0.1695` n `20`; unknown avg `0.3342` n `756`
- 24h: commodity avg `-0.4052` n `12`; crypto_alt avg `-2.6559` n `228`; crypto_major avg `-3.6938` n `8`; equity avg `-3.2972` n `86`; fx avg `-0.1882` n `6`; index avg `-0.9147` n `23`; metal avg `-1.1858` n `20`; unknown avg `0.5337` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1121`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
