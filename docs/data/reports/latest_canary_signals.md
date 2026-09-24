# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-24T00:22:30.681669+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.047` n `12`; crypto_alt avg `-0.1823` n `234`; crypto_major avg `-0.0725` n `8`; equity avg `-0.0246` n `141`; fx avg `0.0012` n `6`; index avg `0.0002` n `26`; metal avg `-0.0585` n `20`; unknown avg `0.1609` n `945`
- 1h: commodity avg `-0.0371` n `12`; crypto_alt avg `-0.0134` n `234`; crypto_major avg `0.1589` n `8`; equity avg `-0.1255` n `141`; fx avg `0.001` n `6`; index avg `-0.0282` n `26`; metal avg `-0.108` n `20`; unknown avg `0.004` n `937`
- 4h: commodity avg `-0.1524` n `12`; crypto_alt avg `0.2503` n `234`; crypto_major avg `0.5552` n `8`; equity avg `-0.0179` n `141`; fx avg `-0.0105` n `6`; index avg `-0.0263` n `26`; metal avg `-0.0603` n `20`; unknown avg `-0.4445` n `911`
- 24h: commodity avg `0.3747` n `12`; crypto_alt avg `-4.881` n `234`; crypto_major avg `-3.6639` n `8`; equity avg `-1.7745` n `140`; fx avg `0.0659` n `6`; index avg `-0.3782` n `26`; metal avg `-0.9316` n `20`; unknown avg `583.4262` n `821`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1286`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1249`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
