# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T17:07:25.221323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.1394` n `234`; crypto_major avg `0.0092` n `8`; equity avg `0.0075` n `141`; fx avg `-0.0012` n `6`; index avg `-0.0049` n `26`; metal avg `0.0047` n `20`; unknown avg `3.5889` n `960`
- 1h: commodity avg `-0.0172` n `12`; crypto_alt avg `0.1618` n `234`; crypto_major avg `-0.1938` n `8`; equity avg `-0.0142` n `141`; fx avg `0.0022` n `6`; index avg `-0.0147` n `26`; metal avg `0.0072` n `20`; unknown avg `3.1633` n `960`
- 4h: commodity avg `-0.1662` n `12`; crypto_alt avg `-0.0519` n `234`; crypto_major avg `-0.6282` n `8`; equity avg `0.0005` n `141`; fx avg `0.007` n `6`; index avg `-0.0079` n `26`; metal avg `0.0128` n `20`; unknown avg `7.2313` n `954`
- 24h: commodity avg `-0.1172` n `12`; crypto_alt avg `-0.7445` n `234`; crypto_major avg `-0.3339` n `8`; equity avg `0.2156` n `141`; fx avg `-0.0117` n `6`; index avg `-0.0064` n `26`; metal avg `-0.0107` n `20`; unknown avg `18.1188` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
