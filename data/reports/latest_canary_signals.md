# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T00:52:31.869607+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0094` n `13`; crypto_alt avg `-0.123` n `239`; crypto_major avg `-0.049` n `8`; equity avg `0.0776` n `166`; fx avg `0.0107` n `6`; index avg `0.0215` n `27`; metal avg `0.024` n `20`; unknown avg `158.1111` n `1263`
- 1h: commodity avg `-0.0102` n `13`; crypto_alt avg `-0.2352` n `239`; crypto_major avg `-0.2438` n `8`; equity avg `0.2621` n `166`; fx avg `-0.0036` n `6`; index avg `0.0619` n `27`; metal avg `-0.111` n `20`; unknown avg `-0.1933` n `1251`
- 4h: commodity avg `-0.3829` n `13`; crypto_alt avg `-0.1955` n `239`; crypto_major avg `0.1227` n `8`; equity avg `0.6047` n `166`; fx avg `0.0969` n `6`; index avg `0.1162` n `27`; metal avg `0.24` n `20`; unknown avg `0.4431` n `1198`
- 24h: commodity avg `-0.4908` n `13`; crypto_alt avg `0.5061` n `239`; crypto_major avg `0.8624` n `8`; equity avg `1.3682` n `166`; fx avg `0.0864` n `6`; index avg `0.1748` n `27`; metal avg `0.244` n `20`; unknown avg `242.2738` n `1033`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1721`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1518`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1241`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
