# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T14:26:12.355631+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `12`; crypto_alt avg `0.1122` n `234`; crypto_major avg `0.1149` n `8`; equity avg `0.0354` n `141`; fx avg `-0.0042` n `6`; index avg `0.003` n `26`; metal avg `0.0031` n `20`; unknown avg `0.0882` n `961`
- 1h: commodity avg `0.0499` n `12`; crypto_alt avg `0.3485` n `234`; crypto_major avg `0.1493` n `8`; equity avg `0.0131` n `141`; fx avg `0.0005` n `6`; index avg `0.0104` n `26`; metal avg `0.0034` n `20`; unknown avg `1.5509` n `959`
- 4h: commodity avg `0.043` n `12`; crypto_alt avg `0.0992` n `234`; crypto_major avg `-0.046` n `8`; equity avg `0.0535` n `141`; fx avg `0.0181` n `6`; index avg `0.0041` n `26`; metal avg `0.003` n `20`; unknown avg `2.0042` n `949`
- 24h: commodity avg `0.2254` n `12`; crypto_alt avg `2.6877` n `234`; crypto_major avg `-0.114` n `8`; equity avg `0.4037` n `141`; fx avg `-0.0121` n `6`; index avg `0.1366` n `26`; metal avg `0.2255` n `20`; unknown avg `2.3298` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1518`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
