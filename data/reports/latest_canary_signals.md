# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T16:37:31.995962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0005` n `13`; crypto_alt avg `-0.1269` n `239`; crypto_major avg `-0.0447` n `8`; equity avg `-0.0435` n `166`; fx avg `0.0002` n `6`; index avg `0.0018` n `27`; metal avg `0.0008` n `20`; unknown avg `160.2882` n `1263`
- 1h: commodity avg `0.0136` n `13`; crypto_alt avg `0.3512` n `239`; crypto_major avg `0.355` n `8`; equity avg `-0.0044` n `166`; fx avg `0.0159` n `6`; index avg `0.0006` n `27`; metal avg `0.0276` n `20`; unknown avg `163.0628` n `1247`
- 4h: commodity avg `-0.0283` n `13`; crypto_alt avg `0.509` n `239`; crypto_major avg `0.9487` n `8`; equity avg `0.2159` n `166`; fx avg `0.0191` n `6`; index avg `0.0775` n `27`; metal avg `0.0809` n `20`; unknown avg `3.038` n `1239`
- 24h: commodity avg `-0.009` n `13`; crypto_alt avg `1.1604` n `239`; crypto_major avg `1.5072` n `8`; equity avg `0.9471` n `166`; fx avg `0.0131` n `6`; index avg `0.1776` n `27`; metal avg `0.1117` n `20`; unknown avg `3.0928` n `1072`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1423`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
