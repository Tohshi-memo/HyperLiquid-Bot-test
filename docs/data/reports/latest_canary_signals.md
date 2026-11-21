# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T17:07:25.940247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0121` n `13`; crypto_alt avg `0.085` n `239`; crypto_major avg `0.0867` n `8`; equity avg `0.0514` n `166`; fx avg `0.0119` n `6`; index avg `0.0076` n `27`; metal avg `0.0174` n `20`; unknown avg `2.5572` n `1254`
- 1h: commodity avg `0.0224` n `13`; crypto_alt avg `-0.0271` n `239`; crypto_major avg `0.3748` n `8`; equity avg `0.0389` n `166`; fx avg `0.007` n `6`; index avg `0.0021` n `27`; metal avg `0.0235` n `20`; unknown avg `2.2016` n `1252`
- 4h: commodity avg `-0.006` n `13`; crypto_alt avg `0.9045` n `239`; crypto_major avg `1.141` n `8`; equity avg `0.6159` n `166`; fx avg `0.016` n `6`; index avg `0.0544` n `27`; metal avg `0.0797` n `20`; unknown avg `1.9629` n `1244`
- 24h: commodity avg `0.482` n `13`; crypto_alt avg `1.3394` n `239`; crypto_major avg `1.6376` n `8`; equity avg `0.5127` n `166`; fx avg `-0.1229` n `6`; index avg `-0.0243` n `27`; metal avg `0.1425` n `20`; unknown avg `0.2472` n `1141`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1495`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1061`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
