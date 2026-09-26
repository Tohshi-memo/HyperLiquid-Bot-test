# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T23:07:28.829820+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0358` n `12`; crypto_alt avg `0.1493` n `234`; crypto_major avg `0.0692` n `8`; equity avg `-0.0048` n `141`; fx avg `-0.0013` n `6`; index avg `-0.0016` n `26`; metal avg `-0.0008` n `20`; unknown avg `1.2424` n `959`
- 1h: commodity avg `0.0331` n `12`; crypto_alt avg `0.0809` n `234`; crypto_major avg `-0.0174` n `8`; equity avg `0.0232` n `141`; fx avg `0.0015` n `6`; index avg `0.0015` n `26`; metal avg `-0.0037` n `20`; unknown avg `3.1304` n `959`
- 4h: commodity avg `0.0804` n `12`; crypto_alt avg `-0.3027` n `234`; crypto_major avg `0.0681` n `8`; equity avg `0.0587` n `141`; fx avg `-0.0162` n `6`; index avg `-0.0061` n `26`; metal avg `0.0057` n `20`; unknown avg `163.0385` n `929`
- 24h: commodity avg `0.3448` n `12`; crypto_alt avg `0.5741` n `234`; crypto_major avg `-0.8456` n `8`; equity avg `-0.0128` n `141`; fx avg `0.0121` n `6`; index avg `-0.0573` n `26`; metal avg `-0.0196` n `20`; unknown avg `4.4388` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1298`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
