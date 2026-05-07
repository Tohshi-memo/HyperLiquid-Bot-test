# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T08:22:21.612680+00:00`
- Correlation status: `ready`
- Asset price records: `533`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.3` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.3078` n `12`; crypto_alt avg `-0.1929` n `228`; crypto_major avg `-0.292` n `8`; equity avg `-0.2242` n `65`; fx avg `0.0569` n `4`; index avg `-0.0408` n `23`; metal avg `-0.1557` n `18`; unknown avg `-0.0899` n `358`
- 1h: commodity avg `0.6327` n `12`; crypto_alt avg `0.0646` n `228`; crypto_major avg `0.0181` n `8`; equity avg `-0.2097` n `65`; fx avg `0.0851` n `4`; index avg `0.0367` n `23`; metal avg `0.1729` n `18`; unknown avg `-0.2179` n `358`
- 4h: commodity avg `-0.5884` n `12`; crypto_alt avg `1.5648` n `228`; crypto_major avg `0.8087` n `8`; equity avg `0.4322` n `65`; fx avg `0.0012` n `4`; index avg `0.2621` n `23`; metal avg `1.2566` n `18`; unknown avg `0.5731` n `356`
- 24h: commodity avg `-1.8148` n `7`; crypto_alt avg `1.0365` n `223`; crypto_major avg `-0.8528` n `7`; equity avg `1.5023` n `47`; fx avg `0.0265` n `4`; index avg `1.5559` n `6`; metal avg `2.1387` n `7`; unknown avg `0.8876` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1327`, n `529`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `529`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1038`, n `529`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0993`, n `525`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0893`, n `525`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0836`, n `525`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0813`, n `525`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.078`, n `525`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0683`, n `525`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0659`, n `529`, weak_sample_signal
