# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T09:07:27.648917+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1194` n `13`; crypto_alt avg `0.5448` n `238`; crypto_major avg `0.3735` n `8`; equity avg `0.5397` n `155`; fx avg `-0.0091` n `6`; index avg `0.1372` n `27`; metal avg `0.1089` n `20`; unknown avg `3.1542` n `1228`
- 1h: commodity avg `-0.0947` n `13`; crypto_alt avg `0.6604` n `238`; crypto_major avg `0.3141` n `8`; equity avg `0.5092` n `155`; fx avg `-0.0126` n `6`; index avg `0.1179` n `27`; metal avg `-0.0333` n `20`; unknown avg `2.2208` n `1230`
- 4h: commodity avg `-0.1158` n `13`; crypto_alt avg `-0.5621` n `238`; crypto_major avg `-0.3529` n `8`; equity avg `-0.2681` n `155`; fx avg `-0.0034` n `6`; index avg `0.0273` n `27`; metal avg `-0.1869` n `20`; unknown avg `1.1683` n `1190`
- 24h: commodity avg `-0.1922` n `13`; crypto_alt avg `-2.3821` n `238`; crypto_major avg `-1.7199` n `8`; equity avg `-1.0807` n `154`; fx avg `0.0314` n `6`; index avg `0.0251` n `27`; metal avg `-0.3761` n `20`; unknown avg `32.3793` n `968`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0825`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
