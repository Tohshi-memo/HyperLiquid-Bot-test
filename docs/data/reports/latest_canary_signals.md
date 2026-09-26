# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T09:07:32.922073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0004` n `12`; crypto_alt avg `-0.1042` n `234`; crypto_major avg `-0.0684` n `8`; equity avg `0.025` n `141`; fx avg `0.0277` n `6`; index avg `0.0041` n `26`; metal avg `0.0044` n `20`; unknown avg `-0.0192` n `959`
- 1h: commodity avg `-0.024` n `12`; crypto_alt avg `0.1061` n `234`; crypto_major avg `0.0387` n `8`; equity avg `0.04` n `141`; fx avg `-0.0025` n `6`; index avg `0.0062` n `26`; metal avg `0.0031` n `20`; unknown avg `0.1022` n `959`
- 4h: commodity avg `-0.046` n `12`; crypto_alt avg `0.6827` n `234`; crypto_major avg `-0.0587` n `8`; equity avg `0.0057` n `141`; fx avg `0.0117` n `6`; index avg `-0.0068` n `26`; metal avg `-0.0018` n `20`; unknown avg `-0.0268` n `919`
- 24h: commodity avg `0.2215` n `12`; crypto_alt avg `2.1405` n `234`; crypto_major avg `-0.0305` n `8`; equity avg `-0.9638` n `141`; fx avg `-0.0477` n `6`; index avg `-0.0179` n `26`; metal avg `0.0191` n `20`; unknown avg `1123.4097` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1795`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1567`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1341`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
