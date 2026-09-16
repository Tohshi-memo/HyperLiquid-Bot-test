# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T21:07:33.413170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0147` n `12`; crypto_alt avg `0.1274` n `234`; crypto_major avg `0.0296` n `8`; equity avg `0.026` n `137`; fx avg `-0.0234` n `6`; index avg `0.003` n `27`; metal avg `0.0157` n `20`; unknown avg `0.6361` n `917`
- 1h: commodity avg `0.0396` n `12`; crypto_alt avg `0.2703` n `234`; crypto_major avg `-0.2006` n `8`; equity avg `0.0931` n `137`; fx avg `-0.0167` n `6`; index avg `0.0136` n `27`; metal avg `0.0071` n `20`; unknown avg `2.3649` n `883`
- 4h: commodity avg `-0.0065` n `12`; crypto_alt avg `1.3639` n `234`; crypto_major avg `1.0188` n `8`; equity avg `-0.4366` n `137`; fx avg `0.0566` n `6`; index avg `-0.1732` n `27`; metal avg `-0.4779` n `20`; unknown avg `2.5804` n `829`
- 24h: commodity avg `-0.5917` n `12`; crypto_alt avg `0.184` n `234`; crypto_major avg `0.8618` n `8`; equity avg `0.7745` n `137`; fx avg `0.0924` n `6`; index avg `0.0197` n `27`; metal avg `-0.2795` n `20`; unknown avg `1.4614` n `771`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0949`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0874`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
