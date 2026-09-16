# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T03:07:36.393023+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `-0.0934` n `234`; crypto_major avg `-0.1228` n `8`; equity avg `0.1532` n `137`; fx avg `0.0052` n `6`; index avg `0.0232` n `27`; metal avg `0.0783` n `20`; unknown avg `1.1484` n `917`
- 1h: commodity avg `-0.1021` n `12`; crypto_alt avg `0.5117` n `234`; crypto_major avg `0.4717` n `8`; equity avg `0.5326` n `137`; fx avg `-0.0427` n `6`; index avg `0.0723` n `27`; metal avg `0.3051` n `20`; unknown avg `7.2081` n `913`
- 4h: commodity avg `-0.1509` n `12`; crypto_alt avg `-0.4154` n `234`; crypto_major avg `-0.0174` n `8`; equity avg `0.4103` n `137`; fx avg `0.074` n `6`; index avg `0.0615` n `27`; metal avg `0.2532` n `20`; unknown avg `5.4757` n `907`
- 24h: commodity avg `0.2104` n `12`; crypto_alt avg `-3.8239` n `234`; crypto_major avg `-3.5553` n `8`; equity avg `-1.0816` n `137`; fx avg `0.2147` n `6`; index avg `-0.0957` n `27`; metal avg `0.3115` n `20`; unknown avg `1.6818` n `798`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
