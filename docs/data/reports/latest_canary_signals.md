# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T07:52:34.898273+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0425` n `12`; crypto_alt avg `0.0831` n `234`; crypto_major avg `-0.1206` n `8`; equity avg `-0.0435` n `141`; fx avg `-0.0157` n `6`; index avg `-0.0072` n `26`; metal avg `-0.0308` n `20`; unknown avg `3.1606` n `945`
- 1h: commodity avg `-0.0612` n `12`; crypto_alt avg `0.3374` n `234`; crypto_major avg `0.5948` n `8`; equity avg `0.2465` n `141`; fx avg `-0.0258` n `6`; index avg `0.0424` n `26`; metal avg `0.1338` n `20`; unknown avg `2.3419` n `943`
- 4h: commodity avg `0.1861` n `12`; crypto_alt avg `1.4237` n `234`; crypto_major avg `1.118` n `8`; equity avg `-0.1413` n `141`; fx avg `-0.0116` n `6`; index avg `-0.0301` n `26`; metal avg `0.1044` n `20`; unknown avg `1.1149` n `921`
- 24h: commodity avg `0.5512` n `12`; crypto_alt avg `-3.3261` n `234`; crypto_major avg `-2.98` n `8`; equity avg `-1.9129` n `140`; fx avg `-0.0621` n `6`; index avg `-0.3864` n `26`; metal avg `-0.3386` n `20`; unknown avg `587.2056` n `821`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1563`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1534`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1186`, n `668`, weak_sample_signal
