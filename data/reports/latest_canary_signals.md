# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T07:07:27.796582+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0167` n `13`; crypto_alt avg `-0.1404` n `238`; crypto_major avg `-0.0454` n `8`; equity avg `-0.0476` n `155`; fx avg `0.0049` n `6`; index avg `-0.0001` n `27`; metal avg `0.0395` n `20`; unknown avg `1.0549` n `1230`
- 1h: commodity avg `0.0434` n `13`; crypto_alt avg `-0.7269` n `238`; crypto_major avg `-0.4065` n `8`; equity avg `-0.3476` n `155`; fx avg `-0.005` n `6`; index avg `-0.032` n `27`; metal avg `0.078` n `20`; unknown avg `0.9678` n `1228`
- 4h: commodity avg `0.0022` n `13`; crypto_alt avg `-0.3811` n `238`; crypto_major avg `0.1052` n `8`; equity avg `0.185` n `155`; fx avg `0.0024` n `6`; index avg `0.1338` n `27`; metal avg `-0.0734` n `20`; unknown avg `0.2365` n `1184`
- 24h: commodity avg `-0.2086` n `13`; crypto_alt avg `-2.3412` n `238`; crypto_major avg `-1.4288` n `8`; equity avg `-1.3414` n `154`; fx avg `0.0234` n `6`; index avg `-0.0219` n `27`; metal avg `-0.2197` n `20`; unknown avg `30.2956` n `968`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
