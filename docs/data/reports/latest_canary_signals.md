# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-29T06:37:28.661185+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0417` n `13`; crypto_alt avg `0.0317` n `238`; crypto_major avg `0.0917` n `8`; equity avg `-0.0815` n `155`; fx avg `0.0003` n `6`; index avg `-0.0117` n `27`; metal avg `-0.0085` n `20`; unknown avg `-0.051` n `1234`
- 1h: commodity avg `0.0793` n `13`; crypto_alt avg `-0.7806` n `238`; crypto_major avg `-0.4678` n `8`; equity avg `-0.4645` n `155`; fx avg `-0.0128` n `6`; index avg `-0.0696` n `27`; metal avg `-0.1411` n `20`; unknown avg `-0.2913` n `1210`
- 4h: commodity avg `-0.041` n `13`; crypto_alt avg `0.3458` n `238`; crypto_major avg `0.6527` n `8`; equity avg `0.5382` n `155`; fx avg `-0.0011` n `6`; index avg `0.1868` n `27`; metal avg `-0.16` n `20`; unknown avg `0.7214` n `1176`
- 24h: commodity avg `-0.1867` n `13`; crypto_alt avg `-2.2571` n `238`; crypto_major avg `-1.3498` n `8`; equity avg `-1.2493` n `154`; fx avg `0.0426` n `6`; index avg `-0.02` n `27`; metal avg `-0.2888` n `20`; unknown avg `30.4903` n `970`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1116`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0756`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0634`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0631`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
