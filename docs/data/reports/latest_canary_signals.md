# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T21:07:27.252833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0536` n `12`; crypto_alt avg `0.0239` n `234`; crypto_major avg `0.047` n `8`; equity avg `-0.0024` n `141`; fx avg `-0.0048` n `6`; index avg `-0.0003` n `26`; metal avg `0.0002` n `20`; unknown avg `0.0078` n `943`
- 1h: commodity avg `0.0603` n `12`; crypto_alt avg `-0.4642` n `234`; crypto_major avg `-0.3067` n `8`; equity avg `0.0616` n `141`; fx avg `-0.02` n `6`; index avg `0.0154` n `26`; metal avg `0.0212` n `20`; unknown avg `6.7268` n `891`
- 4h: commodity avg `0.2979` n `12`; crypto_alt avg `-0.4588` n `234`; crypto_major avg `0.3156` n `8`; equity avg `0.0747` n `141`; fx avg `-0.016` n `6`; index avg `0.052` n `26`; metal avg `0.0962` n `20`; unknown avg `7.2249` n `853`
- 24h: commodity avg `0.6539` n `12`; crypto_alt avg `-3.9094` n `234`; crypto_major avg `-3.6381` n `8`; equity avg `-1.594` n `140`; fx avg `-0.0` n `6`; index avg `-0.3494` n `26`; metal avg `-0.7948` n `20`; unknown avg `574.1055` n `836`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.11`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
