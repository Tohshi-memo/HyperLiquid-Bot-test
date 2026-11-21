# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T00:07:34.317136+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `13`; crypto_alt avg `-0.0993` n `239`; crypto_major avg `0.0802` n `8`; equity avg `0.0134` n `166`; fx avg `0.0031` n `6`; index avg `0.0036` n `27`; metal avg `-0.0045` n `20`; unknown avg `2.8524` n `1246`
- 1h: commodity avg `-0.0527` n `13`; crypto_alt avg `-0.5823` n `239`; crypto_major avg `-0.3624` n `8`; equity avg `-0.2981` n `166`; fx avg `-0.0095` n `6`; index avg `-0.0176` n `27`; metal avg `-0.0155` n `20`; unknown avg `3.0639` n `1246`
- 4h: commodity avg `0.1234` n `13`; crypto_alt avg `1.2916` n `239`; crypto_major avg `1.1352` n `8`; equity avg `1.2341` n `166`; fx avg `-0.0236` n `6`; index avg `0.1061` n `27`; metal avg `0.1679` n `20`; unknown avg `172.6253` n `1200`
- 24h: commodity avg `0.2432` n `13`; crypto_alt avg `-5.0857` n `239`; crypto_major avg `-5.7546` n `8`; equity avg `-5.8833` n `166`; fx avg `-0.0416` n `6`; index avg `-0.6691` n `27`; metal avg `-0.6899` n `20`; unknown avg `12.3145` n `1117`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
