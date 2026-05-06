# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T20:37:23.600280+00:00`
- Correlation status: `ready`
- Asset price records: `486`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.27` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.095` n `12`; crypto_alt avg `-0.1931` n `228`; crypto_major avg `-0.192` n `8`; equity avg `-0.2085` n `65`; fx avg `0.0049` n `4`; index avg `-0.1075` n `23`; metal avg `-0.0759` n `18`; unknown avg `-0.0027` n `356`
- 1h: commodity avg `0.2393` n `12`; crypto_alt avg `0.334` n `228`; crypto_major avg `0.0531` n `8`; equity avg `0.2217` n `65`; fx avg `0.0077` n `4`; index avg `0.0707` n `23`; metal avg `-0.0034` n `18`; unknown avg `0.1561` n `356`
- 4h: commodity avg `0.4683` n `12`; crypto_alt avg `0.0528` n `228`; crypto_major avg `-0.12` n `8`; equity avg `0.7966` n `65`; fx avg `-0.0503` n `4`; index avg `0.4177` n `23`; metal avg `0.107` n `18`; unknown avg `-0.2431` n `356`
- 24h: commodity avg `-2.2699` n `7`; crypto_alt avg `1.9396` n `223`; crypto_major avg `0.1162` n `7`; equity avg `2.634` n `47`; fx avg `-0.5217` n `4`; index avg `1.7354` n `6`; metal avg `3.4014` n `7`; unknown avg `4.058` n `311`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1897`, n `478`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1777`, n `478`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1581`, n `478`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1483`, n `478`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1352`, n `482`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1211`, n `482`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0996`, n `478`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `482`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0755`, n `478`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `478`, weak_sample_signal
