# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T03:52:32.686289+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0077` n `13`; crypto_alt avg `-0.0533` n `235`; crypto_major avg `0.0401` n `8`; equity avg `0.0112` n `150`; fx avg `0.0007` n `6`; index avg `0.0014` n `26`; metal avg `-0.0122` n `20`; unknown avg `1.4969` n `1116`
- 1h: commodity avg `0.0379` n `13`; crypto_alt avg `-0.2185` n `235`; crypto_major avg `-0.1696` n `8`; equity avg `0.005` n `150`; fx avg `-0.0004` n `6`; index avg `-0.0005` n `26`; metal avg `0.0077` n `20`; unknown avg `0.5984` n `1114`
- 4h: commodity avg `-0.0287` n `13`; crypto_alt avg `0.483` n `235`; crypto_major avg `0.179` n `8`; equity avg `0.0868` n `150`; fx avg `0.0051` n `6`; index avg `0.0342` n `26`; metal avg `0.0182` n `20`; unknown avg `0.1123` n `1108`
- 24h: commodity avg `0.0278` n `13`; crypto_alt avg `1.8654` n `235`; crypto_major avg `0.0961` n `8`; equity avg `0.4702` n `150`; fx avg `-0.0228` n `6`; index avg `0.0682` n `26`; metal avg `0.1586` n `20`; unknown avg `12.9609` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1459`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1283`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1207`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0911`, n `668`, weak_sample_signal
