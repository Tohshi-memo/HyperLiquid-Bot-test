# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T20:37:27.930346+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.009` n `12`; crypto_alt avg `-0.1025` n `234`; crypto_major avg `0.0465` n `8`; equity avg `0.0204` n `141`; fx avg `0.0007` n `6`; index avg `-0.0009` n `26`; metal avg `0.0039` n `20`; unknown avg `6.6999` n `961`
- 1h: commodity avg `0.0194` n `12`; crypto_alt avg `-0.4325` n `234`; crypto_major avg `-0.0426` n `8`; equity avg `0.0296` n `141`; fx avg `-0.0039` n `6`; index avg `-0.0025` n `26`; metal avg `0.0047` n `20`; unknown avg `164.3724` n `953`
- 4h: commodity avg `0.0356` n `12`; crypto_alt avg `-1.7505` n `234`; crypto_major avg `-0.7221` n `8`; equity avg `-0.0618` n `141`; fx avg `-0.0021` n `6`; index avg `-0.0189` n `26`; metal avg `0.0083` n `20`; unknown avg `12.485` n `953`
- 24h: commodity avg `0.286` n `12`; crypto_alt avg `0.2784` n `234`; crypto_major avg `-0.9177` n `8`; equity avg `0.0173` n `141`; fx avg `0.0138` n `6`; index avg `-0.0414` n `26`; metal avg `-0.0109` n `20`; unknown avg `4.5293` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1285`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
