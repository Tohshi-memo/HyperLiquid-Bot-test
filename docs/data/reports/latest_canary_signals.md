# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-09T20:22:28.999627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0372` n `13`; crypto_alt avg `0.4789` n `235`; crypto_major avg `0.2004` n `8`; equity avg `0.0227` n `150`; fx avg `0.0061` n `6`; index avg `0.0044` n `26`; metal avg `0.0262` n `20`; unknown avg `0.4779` n `1068`
- 1h: commodity avg `0.0301` n `13`; crypto_alt avg `0.0623` n `235`; crypto_major avg `-0.1567` n `8`; equity avg `-0.0657` n `150`; fx avg `0.003` n `6`; index avg `-0.0166` n `26`; metal avg `0.0107` n `20`; unknown avg `0.1185` n `1040`
- 4h: commodity avg `-0.2831` n `13`; crypto_alt avg `-0.2474` n `235`; crypto_major avg `-0.3551` n `8`; equity avg `0.2594` n `150`; fx avg `0.0286` n `6`; index avg `0.026` n `26`; metal avg `0.0409` n `20`; unknown avg `0.8267` n `1032`
- 24h: commodity avg `-0.0442` n `13`; crypto_alt avg `1.4889` n `235`; crypto_major avg `0.3894` n `8`; equity avg `0.8925` n `150`; fx avg `0.0158` n `6`; index avg `0.1368` n `26`; metal avg `0.6052` n `20`; unknown avg `12.9979` n `909`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1596`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.126`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
