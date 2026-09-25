# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T10:07:28.582031+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0205` n `12`; crypto_alt avg `-0.1456` n `234`; crypto_major avg `-0.2279` n `8`; equity avg `-0.0425` n `141`; fx avg `-0.01` n `6`; index avg `-0.0038` n `26`; metal avg `0.0562` n `20`; unknown avg `0.1478` n `944`
- 1h: commodity avg `0.1393` n `12`; crypto_alt avg `-0.1905` n `234`; crypto_major avg `-0.2102` n `8`; equity avg `-0.1818` n `141`; fx avg `0.0036` n `6`; index avg `-0.0324` n `26`; metal avg `0.0145` n `20`; unknown avg `1.6037` n `944`
- 4h: commodity avg `-0.006` n `12`; crypto_alt avg `1.4055` n `234`; crypto_major avg `0.7306` n `8`; equity avg `0.2363` n `141`; fx avg `-0.0505` n `6`; index avg `0.0598` n `26`; metal avg `0.2338` n `20`; unknown avg `-0.1037` n `926`
- 24h: commodity avg `-0.0465` n `12`; crypto_alt avg `5.1783` n `234`; crypto_major avg `2.9015` n `8`; equity avg `1.9993` n `141`; fx avg `-0.2192` n `6`; index avg `0.3259` n `26`; metal avg `0.2722` n `20`; unknown avg `13.3047` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1441`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
