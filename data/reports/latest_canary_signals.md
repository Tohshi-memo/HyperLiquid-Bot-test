# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T04:22:30.939777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.1218` n `229`; crypto_major avg `0.2121` n `8`; equity avg `0.0541` n `88`; fx avg `0.0` n `6`; index avg `0.0021` n `25`; metal avg `0.0035` n `20`; unknown avg `-0.1179` n `765`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `0.1347` n `229`; crypto_major avg `0.3182` n `8`; equity avg `0.0809` n `88`; fx avg `-0.0026` n `6`; index avg `-0.0093` n `25`; metal avg `0.0071` n `20`; unknown avg `0.3886` n `765`
- 4h: commodity avg `0.0458` n `12`; crypto_alt avg `-0.7023` n `229`; crypto_major avg `-0.6008` n `8`; equity avg `0.1393` n `88`; fx avg `-0.0022` n `6`; index avg `-0.0025` n `25`; metal avg `-0.0173` n `20`; unknown avg `-0.0612` n `763`
- 24h: commodity avg `0.0629` n `12`; crypto_alt avg `-0.7363` n `229`; crypto_major avg `-0.8417` n `8`; equity avg `0.2261` n `88`; fx avg `-0.0047` n `6`; index avg `0.0239` n `25`; metal avg `0.0788` n `20`; unknown avg `-0.8819` n `741`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1092`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0646`, n `668`, weak_sample_signal
