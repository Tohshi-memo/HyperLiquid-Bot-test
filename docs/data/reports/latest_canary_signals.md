# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T23:07:16.143715+00:00`
- Correlation status: `ready`
- Asset price records: `496`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.52` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0189` n `12`; crypto_alt avg `-0.3841` n `228`; crypto_major avg `-0.2142` n `8`; equity avg `0.0226` n `65`; fx avg `-0.0008` n `4`; index avg `0.0278` n `23`; metal avg `0.0193` n `18`; unknown avg `-0.0024` n `356`
- 1h: commodity avg `0.0226` n `12`; crypto_alt avg `-0.6264` n `228`; crypto_major avg `-0.403` n `8`; equity avg `0.1972` n `65`; fx avg `0.0012` n `4`; index avg `0.0137` n `23`; metal avg `0.1037` n `18`; unknown avg `-0.0441` n `356`
- 4h: commodity avg `0.2858` n `12`; crypto_alt avg `-0.3711` n `228`; crypto_major avg `-0.452` n `8`; equity avg `0.0942` n `65`; fx avg `-0.0078` n `4`; index avg `0.0371` n `23`; metal avg `0.1458` n `18`; unknown avg `0.0346` n `356`
- 24h: commodity avg `-1.854` n `7`; crypto_alt avg `1.6623` n `223`; crypto_major avg `-0.2808` n `7`; equity avg `1.631` n `47`; fx avg `-0.6103` n `4`; index avg `1.3491` n `6`; metal avg `3.096` n `7`; unknown avg `3.3716` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1314`, n `492`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1179`, n `492`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0907`, n `488`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0822`, n `488`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0791`, n `488`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0778`, n `488`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0726`, n `488`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `492`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0641`, n `488`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0621`, n `492`, weak_sample_signal
