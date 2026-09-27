# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T04:07:26.190166+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.1999` n `234`; crypto_major avg `-0.0024` n `8`; equity avg `0.0102` n `141`; fx avg `0.0` n `6`; index avg `0.0024` n `26`; metal avg `0.0028` n `20`; unknown avg `-0.1345` n `953`
- 1h: commodity avg `-0.0054` n `12`; crypto_alt avg `-0.2866` n `234`; crypto_major avg `-0.2218` n `8`; equity avg `-0.0063` n `141`; fx avg `-0.002` n `6`; index avg `0.0062` n `26`; metal avg `-0.0032` n `20`; unknown avg `23.9314` n `953`
- 4h: commodity avg `-0.0277` n `12`; crypto_alt avg `-0.3033` n `234`; crypto_major avg `-0.0606` n `8`; equity avg `0.0618` n `141`; fx avg `-0.0045` n `6`; index avg `0.0035` n `26`; metal avg `-0.0045` n `20`; unknown avg `-0.3864` n `947`
- 24h: commodity avg `-0.0132` n `12`; crypto_alt avg `0.3427` n `234`; crypto_major avg `-0.4253` n `8`; equity avg `0.2469` n `141`; fx avg `0.0079` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0049` n `20`; unknown avg `1.1396` n `881`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
