# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T02:37:27.394356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.1885` n `239`; crypto_major avg `-0.2284` n `8`; equity avg `-0.469` n `166`; fx avg `-0.002` n `6`; index avg `-0.0359` n `27`; metal avg `-0.0832` n `20`; unknown avg `0.2539` n `1263`
- 1h: commodity avg `-0.0398` n `13`; crypto_alt avg `-0.5416` n `239`; crypto_major avg `-0.5729` n `8`; equity avg `-0.9748` n `166`; fx avg `0.0253` n `6`; index avg `-0.1309` n `27`; metal avg `-0.2844` n `20`; unknown avg `159.0646` n `1257`
- 4h: commodity avg `-0.3145` n `13`; crypto_alt avg `-0.4166` n `239`; crypto_major avg `-0.3919` n `8`; equity avg `-0.28` n `166`; fx avg `0.113` n `6`; index avg `0.009` n `27`; metal avg `0.0149` n `20`; unknown avg `44.2629` n `1228`
- 24h: commodity avg `-0.4376` n `13`; crypto_alt avg `0.42` n `239`; crypto_major avg `0.7534` n `8`; equity avg `0.5331` n `166`; fx avg `0.1813` n `6`; index avg `0.0842` n `27`; metal avg `0.0375` n `20`; unknown avg `243.7265` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1631`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1438`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
