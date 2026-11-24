# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T01:52:30.797224+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0248` n `13`; crypto_alt avg `-0.2857` n `239`; crypto_major avg `-0.48` n `8`; equity avg `-0.3863` n `166`; fx avg `0.0145` n `6`; index avg `-0.0498` n `27`; metal avg `-0.1037` n `20`; unknown avg `1.4952` n `1266`
- 1h: commodity avg `-0.1255` n `13`; crypto_alt avg `0.3416` n `239`; crypto_major avg `0.1813` n `8`; equity avg `-0.0706` n `166`; fx avg `0.0377` n `6`; index avg `0.035` n `27`; metal avg `-0.0486` n `20`; unknown avg `158.1189` n `1264`
- 4h: commodity avg `-0.0833` n `13`; crypto_alt avg `0.3375` n `239`; crypto_major avg `0.0325` n `8`; equity avg `0.1965` n `166`; fx avg `0.1025` n `6`; index avg `0.1063` n `27`; metal avg `0.1886` n `20`; unknown avg `-0.5398` n `1246`
- 24h: commodity avg `-1.215` n `13`; crypto_alt avg `1.6672` n `239`; crypto_major avg `1.6379` n `8`; equity avg `5.6855` n `166`; fx avg `-0.1774` n `6`; index avg `0.6074` n `27`; metal avg `0.4915` n `20`; unknown avg `240.9336` n `1047`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
