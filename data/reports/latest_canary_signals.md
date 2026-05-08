# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T04:37:15.861907+00:00`
- Correlation status: `ready`
- Asset price records: `614`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.06` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0018` n `12`; crypto_alt avg `-0.0914` n `228`; crypto_major avg `-0.1742` n `8`; equity avg `0.0161` n `65`; fx avg `0.0153` n `5`; index avg `-0.0149` n `23`; metal avg `-0.1426` n `18`; unknown avg `0.0408` n `365`
- 1h: commodity avg `0.2654` n `12`; crypto_alt avg `0.1791` n `228`; crypto_major avg `-0.1404` n `8`; equity avg `0.1844` n `65`; fx avg `0.0561` n `5`; index avg `0.0005` n `23`; metal avg `-0.2765` n `18`; unknown avg `-0.2548` n `365`
- 4h: commodity avg `-0.3416` n `12`; crypto_alt avg `0.1516` n `228`; crypto_major avg `-0.4635` n `8`; equity avg `0.2384` n `65`; fx avg `0.0823` n `5`; index avg `0.1653` n `23`; metal avg `0.4957` n `18`; unknown avg `-0.4143` n `365`
- 24h: commodity avg `0.516` n `12`; crypto_alt avg `2.0088` n `228`; crypto_major avg `-1.3565` n `8`; equity avg `-0.8715` n `65`; fx avg `0.2311` n `5`; index avg `-0.5834` n `23`; metal avg `0.3898` n `18`; unknown avg `-0.0715` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.131`, n `610`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1172`, n `606`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1164`, n `606`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `610`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `610`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1082`, n `610`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0916`, n `606`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0874`, n `606`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0791`, n `606`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `610`, weak_sample_signal
