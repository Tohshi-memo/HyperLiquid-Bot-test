# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T21:52:27.998871+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0114` n `13`; crypto_alt avg `0.011` n `239`; crypto_major avg `0.0195` n `8`; equity avg `0.0769` n `166`; fx avg `0.001` n `6`; index avg `0.0373` n `27`; metal avg `0.0071` n `20`; unknown avg `-0.2602` n `1262`
- 1h: commodity avg `-0.0464` n `13`; crypto_alt avg `0.0399` n `239`; crypto_major avg `0.126` n `8`; equity avg `0.1292` n `166`; fx avg `0.0517` n `6`; index avg `0.0366` n `27`; metal avg `0.0112` n `20`; unknown avg `0.1918` n `1240`
- 4h: commodity avg `-0.0487` n `13`; crypto_alt avg `-0.2299` n `239`; crypto_major avg `-0.052` n `8`; equity avg `0.1292` n `166`; fx avg `0.0514` n `6`; index avg `0.0117` n `27`; metal avg `-0.0719` n `20`; unknown avg `1.0831` n `1217`
- 24h: commodity avg `-0.157` n `13`; crypto_alt avg `0.7876` n `239`; crypto_major avg `0.7161` n `8`; equity avg `0.905` n `166`; fx avg `0.0361` n `6`; index avg `0.122` n `27`; metal avg `-0.0051` n `20`; unknown avg `191.2206` n `1056`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1434`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1244`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
