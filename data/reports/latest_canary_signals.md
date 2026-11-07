# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T22:52:26.030242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0052` n `13`; crypto_alt avg `-0.0713` n `239`; crypto_major avg `-0.0335` n `8`; equity avg `0.0479` n `158`; fx avg `-0.0009` n `6`; index avg `0.0001` n `27`; metal avg `-0.0014` n `20`; unknown avg `-0.1566` n `1262`
- 1h: commodity avg `-0.0056` n `13`; crypto_alt avg `0.3306` n `239`; crypto_major avg `0.1531` n `8`; equity avg `0.0544` n `158`; fx avg `-0.0105` n `6`; index avg `-0.0009` n `27`; metal avg `0.0045` n `20`; unknown avg `-0.5025` n `1250`
- 4h: commodity avg `0.0707` n `13`; crypto_alt avg `-0.5797` n `239`; crypto_major avg `-0.2951` n `8`; equity avg `-0.1912` n `158`; fx avg `-0.0076` n `6`; index avg `-0.0224` n `27`; metal avg `-0.0116` n `20`; unknown avg `-0.3612` n `1214`
- 24h: commodity avg `0.0849` n `13`; crypto_alt avg `-1.5079` n `239`; crypto_major avg `-0.7736` n `8`; equity avg `-0.1611` n `158`; fx avg `-0.0242` n `6`; index avg `0.0372` n `27`; metal avg `-0.0186` n `20`; unknown avg `146.3793` n `1097`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1631`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1247`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
