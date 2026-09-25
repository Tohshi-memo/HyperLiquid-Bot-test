# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T22:07:32.274526+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0059` n `12`; crypto_alt avg `0.1436` n `234`; crypto_major avg `0.0948` n `8`; equity avg `-0.0106` n `141`; fx avg `-0.0122` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0179` n `20`; unknown avg `-0.0177` n `934`
- 1h: commodity avg `0.0309` n `12`; crypto_alt avg `0.1319` n `234`; crypto_major avg `0.3095` n `8`; equity avg `0.0687` n `141`; fx avg `-0.0117` n `6`; index avg `0.0144` n `26`; metal avg `0.0049` n `20`; unknown avg `0.0991` n `934`
- 4h: commodity avg `0.0589` n `12`; crypto_alt avg `0.2807` n `234`; crypto_major avg `0.0819` n `8`; equity avg `-0.0394` n `141`; fx avg `-0.0186` n `6`; index avg `0.0243` n `26`; metal avg `0.0191` n `20`; unknown avg `0.0803` n `852`
- 24h: commodity avg `-0.4919` n `12`; crypto_alt avg `2.0551` n `234`; crypto_major avg `0.7948` n `8`; equity avg `0.1154` n `141`; fx avg `-0.2525` n `6`; index avg `0.2525` n `26`; metal avg `0.1608` n `20`; unknown avg `1183.5937` n `770`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0987`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
