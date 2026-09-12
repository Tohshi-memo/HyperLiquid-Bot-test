# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T15:07:25.393889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.0978` n `233`; crypto_major avg `0.0499` n `8`; equity avg `0.0026` n `136`; fx avg `0.0007` n `6`; index avg `0.0003` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.0296` n `836`
- 1h: commodity avg `-0.0302` n `12`; crypto_alt avg `0.2804` n `233`; crypto_major avg `0.1267` n `8`; equity avg `0.0125` n `136`; fx avg `0.0004` n `6`; index avg `0.0064` n `26`; metal avg `-0.0025` n `20`; unknown avg `3.3606` n `836`
- 4h: commodity avg `-0.0057` n `12`; crypto_alt avg `0.2254` n `233`; crypto_major avg `0.1793` n `8`; equity avg `0.0172` n `136`; fx avg `0.0047` n `6`; index avg `0.0068` n `26`; metal avg `0.0329` n `20`; unknown avg `1.3885` n `824`
- 24h: commodity avg `-0.1993` n `12`; crypto_alt avg `-0.4104` n `233`; crypto_major avg `-1.1573` n `8`; equity avg `-0.2315` n `136`; fx avg `-0.0306` n `6`; index avg `0.0276` n `26`; metal avg `-0.0563` n `20`; unknown avg `10.524` n `694`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0726`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
