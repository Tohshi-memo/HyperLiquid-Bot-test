# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T21:22:25.456253+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `13`; crypto_alt avg `-0.0306` n `239`; crypto_major avg `0.0342` n `8`; equity avg `0.0495` n `166`; fx avg `-0.0064` n `6`; index avg `0.0011` n `27`; metal avg `0.0007` n `20`; unknown avg `-0.1355` n `1258`
- 1h: commodity avg `-0.0002` n `13`; crypto_alt avg `0.0812` n `239`; crypto_major avg `0.0664` n `8`; equity avg `0.1287` n `166`; fx avg `-0.0177` n `6`; index avg `0.019` n `27`; metal avg `-0.0093` n `20`; unknown avg `-0.2754` n `1228`
- 4h: commodity avg `0.0727` n `13`; crypto_alt avg `-0.1289` n `239`; crypto_major avg `0.2718` n `8`; equity avg `0.2512` n `166`; fx avg `-0.0021` n `6`; index avg `0.056` n `27`; metal avg `0.0135` n `20`; unknown avg `311.481` n `1172`
- 24h: commodity avg `0.0176` n `13`; crypto_alt avg `1.4727` n `239`; crypto_major avg `3.0159` n `8`; equity avg `1.305` n `166`; fx avg `-0.088` n `6`; index avg `0.2326` n `27`; metal avg `0.2909` n `20`; unknown avg `185.0595` n `1086`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1007`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
