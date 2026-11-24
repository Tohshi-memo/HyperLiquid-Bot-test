# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T10:07:27.661272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0146` n `13`; crypto_alt avg `-0.125` n `239`; crypto_major avg `-0.0833` n `8`; equity avg `-0.2404` n `166`; fx avg `0.0288` n `6`; index avg `-0.0424` n `27`; metal avg `-0.048` n `20`; unknown avg `1.14` n `1242`
- 1h: commodity avg `0.1608` n `13`; crypto_alt avg `-0.3` n `239`; crypto_major avg `0.0376` n `8`; equity avg `-0.2072` n `166`; fx avg `0.0865` n `6`; index avg `-0.0373` n `27`; metal avg `-0.0048` n `20`; unknown avg `0.9886` n `1238`
- 4h: commodity avg `0.27` n `13`; crypto_alt avg `-1.7097` n `239`; crypto_major avg `-1.1505` n `8`; equity avg `-1.8173` n `166`; fx avg `0.1152` n `6`; index avg `-0.2149` n `27`; metal avg `-0.1275` n `20`; unknown avg `0.2985` n `1208`
- 24h: commodity avg `-0.6383` n `13`; crypto_alt avg `-1.0615` n `239`; crypto_major avg `-1.1705` n `8`; equity avg `1.335` n `166`; fx avg `-0.0975` n `6`; index avg `0.349` n `27`; metal avg `-0.4126` n `20`; unknown avg `1.1172` n `1140`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1347`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0983`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
