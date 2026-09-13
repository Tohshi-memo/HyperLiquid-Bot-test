# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T00:07:29.564859+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0219` n `12`; crypto_alt avg `0.0243` n `233`; crypto_major avg `-0.0682` n `8`; equity avg `-0.0049` n `136`; fx avg `0.0017` n `6`; index avg `-0.002` n `26`; metal avg `0.0064` n `20`; unknown avg `0.0694` n `836`
- 1h: commodity avg `-0.0373` n `12`; crypto_alt avg `0.3071` n `233`; crypto_major avg `0.049` n `8`; equity avg `0.0026` n `136`; fx avg `-0.0023` n `6`; index avg `0.0009` n `26`; metal avg `0.0031` n `20`; unknown avg `-0.097` n `836`
- 4h: commodity avg `-0.0464` n `12`; crypto_alt avg `0.1315` n `233`; crypto_major avg `0.0385` n `8`; equity avg `-0.0697` n `136`; fx avg `-0.004` n `6`; index avg `-0.0148` n `26`; metal avg `-0.0214` n `20`; unknown avg `11.6168` n `796`
- 24h: commodity avg `-0.0933` n `12`; crypto_alt avg `1.3271` n `233`; crypto_major avg `0.304` n `8`; equity avg `-0.3526` n `136`; fx avg `0.0014` n `6`; index avg `-0.0193` n `26`; metal avg `0.01` n `20`; unknown avg `0.4832` n `724`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0502`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.05`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0487`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0426`, n `668`, weak_sample_signal
