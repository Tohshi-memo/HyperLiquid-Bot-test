# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T19:52:21.798958+00:00`
- Correlation status: `ready`
- Asset price records: `483`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.55` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0587` n `12`; crypto_alt avg `0.2464` n `228`; crypto_major avg `0.1827` n `8`; equity avg `0.0959` n `65`; fx avg `0.0092` n `4`; index avg `0.0603` n `23`; metal avg `0.0142` n `18`; unknown avg `0.0445` n `356`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `-0.0472` n `228`; crypto_major avg `0.2125` n `8`; equity avg `0.3517` n `65`; fx avg `0.0003` n `4`; index avg `0.2059` n `23`; metal avg `0.2906` n `18`; unknown avg `0.0069` n `356`
- 4h: commodity avg `-0.1233` n `12`; crypto_alt avg `-0.202` n `228`; crypto_major avg `-0.1898` n `8`; equity avg `0.7591` n `65`; fx avg `-0.0249` n `4`; index avg `0.433` n `23`; metal avg `0.0859` n `18`; unknown avg `-0.342` n `356`
- 24h: commodity avg `-2.4949` n `7`; crypto_alt avg `2.3022` n `223`; crypto_major avg `0.5044` n `7`; equity avg `2.8512` n `47`; fx avg `-0.4847` n `4`; index avg `1.9115` n `6`; metal avg `3.4951` n `7`; unknown avg `3.2692` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1643`, n `475`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.151`, n `475`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1461`, n `475`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1355`, n `475`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1344`, n `479`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1203`, n `479`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `475`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `475`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0749`, n `479`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0742`, n `479`, weak_sample_signal
