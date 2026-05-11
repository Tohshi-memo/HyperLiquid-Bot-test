# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-11T23:15:53.356993+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `2.5258` n `12`; crypto_alt avg `0.1863` n `228`; crypto_major avg `1.2957` n `8`; equity avg `0.0888` n `65`; fx avg `0.2935` n `5`; index avg `0.2298` n `23`; metal avg `2.5943` n `18`; unknown avg `-0.0781` n `366`
- 1h: commodity avg `2.5258` n `12`; crypto_alt avg `0.1863` n `228`; crypto_major avg `1.2957` n `8`; equity avg `0.0888` n `65`; fx avg `0.2935` n `5`; index avg `0.2298` n `23`; metal avg `2.5943` n `18`; unknown avg `-0.0781` n `366`
- 4h: commodity avg `2.5258` n `12`; crypto_alt avg `0.1863` n `228`; crypto_major avg `1.2957` n `8`; equity avg `0.0888` n `65`; fx avg `0.2935` n `5`; index avg `0.2298` n `23`; metal avg `2.5943` n `18`; unknown avg `-0.0781` n `366`
- 24h: commodity avg `2.5258` n `12`; crypto_alt avg `0.1863` n `228`; crypto_major avg `1.2957` n `8`; equity avg `0.0888` n `65`; fx avg `0.2935` n `5`; index avg `0.2298` n `23`; metal avg `2.5943` n `18`; unknown avg `-0.0781` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1428`, n `671`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1234`, n `671`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1125`, n `671`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `671`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0935`, n `671`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0812`, n `671`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `671`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `671`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0685`, n `671`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0658`, n `671`, weak_sample_signal
