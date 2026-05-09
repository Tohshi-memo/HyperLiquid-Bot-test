# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-09T09:52:17.772406+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `12`; crypto_alt avg `-0.2428` n `228`; crypto_major avg `-0.221` n `8`; equity avg `-0.0217` n `65`; fx avg `0.0` n `5`; index avg `-0.0026` n `23`; metal avg `-0.0011` n `18`; unknown avg `0.1799` n `376`
- 1h: commodity avg `-0.0118` n `12`; crypto_alt avg `-0.8259` n `228`; crypto_major avg `-0.3303` n `8`; equity avg `-0.0695` n `65`; fx avg `0.0` n `5`; index avg `-0.026` n `23`; metal avg `-0.0011` n `18`; unknown avg `-0.3186` n `376`
- 4h: commodity avg `0.0187` n `12`; crypto_alt avg `-1.2139` n `228`; crypto_major avg `-0.4605` n `8`; equity avg `0.0224` n `65`; fx avg `0.0006` n `5`; index avg `0.0497` n `23`; metal avg `-0.0034` n `18`; unknown avg `-0.5278` n `356`
- 24h: commodity avg `-0.2806` n `12`; crypto_alt avg `2.92` n `228`; crypto_major avg `2.0088` n `8`; equity avg `2.8811` n `65`; fx avg `-0.0424` n `5`; index avg `1.1667` n `23`; metal avg `0.0435` n `18`; unknown avg `0.4582` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
