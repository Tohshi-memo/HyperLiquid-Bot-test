# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T04:22:26.989283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `13`; crypto_alt avg `0.3276` n `239`; crypto_major avg `0.2821` n `8`; equity avg `0.0764` n `166`; fx avg `0.0055` n `6`; index avg `0.0319` n `27`; metal avg `0.0378` n `20`; unknown avg `-0.2573` n `1260`
- 1h: commodity avg `0.0562` n `13`; crypto_alt avg `0.0211` n `239`; crypto_major avg `-0.2159` n `8`; equity avg `0.134` n `166`; fx avg `0.0485` n `6`; index avg `-0.0497` n `27`; metal avg `-0.0358` n `20`; unknown avg `0.3738` n `1252`
- 4h: commodity avg `0.1064` n `13`; crypto_alt avg `0.5671` n `239`; crypto_major avg `0.528` n `8`; equity avg `0.4348` n `166`; fx avg `0.165` n `6`; index avg `-0.0653` n `27`; metal avg `-0.0023` n `20`; unknown avg `2.9794` n `1241`
- 24h: commodity avg `-0.2801` n `13`; crypto_alt avg `2.0804` n `239`; crypto_major avg `2.8021` n `8`; equity avg `2.1816` n `166`; fx avg `0.2266` n `6`; index avg `0.1774` n `27`; metal avg `0.3932` n `20`; unknown avg `245.4196` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.148`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1382`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1239`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1185`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
