# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-23T10:52:32.982945+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1153` n `13`; crypto_alt avg `0.0708` n `239`; crypto_major avg `0.1115` n `8`; equity avg `0.1706` n `166`; fx avg `0.0075` n `6`; index avg `0.026` n `27`; metal avg `0.0784` n `20`; unknown avg `0.1846` n `1266`
- 1h: commodity avg `-0.2006` n `13`; crypto_alt avg `0.1976` n `239`; crypto_major avg `0.3641` n `8`; equity avg `0.1087` n `166`; fx avg `-0.0244` n `6`; index avg `0.0481` n `27`; metal avg `0.0506` n `20`; unknown avg `0.1491` n `1260`
- 4h: commodity avg `-0.3711` n `13`; crypto_alt avg `0.1665` n `239`; crypto_major avg `0.3213` n `8`; equity avg `0.8837` n `166`; fx avg `-0.035` n `6`; index avg `0.1022` n `27`; metal avg `0.0186` n `20`; unknown avg `45.1228` n `1106`
- 24h: commodity avg `-0.9031` n `13`; crypto_alt avg `0.8001` n `239`; crypto_major avg `1.2594` n `8`; equity avg `2.2989` n `166`; fx avg `0.2047` n `6`; index avg `0.1491` n `27`; metal avg `0.4307` n `20`; unknown avg `0.0303` n `1059`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1523`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
