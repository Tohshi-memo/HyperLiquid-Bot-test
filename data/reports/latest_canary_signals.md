# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T08:37:25.802652+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `-0.0003` n `234`; crypto_major avg `0.0528` n `8`; equity avg `0.0203` n `141`; fx avg `0.0039` n `6`; index avg `0.0029` n `26`; metal avg `-0.0025` n `20`; unknown avg `-0.0005` n `961`
- 1h: commodity avg `-0.0016` n `12`; crypto_alt avg `0.2772` n `234`; crypto_major avg `0.5775` n `8`; equity avg `0.0896` n `141`; fx avg `-0.0069` n `6`; index avg `0.0218` n `26`; metal avg `-0.0032` n `20`; unknown avg `1.724` n `943`
- 4h: commodity avg `-0.0221` n `12`; crypto_alt avg `1.7417` n `234`; crypto_major avg `1.2823` n `8`; equity avg `0.169` n `141`; fx avg `0.0032` n `6`; index avg `0.0303` n `26`; metal avg `0.0056` n `20`; unknown avg `4.6465` n `923`
- 24h: commodity avg `0.037` n `12`; crypto_alt avg `1.2084` n `234`; crypto_major avg `0.6455` n `8`; equity avg `0.3784` n `141`; fx avg `-0.0095` n `6`; index avg `0.0366` n `26`; metal avg `0.0032` n `20`; unknown avg `6.4266` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
