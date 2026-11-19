# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T07:52:29.606775+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.01` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0447` n `13`; crypto_alt avg `0.0546` n `239`; crypto_major avg `0.0083` n `8`; equity avg `-0.0174` n `164`; fx avg `-0.0016` n `6`; index avg `-0.0035` n `27`; metal avg `-0.0224` n `20`; unknown avg `35.1442` n `1260`
- 1h: commodity avg `0.012` n `13`; crypto_alt avg `0.0249` n `239`; crypto_major avg `-0.1003` n `8`; equity avg `0.2746` n `164`; fx avg `0.0549` n `6`; index avg `0.0408` n `27`; metal avg `-0.0175` n `20`; unknown avg `35.435` n `1254`
- 4h: commodity avg `0.013` n `13`; crypto_alt avg `0.3222` n `239`; crypto_major avg `1.0059` n `8`; equity avg `1.0128` n `164`; fx avg `0.0614` n `6`; index avg `0.1664` n `27`; metal avg `0.1526` n `20`; unknown avg `2.5635` n `1214`
- 24h: commodity avg `0.2317` n `13`; crypto_alt avg `-0.0976` n `239`; crypto_major avg `-0.9624` n `8`; equity avg `-0.1019` n `164`; fx avg `-0.0069` n `6`; index avg `0.1402` n `27`; metal avg `-0.3361` n `20`; unknown avg `97.0542` n `1105`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1656`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0528`, n `668`, weak_sample_signal
