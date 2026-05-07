# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T00:07:26.124182+00:00`
- Correlation status: `ready`
- Asset price records: `500`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.05` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1435` n `12`; crypto_alt avg `-0.061` n `228`; crypto_major avg `0.0351` n `8`; equity avg `-0.1142` n `65`; fx avg `0.0502` n `4`; index avg `-0.0037` n `23`; metal avg `-0.1193` n `18`; unknown avg `-0.0644` n `356`
- 1h: commodity avg `0.1707` n `12`; crypto_alt avg `0.4751` n `228`; crypto_major avg `0.308` n `8`; equity avg `0.0539` n `65`; fx avg `0.0667` n `4`; index avg `0.0753` n `23`; metal avg `-0.0764` n `18`; unknown avg `0.0897` n `356`
- 4h: commodity avg `0.3336` n `12`; crypto_alt avg `-0.08` n `228`; crypto_major avg `-0.3651` n `8`; equity avg `-0.3318` n `65`; fx avg `0.0407` n `4`; index avg `-0.1138` n `23`; metal avg `-0.0945` n `18`; unknown avg `0.0036` n `356`
- 24h: commodity avg `-1.5828` n `7`; crypto_alt avg `2.2356` n `223`; crypto_major avg `0.437` n `7`; equity avg `1.826` n `47`; fx avg `-0.3236` n `4`; index avg `1.4602` n `6`; metal avg `2.6556` n `7`; unknown avg `3.5014` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1291`, n `496`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1159`, n `496`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1034`, n `492`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0925`, n `492`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0875`, n `492`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0815`, n `492`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0785`, n `492`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0672`, n `496`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0621`, n `492`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0598`, n `492`, weak_sample_signal
