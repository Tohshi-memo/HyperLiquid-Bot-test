# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-15T21:52:28.120827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0234` n `13`; crypto_alt avg `0.1761` n `239`; crypto_major avg `0.3502` n `8`; equity avg `0.0144` n `162`; fx avg `-0.0098` n `6`; index avg `-0.0039` n `27`; metal avg `0.0122` n `20`; unknown avg `0.7609` n `1265`
- 1h: commodity avg `-0.0473` n `13`; crypto_alt avg `-0.2246` n `239`; crypto_major avg `0.0797` n `8`; equity avg `0.0742` n `162`; fx avg `0.0027` n `6`; index avg `-0.0002` n `27`; metal avg `-0.0271` n `20`; unknown avg `2.3952` n `1245`
- 4h: commodity avg `0.011` n `13`; crypto_alt avg `0.6376` n `239`; crypto_major avg `0.9866` n `8`; equity avg `0.5754` n `162`; fx avg `0.0575` n `6`; index avg `0.0528` n `27`; metal avg `0.0815` n `20`; unknown avg `0.8514` n `1233`
- 24h: commodity avg `0.0372` n `13`; crypto_alt avg `2.8988` n `239`; crypto_major avg `3.7455` n `8`; equity avg `1.1469` n `162`; fx avg `0.0299` n `6`; index avg `0.1071` n `27`; metal avg `0.291` n `20`; unknown avg `176.0277` n `1154`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1246`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0774`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
