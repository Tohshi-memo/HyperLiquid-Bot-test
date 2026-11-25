# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T23:07:26.172533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `13`; crypto_alt avg `-0.2191` n `239`; crypto_major avg `-0.3474` n `8`; equity avg `-0.3557` n `168`; fx avg `0.0063` n `6`; index avg `-0.0193` n `27`; metal avg `-0.1074` n `20`; unknown avg `0.1218` n `1207`
- 1h: commodity avg `-0.0386` n `13`; crypto_alt avg `-0.1823` n `239`; crypto_major avg `-0.3868` n `8`; equity avg `0.0378` n `168`; fx avg `0.0034` n `6`; index avg `-0.0197` n `27`; metal avg `-0.0913` n `20`; unknown avg `-0.1468` n `1199`
- 4h: commodity avg `0.0261` n `13`; crypto_alt avg `0.241` n `239`; crypto_major avg `0.0373` n `8`; equity avg `-0.1199` n `168`; fx avg `-0.0147` n `6`; index avg `-0.0389` n `27`; metal avg `0.1655` n `20`; unknown avg `179.3006` n `1141`
- 24h: commodity avg `0.3851` n `13`; crypto_alt avg `1.9073` n `239`; crypto_major avg `0.3682` n `8`; equity avg `-1.0783` n `168`; fx avg `0.0463` n `6`; index avg `-0.1311` n `27`; metal avg `0.137` n `20`; unknown avg `770.8543` n `1017`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1794`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1279`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.086`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
