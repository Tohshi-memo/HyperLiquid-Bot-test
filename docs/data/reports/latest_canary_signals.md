# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T09:22:37.107590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0161` n `12`; crypto_alt avg `-0.3688` n `234`; crypto_major avg `-0.3097` n `8`; equity avg `-0.0776` n `141`; fx avg `0.0` n `6`; index avg `-0.0027` n `26`; metal avg `-0.0071` n `20`; unknown avg `0.0972` n `961`
- 1h: commodity avg `-0.009` n `12`; crypto_alt avg `-0.1542` n `234`; crypto_major avg `-0.2071` n `8`; equity avg `-0.0385` n `141`; fx avg `-0.0025` n `6`; index avg `0.0028` n `26`; metal avg `0.0005` n `20`; unknown avg `-0.0486` n `959`
- 4h: commodity avg `-0.0471` n `12`; crypto_alt avg `0.3536` n `234`; crypto_major avg `-0.3006` n `8`; equity avg `-0.0373` n `141`; fx avg `0.0166` n `6`; index avg `-0.0062` n `26`; metal avg `-0.0094` n `20`; unknown avg `-0.0782` n `919`
- 24h: commodity avg `0.0758` n `12`; crypto_alt avg `1.9768` n `234`; crypto_major avg `-0.2236` n `8`; equity avg `-1.0373` n `141`; fx avg `-0.0321` n `6`; index avg `-0.0116` n `26`; metal avg `0.0283` n `20`; unknown avg `1122.7652` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1488`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
