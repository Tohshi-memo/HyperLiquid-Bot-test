# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T16:55:23.071071+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0877` n `12`; crypto_alt avg `-0.2405` n `228`; crypto_major avg `-0.2632` n `8`; equity avg `-0.0829` n `74`; fx avg `0.0077` n `6`; index avg `-0.0294` n `23`; metal avg `0.0011` n `18`; unknown avg `0.0291` n `645`
- 1h: commodity avg `-0.2412` n `12`; crypto_alt avg `-0.0015` n `228`; crypto_major avg `-0.116` n `8`; equity avg `-0.1221` n `74`; fx avg `0.0083` n `6`; index avg `-0.037` n `23`; metal avg `0.0435` n `18`; unknown avg `0.2175` n `645`
- 4h: commodity avg `0.0045` n `12`; crypto_alt avg `-0.4541` n `228`; crypto_major avg `-0.4715` n `8`; equity avg `-0.1122` n `74`; fx avg `-0.0289` n `6`; index avg `0.0375` n `23`; metal avg `-0.058` n `18`; unknown avg `0.1323` n `645`
- 24h: commodity avg `-0.3545` n `12`; crypto_alt avg `-1.1487` n `228`; crypto_major avg `-0.4828` n `8`; equity avg `0.5317` n `74`; fx avg `0.0002` n `6`; index avg `0.2161` n `23`; metal avg `-0.0205` n `18`; unknown avg `1.7148` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0666`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
