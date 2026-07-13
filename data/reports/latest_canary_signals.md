# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T02:22:23.999996+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0415` n `12`; crypto_alt avg `0.4021` n `230`; crypto_major avg `0.3694` n `8`; equity avg `0.3764` n `92`; fx avg `-0.0036` n `6`; index avg `0.0993` n `25`; metal avg `0.0121` n `20`; unknown avg `0.097` n `766`
- 1h: commodity avg `-0.0241` n `12`; crypto_alt avg `-0.4209` n `230`; crypto_major avg `-0.4038` n `8`; equity avg `-0.4276` n `92`; fx avg `0.021` n `6`; index avg `-0.0784` n `25`; metal avg `0.0059` n `20`; unknown avg `0.2085` n `766`
- 4h: commodity avg `0.0572` n `12`; crypto_alt avg `-0.1012` n `230`; crypto_major avg `-0.0071` n `8`; equity avg `-1.2644` n `92`; fx avg `0.0795` n `6`; index avg `-0.2812` n `25`; metal avg `-0.071` n `20`; unknown avg `-0.1063` n `765`
- 24h: commodity avg `0.0563` n `12`; crypto_alt avg `-1.1184` n `230`; crypto_major avg `-0.4018` n `8`; equity avg `-1.5484` n `92`; fx avg `0.0139` n `6`; index avg `-0.33` n `25`; metal avg `-0.3129` n `20`; unknown avg `0.0892` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1872`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1195`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1119`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
