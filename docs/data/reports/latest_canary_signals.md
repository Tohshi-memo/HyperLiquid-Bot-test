# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T09:37:24.202722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0021` n `12`; crypto_alt avg `0.0609` n `230`; crypto_major avg `-0.0061` n `8`; equity avg `-0.1118` n `102`; fx avg `-0.0001` n `6`; index avg `-0.0273` n `25`; metal avg `-0.1077` n `20`; unknown avg `0.0343` n `774`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `0.0779` n `230`; crypto_major avg `0.0888` n `8`; equity avg `-0.0912` n `102`; fx avg `0.0007` n `6`; index avg `-0.0436` n `25`; metal avg `-0.1331` n `20`; unknown avg `-0.0114` n `774`
- 4h: commodity avg `-0.2876` n `12`; crypto_alt avg `0.0389` n `230`; crypto_major avg `-0.0449` n `8`; equity avg `0.1362` n `102`; fx avg `-0.0064` n `6`; index avg `0.049` n `25`; metal avg `0.0042` n `20`; unknown avg `0.054` n `758`
- 24h: commodity avg `-0.4405` n `12`; crypto_alt avg `-3.5301` n `230`; crypto_major avg `-3.5849` n `8`; equity avg `-4.1604` n `102`; fx avg `-0.1496` n `6`; index avg `-0.8954` n `25`; metal avg `-0.5527` n `20`; unknown avg `998.1699` n `757`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1523`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
