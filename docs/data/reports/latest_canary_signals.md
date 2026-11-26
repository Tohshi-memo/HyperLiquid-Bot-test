# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T08:22:26.211408+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0747` n `13`; crypto_alt avg `0.0666` n `239`; crypto_major avg `-0.0041` n `8`; equity avg `-0.2205` n `168`; fx avg `-0.0139` n `6`; index avg `-0.0125` n `27`; metal avg `-0.0331` n `20`; unknown avg `0.1486` n `1243`
- 1h: commodity avg `0.1579` n `13`; crypto_alt avg `0.0929` n `239`; crypto_major avg `0.0049` n `8`; equity avg `-0.2303` n `168`; fx avg `0.0077` n `6`; index avg `-0.0225` n `27`; metal avg `-0.0603` n `20`; unknown avg `0.5377` n `1225`
- 4h: commodity avg `-0.1825` n `13`; crypto_alt avg `-0.3263` n `239`; crypto_major avg `-0.6204` n `8`; equity avg `-0.895` n `168`; fx avg `0.0368` n `6`; index avg `-0.092` n `27`; metal avg `-0.2055` n `20`; unknown avg `0.2843` n `1205`
- 24h: commodity avg `0.86` n `13`; crypto_alt avg `3.1117` n `239`; crypto_major avg `3.3074` n `8`; equity avg `2.7714` n `168`; fx avg `0.0775` n `6`; index avg `0.2123` n `27`; metal avg `0.6191` n `20`; unknown avg `765.2013` n `1025`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
