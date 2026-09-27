# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T00:37:27.186923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0455` n `12`; crypto_alt avg `0.0626` n `234`; crypto_major avg `0.0923` n `8`; equity avg `0.0032` n `141`; fx avg `-0.0002` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0054` n `20`; unknown avg `9.7498` n `961`
- 1h: commodity avg `-0.0815` n `12`; crypto_alt avg `-0.177` n `234`; crypto_major avg `-0.1185` n `8`; equity avg `0.0397` n `141`; fx avg `0.0038` n `6`; index avg `0.0028` n `26`; metal avg `-0.0023` n `20`; unknown avg `10.1387` n `951`
- 4h: commodity avg `-0.0483` n `12`; crypto_alt avg `0.2737` n `234`; crypto_major avg `0.2582` n `8`; equity avg `0.0784` n `141`; fx avg `-0.0095` n `6`; index avg `0.0015` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.19` n `927`
- 24h: commodity avg `-0.3439` n `12`; crypto_alt avg `0.8361` n `234`; crypto_major avg `-0.2341` n `8`; equity avg `0.293` n `141`; fx avg `0.0225` n `6`; index avg `0.038` n `26`; metal avg `0.021` n `20`; unknown avg `5.0456` n `886`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0972`, n `668`, weak_sample_signal
