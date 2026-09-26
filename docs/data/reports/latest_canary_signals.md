# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T09:37:30.402860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `0.0269` n `234`; crypto_major avg `-0.0345` n `8`; equity avg `0.0091` n `141`; fx avg `-0.0015` n `6`; index avg `-0.0003` n `26`; metal avg `0.0028` n `20`; unknown avg `0.0703` n `961`
- 1h: commodity avg `0.0003` n `12`; crypto_alt avg `-0.5075` n `234`; crypto_major avg `-0.5852` n `8`; equity avg `-0.0496` n `141`; fx avg `-0.0062` n `6`; index avg `0.0023` n `26`; metal avg `0.0038` n `20`; unknown avg `0.218` n `959`
- 4h: commodity avg `-0.0476` n `12`; crypto_alt avg `0.3619` n `234`; crypto_major avg `-0.247` n `8`; equity avg `-0.0061` n `141`; fx avg `0.0144` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0054` n `20`; unknown avg `0.0024` n `919`
- 24h: commodity avg `0.0875` n `12`; crypto_alt avg `1.7512` n `234`; crypto_major avg `-0.6028` n `8`; equity avg `-1.0214` n `141`; fx avg `-0.0446` n `6`; index avg `-0.0065` n `26`; metal avg `0.0288` n `20`; unknown avg `1121.5555` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1569`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
