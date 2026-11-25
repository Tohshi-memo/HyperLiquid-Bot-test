# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T22:52:27.050565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0156` n `13`; crypto_alt avg `0.0363` n `239`; crypto_major avg `0.0136` n `8`; equity avg `0.1517` n `168`; fx avg `-0.0032` n `6`; index avg `0.004` n `27`; metal avg `0.01` n `20`; unknown avg `0.0692` n `1267`
- 1h: commodity avg `-0.0374` n `13`; crypto_alt avg `-0.1679` n `239`; crypto_major avg `-0.2402` n `8`; equity avg `0.4343` n `168`; fx avg `-0.0042` n `6`; index avg `0.0027` n `27`; metal avg `0.0968` n `20`; unknown avg `42.369` n `1247`
- 4h: commodity avg `-0.0474` n `13`; crypto_alt avg `0.8707` n `239`; crypto_major avg `0.7314` n `8`; equity avg `0.7434` n `168`; fx avg `-0.0285` n `6`; index avg `-0.0025` n `27`; metal avg `0.377` n `20`; unknown avg `4.6496` n `1197`
- 24h: commodity avg `0.3931` n `13`; crypto_alt avg `1.9867` n `239`; crypto_major avg `0.7183` n `8`; equity avg `-0.607` n `168`; fx avg `0.0322` n `6`; index avg `-0.086` n `27`; metal avg `0.2544` n `20`; unknown avg `355.7108` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1781`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
