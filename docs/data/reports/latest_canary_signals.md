# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T19:37:36.569405+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `12`; crypto_alt avg `0.1397` n `228`; crypto_major avg `0.1797` n `8`; equity avg `0.2594` n `86`; fx avg `-0.005` n `6`; index avg `0.0434` n `23`; metal avg `0.0694` n `20`; unknown avg `0.0876` n `764`
- 1h: commodity avg `0.0541` n `12`; crypto_alt avg `0.142` n `228`; crypto_major avg `0.1001` n `8`; equity avg `0.0367` n `86`; fx avg `0.0064` n `6`; index avg `0.0235` n `23`; metal avg `0.046` n `20`; unknown avg `-0.0254` n `756`
- 4h: commodity avg `-0.0161` n `12`; crypto_alt avg `0.2231` n `228`; crypto_major avg `0.2388` n `8`; equity avg `-0.1515` n `86`; fx avg `-0.0046` n `6`; index avg `0.0015` n `23`; metal avg `-0.1659` n `20`; unknown avg `-0.1655` n `756`
- 24h: commodity avg `-0.3879` n `12`; crypto_alt avg `-3.0888` n `228`; crypto_major avg `-3.9729` n `8`; equity avg `-3.0838` n `86`; fx avg `-0.1768` n `6`; index avg `-0.8894` n `23`; metal avg `-1.0919` n `20`; unknown avg `-0.1299` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
