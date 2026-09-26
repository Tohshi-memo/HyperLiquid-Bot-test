# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T02:38:04.400619+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.031` n `12`; crypto_alt avg `-0.0703` n `234`; crypto_major avg `-0.1279` n `8`; equity avg `-0.024` n `141`; fx avg `0.0044` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0041` n `20`; unknown avg `0.0332` n `961`
- 1h: commodity avg `-0.0716` n `12`; crypto_alt avg `-0.0872` n `234`; crypto_major avg `-0.1412` n `8`; equity avg `0.0417` n `141`; fx avg `-0.0006` n `6`; index avg `0.014` n `26`; metal avg `0.0163` n `20`; unknown avg `15.3636` n `958`
- 4h: commodity avg `0.3038` n `12`; crypto_alt avg `-0.039` n `234`; crypto_major avg `-0.2015` n `8`; equity avg `-0.1593` n `141`; fx avg `0.0009` n `6`; index avg `-0.0433` n `26`; metal avg `-0.0097` n `20`; unknown avg `1.9992` n `952`
- 24h: commodity avg `0.1059` n `12`; crypto_alt avg `3.3646` n `234`; crypto_major avg `1.1886` n `8`; equity avg `-0.2764` n `141`; fx avg `-0.1322` n `6`; index avg `0.1446` n `26`; metal avg `0.1708` n `20`; unknown avg `1126.0036` n `810`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
