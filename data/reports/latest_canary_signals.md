# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T04:37:33.165622+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0032` n `13`; crypto_alt avg `-0.251` n `239`; crypto_major avg `-0.3184` n `8`; equity avg `-0.1659` n `166`; fx avg `0.0038` n `6`; index avg `-0.0206` n `27`; metal avg `0.0036` n `20`; unknown avg `0.9265` n `1266`
- 1h: commodity avg `0.0591` n `13`; crypto_alt avg `-0.2533` n `239`; crypto_major avg `-0.5182` n `8`; equity avg `-0.2893` n `166`; fx avg `0.0385` n `6`; index avg `-0.0706` n `27`; metal avg `-0.0438` n `20`; unknown avg `10.832` n `1252`
- 4h: commodity avg `0.0815` n `13`; crypto_alt avg `0.3152` n `239`; crypto_major avg `0.2577` n `8`; equity avg `0.2221` n `166`; fx avg `0.1566` n `6`; index avg `-0.0774` n `27`; metal avg `0.0572` n `20`; unknown avg `164.3523` n `1239`
- 24h: commodity avg `-0.3036` n `13`; crypto_alt avg `1.6823` n `239`; crypto_major avg `2.3972` n `8`; equity avg `1.9649` n `166`; fx avg `0.2465` n `6`; index avg `0.1549` n `27`; metal avg `0.3824` n `20`; unknown avg `294.0886` n `1023`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1483`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1409`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
