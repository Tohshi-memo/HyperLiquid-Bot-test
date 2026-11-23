# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T05:52:22.891411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0091` n `13`; crypto_alt avg `0.163` n `239`; crypto_major avg `0.1693` n `8`; equity avg `0.265` n `166`; fx avg `0.0055` n `6`; index avg `0.0212` n `27`; metal avg `0.0366` n `20`; unknown avg `65.6528` n `1266`
- 1h: commodity avg `0.0452` n `13`; crypto_alt avg `0.5875` n `239`; crypto_major avg `0.6566` n `8`; equity avg `0.5704` n `166`; fx avg `0.0017` n `6`; index avg `0.0347` n `27`; metal avg `0.1797` n `20`; unknown avg `23.8763` n `1256`
- 4h: commodity avg `0.0398` n `13`; crypto_alt avg `1.3128` n `239`; crypto_major avg `1.4395` n `8`; equity avg `0.905` n `166`; fx avg `0.0362` n `6`; index avg `-0.0105` n `27`; metal avg `0.2198` n `20`; unknown avg `167.0026` n `1243`
- 24h: commodity avg `-0.2839` n `13`; crypto_alt avg `2.5459` n `239`; crypto_major avg `3.6471` n `8`; equity avg `2.6962` n `166`; fx avg `0.2107` n `6`; index avg `0.2228` n `27`; metal avg `0.6019` n `20`; unknown avg `489.0282` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
