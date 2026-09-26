# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T20:52:25.839898+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1066` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0198` n `12`; crypto_alt avg `-0.7587` n `234`; crypto_major avg `-0.442` n `8`; equity avg `-0.088` n `141`; fx avg `-0.0061` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0063` n `20`; unknown avg `-0.1749` n `961`
- 1h: commodity avg `-0.0223` n `12`; crypto_alt avg `-1.212` n `234`; crypto_major avg `-0.5099` n `8`; equity avg `-0.0807` n `141`; fx avg `-0.0186` n `6`; index avg `-0.0104` n `26`; metal avg `-0.0017` n `20`; unknown avg `163.4455` n `953`
- 4h: commodity avg `0.0044` n `12`; crypto_alt avg `-2.3738` n `234`; crypto_major avg `-1.1341` n `8`; equity avg `-0.1448` n `141`; fx avg `-0.005` n `6`; index avg `-0.0275` n `26`; metal avg `0.0025` n `20`; unknown avg `4.0271` n `953`
- 24h: commodity avg `0.2926` n `12`; crypto_alt avg `-0.1883` n `234`; crypto_major avg `-1.1656` n `8`; equity avg `-0.0807` n `141`; fx avg `0.0118` n `6`; index avg `-0.0483` n `26`; metal avg `-0.0368` n `20`; unknown avg `4.2339` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1585`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1503`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
