# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T01:07:23.375506+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `13`; crypto_alt avg `0.018` n `239`; crypto_major avg `0.0443` n `8`; equity avg `0.0562` n `166`; fx avg `-0.0205` n `6`; index avg `0.0009` n `27`; metal avg `0.0041` n `20`; unknown avg `208.2763` n `1255`
- 1h: commodity avg `0.009` n `13`; crypto_alt avg `-0.0775` n `239`; crypto_major avg `-0.0012` n `8`; equity avg `0.0439` n `166`; fx avg `-0.0313` n `6`; index avg `0.0087` n `27`; metal avg `0.0012` n `20`; unknown avg `990.4022` n `1257`
- 4h: commodity avg `-0.0083` n `13`; crypto_alt avg `-0.1086` n `239`; crypto_major avg `-0.1929` n `8`; equity avg `0.1303` n `166`; fx avg `-0.0111` n `6`; index avg `0.0328` n `27`; metal avg `-0.0362` n `20`; unknown avg `1013.2465` n `1230`
- 24h: commodity avg `0.0581` n `13`; crypto_alt avg `0.4704` n `239`; crypto_major avg `1.8975` n `8`; equity avg `0.5766` n `166`; fx avg `-0.067` n `6`; index avg `0.1582` n `27`; metal avg `0.0948` n `20`; unknown avg `1387.2789` n `1078`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1478`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1117`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1047`, n `668`, weak_sample_signal
