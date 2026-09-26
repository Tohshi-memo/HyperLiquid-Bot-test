# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T23:22:31.280824+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0243` n `12`; crypto_alt avg `0.0151` n `234`; crypto_major avg `0.1016` n `8`; equity avg `0.009` n `141`; fx avg `-0.0042` n `6`; index avg `0.0025` n `26`; metal avg `0.0018` n `20`; unknown avg `-0.2092` n `961`
- 1h: commodity avg `0.0147` n `12`; crypto_alt avg `0.2166` n `234`; crypto_major avg `0.1866` n `8`; equity avg `0.0383` n `141`; fx avg `-0.003` n `6`; index avg `0.0006` n `26`; metal avg `0.0002` n `20`; unknown avg `2.8673` n `959`
- 4h: commodity avg `0.0597` n `12`; crypto_alt avg `-0.176` n `234`; crypto_major avg `0.2141` n `8`; equity avg `0.0587` n `141`; fx avg `-0.0072` n `6`; index avg `-0.0039` n `26`; metal avg `0.0039` n `20`; unknown avg `163.8481` n `929`
- 24h: commodity avg `0.3335` n `12`; crypto_alt avg `0.3789` n `234`; crypto_major avg `-0.7783` n `8`; equity avg `0.0027` n `141`; fx avg `0.0111` n `6`; index avg `-0.0634` n `26`; metal avg `-0.0237` n `20`; unknown avg `4.2779` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1552`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
