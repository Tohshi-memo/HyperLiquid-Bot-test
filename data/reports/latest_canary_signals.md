# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T21:37:23.187983+00:00`
- Correlation status: `ready`
- Asset price records: `490`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.98` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1066` n `12`; crypto_alt avg `0.3889` n `228`; crypto_major avg `0.1604` n `8`; equity avg `-0.141` n `65`; fx avg `-0.0069` n `4`; index avg `0.0173` n `23`; metal avg `-0.0115` n `18`; unknown avg `0.0822` n `356`
- 1h: commodity avg `0.1475` n `12`; crypto_alt avg `0.5682` n `228`; crypto_major avg `0.2109` n `8`; equity avg `-0.509` n `65`; fx avg `-0.0168` n `4`; index avg `-0.0957` n `23`; metal avg `0.0061` n `18`; unknown avg `0.0834` n `356`
- 4h: commodity avg `0.2912` n `12`; crypto_alt avg `0.5484` n `228`; crypto_major avg `0.1483` n `8`; equity avg `0.0357` n `65`; fx avg `-0.0355` n `4`; index avg `0.2082` n `23`; metal avg `0.3756` n `18`; unknown avg `0.2179` n `356`
- 24h: commodity avg `-2.2846` n `7`; crypto_alt avg `2.1733` n `223`; crypto_major avg `0.4374` n `7`; equity avg `2.2852` n `47`; fx avg `-0.5677` n `4`; index avg `1.4391` n `6`; metal avg `3.448` n `7`; unknown avg `3.9799` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1318`, n `486`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.118`, n `486`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1164`, n `482`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1085`, n `482`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1041`, n `482`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0985`, n `482`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0831`, n `482`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `486`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0629`, n `482`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0608`, n `486`, weak_sample_signal
