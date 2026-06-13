# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T18:52:34.846135+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `-0.2393` n `228`; crypto_major avg `-0.1765` n `8`; equity avg `-0.049` n `74`; fx avg `0.001` n `6`; index avg `0.0193` n `23`; metal avg `-0.0072` n `18`; unknown avg `0.0333` n `644`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `-0.3028` n `228`; crypto_major avg `0.1119` n `8`; equity avg `0.1551` n `74`; fx avg `0.031` n `6`; index avg `0.081` n `23`; metal avg `-0.073` n `18`; unknown avg `-0.0454` n `644`
- 4h: commodity avg `-0.1074` n `12`; crypto_alt avg `-0.0883` n `228`; crypto_major avg `-0.3977` n `8`; equity avg `0.0529` n `74`; fx avg `0.0424` n `6`; index avg `-0.042` n `23`; metal avg `0.0664` n `18`; unknown avg `-2.0826` n `644`
- 24h: commodity avg `-0.5639` n `12`; crypto_alt avg `1.7358` n `228`; crypto_major avg `-0.0259` n `8`; equity avg `0.0539` n `74`; fx avg `0.0458` n `6`; index avg `0.4596` n `23`; metal avg `0.2345` n `18`; unknown avg `-1.7465` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0674`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0668`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0545`, n `668`, weak_sample_signal
