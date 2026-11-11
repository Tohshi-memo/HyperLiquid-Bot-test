# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T06:52:25.136382+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0463` n `13`; crypto_alt avg `-0.3847` n `239`; crypto_major avg `-0.4914` n `8`; equity avg `-0.2222` n `161`; fx avg `-0.0034` n `6`; index avg `-0.0131` n `27`; metal avg `-0.0083` n `20`; unknown avg `-0.1391` n `1261`
- 1h: commodity avg `0.0561` n `13`; crypto_alt avg `-0.7743` n `239`; crypto_major avg `-0.6089` n `8`; equity avg `-0.0992` n `161`; fx avg `-0.0227` n `6`; index avg `0.0009` n `27`; metal avg `-0.0207` n `20`; unknown avg `-0.1229` n `1223`
- 4h: commodity avg `0.0186` n `13`; crypto_alt avg `-0.9189` n `239`; crypto_major avg `-0.4222` n `8`; equity avg `0.9238` n `161`; fx avg `-0.0575` n `6`; index avg `0.1442` n `27`; metal avg `0.2015` n `20`; unknown avg `1.4072` n `1213`
- 24h: commodity avg `0.4524` n `13`; crypto_alt avg `-1.6698` n `239`; crypto_major avg `-2.7619` n `8`; equity avg `1.6708` n `161`; fx avg `-0.1919` n `6`; index avg `0.2247` n `27`; metal avg `-0.0777` n `20`; unknown avg `1.3704` n `1160`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1393`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
