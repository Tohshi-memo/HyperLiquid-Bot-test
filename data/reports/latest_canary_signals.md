# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T16:07:23.964493+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0084` n `13`; crypto_alt avg `0.0977` n `239`; crypto_major avg `0.0368` n `8`; equity avg `-0.0131` n `166`; fx avg `0.0072` n `6`; index avg `0.0007` n `27`; metal avg `0.0194` n `20`; unknown avg `2.9968` n `1239`
- 1h: commodity avg `-0.0122` n `13`; crypto_alt avg `0.1797` n `239`; crypto_major avg `0.1474` n `8`; equity avg `-0.0793` n `166`; fx avg `0.0098` n `6`; index avg `-0.023` n `27`; metal avg `0.0336` n `20`; unknown avg `1.9946` n `1245`
- 4h: commodity avg `-0.0621` n `13`; crypto_alt avg `-0.028` n `239`; crypto_major avg `0.0499` n `8`; equity avg `-0.0909` n `166`; fx avg `0.015` n `6`; index avg `0.0427` n `27`; metal avg `0.0287` n `20`; unknown avg `164.0982` n `1237`
- 24h: commodity avg `-0.0168` n `13`; crypto_alt avg `0.9289` n `239`; crypto_major avg `1.3382` n `8`; equity avg `0.8768` n `166`; fx avg `0.0082` n `6`; index avg `0.1575` n `27`; metal avg `0.0891` n `20`; unknown avg `0.5429` n `1068`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1278`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
