# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T22:52:29.517584+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `13`; crypto_alt avg `0.2407` n `239`; crypto_major avg `0.0988` n `8`; equity avg `-0.049` n `160`; fx avg `0.002` n `6`; index avg `0.0089` n `27`; metal avg `0.0014` n `20`; unknown avg `0.1498` n `1262`
- 1h: commodity avg `-0.0185` n `13`; crypto_alt avg `0.1685` n `239`; crypto_major avg `-0.1525` n `8`; equity avg `-0.0753` n `160`; fx avg `-0.0011` n `6`; index avg `-0.0074` n `27`; metal avg `-0.0057` n `20`; unknown avg `0.9961` n `1250`
- 4h: commodity avg `0.1204` n `13`; crypto_alt avg `0.1679` n `239`; crypto_major avg `0.2066` n `8`; equity avg `0.8114` n `160`; fx avg `-0.0036` n `6`; index avg `0.0739` n `27`; metal avg `0.0521` n `20`; unknown avg `0.793` n `1224`
- 24h: commodity avg `0.062` n `13`; crypto_alt avg `-1.2165` n `239`; crypto_major avg `-2.9407` n `8`; equity avg `-1.418` n `160`; fx avg `-0.1016` n `6`; index avg `-0.2066` n `27`; metal avg `-0.6637` n `20`; unknown avg `20.8887` n `1173`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2573`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0932`, n `668`, weak_sample_signal
