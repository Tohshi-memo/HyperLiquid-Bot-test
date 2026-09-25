# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T09:52:32.627073+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0353` n `12`; crypto_alt avg `-0.0839` n `234`; crypto_major avg `-0.2083` n `8`; equity avg `-0.1307` n `141`; fx avg `0.0183` n `6`; index avg `-0.0141` n `26`; metal avg `-0.0277` n `20`; unknown avg `0.366` n `946`
- 1h: commodity avg `0.0646` n `12`; crypto_alt avg `0.2189` n `234`; crypto_major avg `0.4091` n `8`; equity avg `-0.0224` n `141`; fx avg `-0.0124` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0325` n `20`; unknown avg `1.1677` n `944`
- 4h: commodity avg `-0.0355` n `12`; crypto_alt avg `1.4678` n `234`; crypto_major avg `0.9821` n `8`; equity avg `0.321` n `141`; fx avg `-0.024` n `6`; index avg `0.0642` n `26`; metal avg `0.1562` n `20`; unknown avg `0.0584` n `904`
- 24h: commodity avg `0.0084` n `12`; crypto_alt avg `5.08` n `234`; crypto_major avg `2.9465` n `8`; equity avg `2.1429` n `141`; fx avg `-0.1976` n `6`; index avg `0.3399` n `26`; metal avg `0.198` n `20`; unknown avg `13.4237` n `797`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1617`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
