# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T20:22:16.842537+00:00`
- Correlation status: `ready`
- Asset price records: `485`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.36` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0877` n `12`; crypto_alt avg `-0.0731` n `228`; crypto_major avg `-0.1117` n `8`; equity avg `0.1932` n `65`; fx avg `-0.0232` n `4`; index avg `0.0258` n `23`; metal avg `0.0294` n `18`; unknown avg `0.031` n `356`
- 1h: commodity avg `0.279` n `12`; crypto_alt avg `0.245` n `228`; crypto_major avg `0.0439` n `8`; equity avg `0.4413` n `65`; fx avg `0.0061` n `4`; index avg `0.1433` n `23`; metal avg `0.0384` n `18`; unknown avg `0.1133` n `356`
- 4h: commodity avg `0.2496` n `12`; crypto_alt avg `0.1195` n `228`; crypto_major avg `0.0309` n `8`; equity avg `1.0134` n `65`; fx avg `-0.0516` n `4`; index avg `0.5411` n `23`; metal avg `0.2138` n `18`; unknown avg `-0.2745` n `356`
- 24h: commodity avg `-2.3218` n `7`; crypto_alt avg `2.3472` n `223`; crypto_major avg `0.4155` n `7`; equity avg `3.3604` n `47`; fx avg `-0.5036` n `4`; index avg `2.0391` n `6`; metal avg `3.5579` n `7`; unknown avg `4.0344` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1873`, n `477`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.175`, n `477`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1589`, n `477`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1489`, n `477`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1356`, n `481`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1216`, n `481`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0982`, n `477`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `481`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0739`, n `477`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0731`, n `477`, weak_sample_signal
