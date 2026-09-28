# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T06:52:32.973866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.084` n `12`; crypto_alt avg `0.0322` n `234`; crypto_major avg `0.0171` n `8`; equity avg `-0.4547` n `140`; fx avg `-0.0277` n `6`; index avg `0.0091` n `23`; metal avg `0.0221` n `18`; unknown avg `1.3869` n `944`
- 1h: commodity avg `-0.1446` n `12`; crypto_alt avg `-0.2871` n `234`; crypto_major avg `-0.1307` n `8`; equity avg `-0.5352` n `140`; fx avg `-0.0276` n `6`; index avg `-0.0329` n `23`; metal avg `0.0271` n `18`; unknown avg `4.3711` n `918`
- 4h: commodity avg `0.0149` n `12`; crypto_alt avg `-1.6211` n `234`; crypto_major avg `-0.9117` n `8`; equity avg `-0.8246` n `140`; fx avg `0.0058` n `6`; index avg `-0.0467` n `23`; metal avg `-0.0875` n `18`; unknown avg `0.6959` n `910`
- 24h: commodity avg `-0.4609` n `12`; crypto_alt avg `-2.7025` n `234`; crypto_major avg `-2.3485` n `8`; equity avg `-2.2207` n `140`; fx avg `0.0535` n `6`; index avg `-0.1744` n `23`; metal avg `-0.8702` n `18`; unknown avg `4.5918` n `797`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1601`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
