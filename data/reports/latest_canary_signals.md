# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T10:37:27.894489+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0055` n `12`; crypto_alt avg `0.006` n `230`; crypto_major avg `0.0679` n `8`; equity avg `-0.0895` n `102`; fx avg `0.0063` n `6`; index avg `-0.026` n `25`; metal avg `0.0179` n `20`; unknown avg `-0.0021` n `774`
- 1h: commodity avg `0.0845` n `12`; crypto_alt avg `-0.0141` n `230`; crypto_major avg `-0.125` n `8`; equity avg `-0.3205` n `102`; fx avg `-0.0385` n `6`; index avg `-0.0579` n `25`; metal avg `-0.0988` n `20`; unknown avg `-0.0172` n `774`
- 4h: commodity avg `-0.0387` n `12`; crypto_alt avg `-0.1434` n `230`; crypto_major avg `-0.1997` n `8`; equity avg `-0.114` n `102`; fx avg `-0.0439` n `6`; index avg `-0.0388` n `25`; metal avg `-0.1968` n `20`; unknown avg `-0.0223` n `774`
- 24h: commodity avg `-0.4341` n `12`; crypto_alt avg `-3.6008` n `230`; crypto_major avg `-3.7677` n `8`; equity avg `-4.4622` n `102`; fx avg `-0.1795` n `6`; index avg `-0.9371` n `25`; metal avg `-0.6948` n `20`; unknown avg `998.1159` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1391`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
