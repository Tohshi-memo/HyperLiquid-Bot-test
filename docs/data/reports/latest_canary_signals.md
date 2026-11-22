# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T22:37:23.002345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.004` n `13`; crypto_alt avg `-0.1562` n `239`; crypto_major avg `-0.1903` n `8`; equity avg `-0.0468` n `166`; fx avg `-0.0195` n `6`; index avg `-0.0076` n `27`; metal avg `-0.0147` n `20`; unknown avg `0.3447` n `1264`
- 1h: commodity avg `-0.0184` n `13`; crypto_alt avg `-0.486` n `239`; crypto_major avg `-0.4209` n `8`; equity avg `-0.2663` n `166`; fx avg `0.0297` n `6`; index avg `-0.0334` n `27`; metal avg `-0.0368` n `20`; unknown avg `-0.2831` n `1238`
- 4h: commodity avg `-0.0439` n `13`; crypto_alt avg `-0.0849` n `239`; crypto_major avg `-0.3744` n `8`; equity avg `-0.2526` n `166`; fx avg `0.077` n `6`; index avg `-0.0637` n `27`; metal avg `-0.0908` n `20`; unknown avg `-0.1505` n `1208`
- 24h: commodity avg `-0.1569` n `13`; crypto_alt avg `0.3767` n `239`; crypto_major avg `0.5536` n `8`; equity avg `0.6283` n `166`; fx avg `0.0662` n `6`; index avg `0.0585` n `27`; metal avg `-0.0026` n `20`; unknown avg `191.8181` n `1046`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1581`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.146`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
