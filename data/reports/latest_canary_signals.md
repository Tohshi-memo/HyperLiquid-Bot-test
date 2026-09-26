# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T12:37:29.831548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0057` n `12`; crypto_alt avg `-0.3101` n `234`; crypto_major avg `-0.0969` n `8`; equity avg `-0.0134` n `141`; fx avg `-0.0003` n `6`; index avg `-0.003` n `26`; metal avg `-0.0038` n `20`; unknown avg `3.0423` n `961`
- 1h: commodity avg `0.0405` n `12`; crypto_alt avg `-0.3222` n `234`; crypto_major avg `-0.1987` n `8`; equity avg `-0.0139` n `141`; fx avg `-0.0123` n `6`; index avg `-0.0073` n `26`; metal avg `-0.0041` n `20`; unknown avg `3.537` n `949`
- 4h: commodity avg `0.0379` n `12`; crypto_alt avg `0.1043` n `234`; crypto_major avg `-0.2799` n `8`; equity avg `0.025` n `141`; fx avg `0.0125` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0006` n `20`; unknown avg `2.9387` n `949`
- 24h: commodity avg `0.0703` n `12`; crypto_alt avg `1.5822` n `234`; crypto_major avg `-1.1585` n `8`; equity avg `-0.7905` n `141`; fx avg `-0.0579` n `6`; index avg `0.0033` n `26`; metal avg `-0.07` n `20`; unknown avg `1122.027` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
